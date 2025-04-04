import streamlit as st
import openai

st.title("📘 AI Math 2b Tutor 🇸🇪")

# Set your API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Get user input
question = st.text_input("Ask a math question:")

if question:
    try:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a helpful math tutor."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response["choices"][0]["message"]["content"]
            st.success(answer)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
