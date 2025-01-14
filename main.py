from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# CORS settings
origins = [
    "http://localhost:5174",  # Your React app origin
    "http://localhost:3000",  # Add any other frontend origin if needed
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

# Configure the Generative AI model
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Store the chat session globally
chat_session = None

# Initialize the chat session with status codes context
def initialize_chat():
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

# Chat endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        initialize_chat()  # Ensure chat session is initialized
        response = chat_session.send_message(request.message)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error in generating response")


# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
