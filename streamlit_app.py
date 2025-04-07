import streamlit as st
import openai

st.title("📘 AI Math 2b Tutor 🇸🇪")

# Set your API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

def ask_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Or another engine like "gpt-4", depending on your plan
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,  # Controls randomness in the output; lower = more focused
    )
    return response.choices[0].text.strip()

# Function to handle Socratic steering
def socratic_steering_step():
    if "step" not in st.session_state:
        st.session_state.step = 0  # Start with step 0 (first question)

    # Define your Socratic questions for each step
    steps = [
        {
            "question": "What do you think is the first step in solving the problem?",
            "hint": "You can use the concept of similar triangles to set up a proportion."
        },
        {
            "question": "Can you express this proportion mathematically?",
            "hint": "Think about how you could write a proportion between the heights and shadows."
        },
        {
            "question": "What happens if you solve this proportion for the height of the streetlight?",
            "hint": "Try to solve for the height using cross-multiplication."
        }
    ]
    
    # Handle conversation flow
    step = st.session_state.step
    if step < len(steps):
        st.write(steps[step]["question"])
        user_input = st.text_input("Your answer:")
        
        if user_input:
            # Call OpenAI's ask_openai to get a hint or guidance based on the user input
            ai_response = ask_openai(f"User answer: {user_input}. Can you provide a hint or feedback for solving the math problem?")
            
            # Display AI-generated feedback
            st.write("AI's Feedback: " + ai_response)
            
            # Check if the answer is correct (this can be refined, for now using a basic match)
            if "height of the streetlight is 5 meters" in user_input.lower():
                st.session_state.step += 1  # Move to the next step
                st.write("Great! Let's move on to the next step.")
            else:
                st.write(f"Not quite. {steps[step]['hint']}")  # Provide hint for next step
    else:
        st.write("Congratulations! You've solved the problem.")

# Streamlit App
def main():
    st.title("Socratic Steering Math Tutor")

    # Initialize session state if needed
    if "step" not in st.session_state:
        st.session_state.step = 0

    # Start the Socratic steering process
    socratic_steering_step()

if __name__ == "__main__":
    main()
