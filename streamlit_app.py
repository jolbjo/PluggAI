import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("📘 AI Math 2b Tutor 🇸🇪")
user_question = st.text_input("What's your math question?")

if user_question:
    prompt = f"""
    You are a helpful AI tutor for Swedish high school students studying Math 2b.
    Help the student solve this problem with Socratic questioning.
    Guide them step by step, without giving the final answer immediately.

    Problem: {user_question}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    st.write(response['choices'][0]['message']['content'])
