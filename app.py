import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found. Please add GEMINI_API_KEY in your .env file.")
else:
    st.title("💼 Marketing Assistant Chatbot")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

    memory = ConversationBufferMemory(return_messages=True)
    conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

    st.markdown("### 🤖 Your Expert Marketing Assistant")
    st.write(
        """
        This chatbot helps you with:
        - Lead generation strategies  
        - Project selling frameworks & templates  
        - Marketing process structures (flowcharts, steps, templates)  
        - Client management tips  

        Ask me anything about marketing, sales, or proposals!
        """
    )

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("💬 Ask your question:")

    if user_input:
        response = conversation.run(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

    for role, message in st.session_state.history:
        if role == "You":
            st.markdown(f"**🧑 {role}:** {message}")
        else:
            st.markdown(f"**🤖 {role}:** {message}")
