from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Please check your environment variables.")

# Configure Generative AI
genai.configure(api_key=api_key)

# Initialize FastAPI app
app = FastAPI()

# CORS settings
origins = [
    "http://localhost:5174",  # Your React app origin
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Pydantic models for request and response
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# Store the chat session globally
chat_session = None

# Initialize the chat session
def get_chat_session():
    global chat_session
    if chat_session is None:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "chat with me with the help of status codes",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Okay, let's chat! I'm ready to respond using HTTP status codes as a subtle (and hopefully fun) way to add context to our conversation.\n\nI'll start with a **200 OK**. This means I'm ready and willing to chat.\n\nHow are you doing today? What's on your mind?",
                    ],
                },
            ]
        )
    return chat_session

# Chat endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, session=Depends(get_chat_session)):
    try:
        response = session.send_message(request.message)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
