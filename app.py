import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
st.title("Multi Model ChatBot")


option = st.selectbox(
    "AI Model", 
    ("open ai", "google ai", "anthropic", "grok")
)


query = st.text_input("User question : ", "What is Machine learning")


if st.button("submit"):
    
    match option:
        case "open ai":
            from langchain_openai import ChatOpenAI

            llm = ChatOpenAI(
                model="gpt-4o-mini",
                api_key=st.secrets["OPENAI_API_KEY"],  # Pulls securely from secrets.toml
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)

        case "google ai":
            from langchain_google_genai import ChatGoogleGenerativeAI

            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                google_api_key=st.secrets["GOOGLE_API_KEY"],
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)

        case "anthropic":
            from langchain_anthropic import ChatAnthropic

            llm = ChatAnthropic(
                model="claude-3-5-sonnet-latest",
                api_key=st.secrets["ANTHROPIC_API_KEY"],
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)

        case "grok":
            from langchain_groq import ChatGroq

            llm = ChatGroq(
                model="llama-3.3-70b-specdec",
                api_key=st.secrets["GROQ_API_KEY"],
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)
    
