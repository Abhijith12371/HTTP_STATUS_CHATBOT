import axios from 'axios';
import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

const ChatForm = () => {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleMessage = async () => {
        if (!message.trim()) {
            setError('Message cannot be empty');
            return;
        }

        setLoading(true);
        setError('');
        setResponse('');

        try {
            const res = await axios.post(
                `http://127.0.0.1:8000/chat`,
                { message },
                { headers: { 'Content-Type': 'application/json' } }
            );
            setResponse(res.data.response);
        } catch (err) {
            setError('Failed to send message. Please try again.');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-gray-100 min-h-screen flex items-center justify-center">
            <div className="bg-white shadow-md rounded-lg p-6 max-w-md w-full">
                <h1 className="text-2xl font-bold text-gray-800 mb-4">Chat with Bot</h1>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Type your message"
                    className="w-full border border-gray-300 rounded-lg p-3 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button
                    onClick={handleMessage}
                    disabled={loading}
                    className={`w-full text-white font-bold py-2 px-4 rounded-lg ${
                        loading
                            ? 'bg-blue-300 cursor-not-allowed'
                            : 'bg-blue-500 hover:bg-blue-600'
                    }`}
                >
                    {loading ? 'Sending...' : 'Send'}
                </button>
                {error && <p className="text-red-500 mt-4">{error}</p>}
                {response && (
                    <div className="bg-green-100 p-4 mt-4 rounded-lg">
                        <p className="text-green-800 font-semibold">Response:</p>
                        <ReactMarkdown className="prose prose-green text-gray-700">{response}</ReactMarkdown>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ChatForm;
