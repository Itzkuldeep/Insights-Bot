# GlimpseBot

**GlimpseBot** is an intelligent chatbot built using Streamlit and Google Generative AI. It allows users to ask questions and receive insightful answers while maintaining a history of previous chats with a "glimpse" feature, which shows a preview of previous queries and responses.

## Features
- **Streamlined UI** with a modern design using Streamlit.
- **Chat Glimpse**: Displays a short preview of previous chats, expandable for full conversation.
- **Model Selection**: Choose from multiple AI models.
- **Error Handling**: Gracefully handles API errors and invalid inputs.
- **Response Spinner**: Shows a loading spinner while generating responses.

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/glimpsebot.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your environment variables in a `.env` file:
    ```
    GOOGLE_API_KEY=your_api_key
    ```
4. Run the app:
    ```bash
    streamlit run app.py
    ```

## Future Enhancements
- Add more AI models for generating diverse responses.
- Integrate user feedback for improving answers.

## License
This project is licensed under the MIT License.
