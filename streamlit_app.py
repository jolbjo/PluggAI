import streamlit as st
import openai

st.title("📘 AI Math 2b Tutor 🇸🇪")

# Set your API key
openai.api_key = st.secrets["openai"]["api_key"]

def ask_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another engine like "gpt-4", depending on your plan
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,  # Controls randomness in the output; lower = more focused
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, there was an error processing your request."

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
    
    # If it's the first step, introduce the problem
    if step == 0:
        st.write("Let's start with a problem! A streetlight is 10 meters away from a person.")
        st.write("The person's shadow is 4.2 meters long. If the person is 2.1 meters tall, what is the height of the streetlight?")
        st.write("Now, let's begin with the first question.")

    # Ask Socratic questions based on the current step
    if step < len(steps):
        st.write(steps[step]["question"])
        user_input = st.text_area("Your answer:", height=150)  # Use text_area for multi-line input
        
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
    # Start the Socratic steering process
    socratic_steering_step()

if __name__ == "__main__":
    main()

