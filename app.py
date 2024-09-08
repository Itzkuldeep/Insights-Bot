# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# #--------------LOGICS
# model = genai.GenerativeModel("gemini-pro")
# def get_ideas(query):
#     response = model.generate_content(query)
#     return response.text

# ### Streamlit for UI

# st.set_page_config(page_title="The Bot")

# st.header("The Bot")

# input = st.text_input("Input: ", key="input")
# submit = st.button("Ask the Question")

# if submit:
#     response = get_ideas(input)
#     st.subheader("Your answer is: ")
#     st.write(response)

# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st
# import os
# import google.generativeai as genai

# # Configure the API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Logic Enhancements
# model = genai.GenerativeModel("gemini-pro")

# def get_ideas(query):
#     try:
#         response = model.generate_content(query)
#         return response.text
#     except Exception as e:
#         return f"Error occurred: {str(e)}"

# # Streamlit UI Enhancements
# st.set_page_config(page_title="The Bot", layout="wide")
# st.header("The Enhanced Bot")

# # Sidebar for additional controls
# st.sidebar.title("Settings")
# st.sidebar.subheader("Choose the model:")
# model_choice = st.sidebar.selectbox("Select a model", ["gemini-pro", "model-2"])

# input = st.text_input("Input your question: ", key="input")
# submit = st.button("Ask the Question")

# if submit:
#     with st.spinner("Thinking..."):
#         response = get_ideas(input)
    
#     # Display the response
#     st.subheader("Your answer is: ")
#     st.write(response)

#     # Save chat history
#     if "history" not in st.session_state:
#         st.session_state.history = []
    
#     st.session_state.history.append({"query": input, "response": response})
    
#     # Display chat history
#     if st.session_state.history:
#         st.sidebar.write("**Previous Chats:**")
#         for chat in st.session_state.history:
#             st.sidebar.write(f"**You:** {chat['query']}")
#             st.sidebar.write(f"**Bot:** {chat['response']}")
#             st.sidebar.write("---")



from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

# Configure the API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Logic Enhancements
model = genai.GenerativeModel("gemini-pro")

def get_ideas(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Streamlit UI Enhancements
st.set_page_config(page_title="The Bot", layout="wide")
st.header("The Enhanced Bot")

# Sidebar for additional controls
st.sidebar.title("Settings")
st.sidebar.subheader("Choose the model:")
model_choice = st.sidebar.selectbox("Select a model", ["gemini-pro", "model-2"])

input = st.text_input("Input your question: ", key="input")
submit = st.button("Ask the Question")

if submit:
    with st.spinner("Thinking..."):
        response = get_ideas(input)
    
    # Display the response
    st.subheader("Your answer is: ")
    st.write(response)

    # Save chat history
    if "history" not in st.session_state:
        st.session_state.history = []
    
    st.session_state.history.append({"query": input, "response": response})
    
    # Display chat history with glimpses
    if st.session_state.history:
        st.sidebar.write("**Previous Chats:**")
        for i, chat in enumerate(st.session_state.history):
            query_preview = chat['query'][:30] + "..." if len(chat['query']) > 30 else chat['query']
            response_preview = chat['response'][:30] + "..." if len(chat['response']) > 30 else chat['response']
            
            with st.sidebar.expander(f"Chat {i + 1}: {query_preview}"):
                st.write(f"**Full Query:** {chat['query']}")
                st.write(f"**Full Response:** {chat['response']}")
                st.write(f"**Preview Response:** {response_preview}")