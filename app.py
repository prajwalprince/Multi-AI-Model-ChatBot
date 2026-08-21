import streamlit as st

st.title("Multi Model ChatBot")

# Dropdown menu for selecting the model
option = st.selectbox(
    "AI Model", 
    ("open ai", "google ai", "anthropic", "grok")
)

# User input text field
query = st.text_input("User question : ", "What is Machine learning")

# Submit button to trigger the API call
if st.button("Ask"):
    # Python's match-case syntax (No curly braces)
    match option:
        case "open ai":
            from langchain_openai import ChatOpenAI

            llm = ChatOpenAI(
                model="gpt-4o-mini",
                api_key="your-openai-api-key",  # Replace with safe keys
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)

        case "google ai":
            from langchain_google_genai import ChatGoogleGenerativeAI

            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                google_api_key="your-google-api-key",
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)

        case "anthropic":
            from langchain_anthropic import ChatAnthropic

            llm = ChatAnthropic(
                model="claude-3-5-sonnet-latest",
                api_key="your-anthropic-api-key",
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)

        case "grok":  # Fixed the 'groc' typo to match the selectbox
            from langchain_groq import ChatGroq

            llm = ChatGroq(
                model="llama-3.3-70b-specdec",
                api_key="your-groq-api-key",
                temperature=0
            )
            response = llm.invoke(query)
            st.write(response.content)
