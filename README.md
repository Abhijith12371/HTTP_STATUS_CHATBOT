# Server Messaging Chatbot

Welcome to the **Server Messaging Chatbot**! This project is a full-stack application that consists of a Flask backend server and a Vite front-end project using React and Tailwind CSS for styling.

---

## Project Structure

```
root
├── main.py               # Flask backend server
├── index.html            # Vite entry HTML file
├── package.json          # Front-end dependencies
├── src/                  # Front-end source files
│   └── components/       # React components
│       └── ChatBox.jsx   # Main chatbox component
├── main.js               # Vite entry JavaScript file
├── vite.config.js        # Vite configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Getting Started

### Backend Setup (Flask)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/server-messaging-chatbot.git
   cd server-messaging-chatbot
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate
   ```

3. **Install backend dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server:**

   ```bash
   python main.py
   ```

---

### Frontend Setup (Vite with Tailwind CSS)

1. **Navigate to the project directory:**

   ```bash
   cd vite-project
   ```

2. **Install front-end dependencies:**

   ```bash
   npm install
   ```

3. **Set up Tailwind CSS:**
   
   Create a `tailwind.config.js` file if not already present and configure it:

   ```javascript
   module.exports = {
     content: ['./index.html', './src/**/*.{js,jsx}'],
     theme: {
       extend: {},
     },
     plugins: [],
   };
   ```

   Include Tailwind directives in your CSS file (e.g., `src/index.css`):

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

4. **Start the Vite development server:**

   ```bash
   npm run dev
   ```

5. **Open the application in your browser:**
   Visit `http://localhost:5173` to see the chatbot in action.

---

## Usage

1. Enter a message in the input field.
2. Click the **Send** button to communicate with the bot.
3. The bot's response will be displayed below your message.

---

## Technologies Used

- **Python** (Flask) for the backend
- **JavaScript** (Vite + React) for the frontend
- **Tailwind CSS** for styling

---

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this project.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Author

Created by Abhijith(https://github.com/Abhijith12371).

