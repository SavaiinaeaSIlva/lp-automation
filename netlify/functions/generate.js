// File: netlify/functions/generate.js

// 1. Import the Google AI library
const { GoogleGenerativeAI } = require("@google/generative-ai");

// 2. Access your API key securely from Netlify's environment variables
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

// 3. This is the main function Netlify will run
exports.handler = async function(event, context) {
  // Only allow POST requests
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  try {
    // Get the user's prompt from the request
    const { prompt } = JSON.parse(event.body);

    if (!prompt) {
      return { statusCode: 400, body: "Bad Request: No prompt provided." };
    }

    // Call the Gemini API
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();

    // Send the AI's response back to the frontend
    return {
      statusCode: 200,
      body: JSON.stringify({ reply: text })
    };

  } catch (error) {
    console.error("Error calling Gemini API:", error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: "Sorry, something went wrong." })
    };
  }
};
