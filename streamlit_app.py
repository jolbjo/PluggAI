import streamlit as st
import openai

st.title("📘 AI Math 2b Tutor 🇸🇪")

# Set your API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_input("Ask me a question")

if user_input:
    socratic = socratic_response(user_input)  # First, try Socratic steering
    if socratic:
        st.write(socratic)  # If Socratic, show the response
    else:
        # If no Socratic response, fallback to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or o3-mini, depending on your setup
            messages=[{"role": "user", "content": user_input}]
        )
        st.write(response.choices[0].message.content)

def socratic_response(user_input):
    # Simple examples, you can expand this list
    if "9/3" in user_input:
        return "Let’s think: if you divide 9 into 3 equal parts, how many would be in each group?"
    elif "f(x) = 2x + 1" in user_input and "x=4" in user_input:
        return "Okay! Try plugging 4 into x. What's 2 times 4, and then add 1?"
    elif "derivative of x^2" in user_input:
        return "Great question. What does taking the derivative mean? What happens to the exponent?"
    else:
        return None

def socratic_steering(problem_type):
    if problem_type == "streetlight_and_shadow":
        # Step 1: Ask about proportional reasoning
        st.write("Let's solve the problem using proportional reasoning.")
        st.write("What is the relationship between the height of Patrik and the length of his shadow?")
        
        # Step 2: Ask the user to set up the proportion
        st.write("Can you set up a proportion between the height of Patrik and the streetlight, and their respective shadows?")
        # We can guide the user to write something like: (height of Patrik / shadow of Patrik) = (height of streetlight / shadow of streetlight)
        
        st.write("Now, can you solve for the height of the streetlight?")
        
        # Provide solution if necessary
        st.write("The proportion is: (2.1 / 4.2) = (height of streetlight / 10)")
        st.write("Now, solve for the height of the streetlight!")
        
        # Answer
        st.write("The height of the streetlight should be: 5 meters.")

def algebra_problem(problem_type):
    if problem_type == "algebra_equation":
        # Step 1: Ask the student to distribute
        st.write("Let's simplify the equation: 2(x + 4) - 4(1 - 2x) = 0")
        st.write("First, what happens if you distribute the 2 across (x + 4)?")
        
        # Step 2: Guide through the simplification process
        st.write("Now simplify -4(1 - 2x). What do you get?")
        
        # Step 3: Ask the user to combine like terms
        st.write("Can you combine the like terms now? What do you get?")
        
        # Final step: Solve for x
        st.write("Now, solve for x.")
        
        # Solution
        st.write("After simplification, you should have: 2x + 8 - 4 + 8x = 0, which simplifies to 10x + 4 = 0.")
        st.write("Now, solve for x: x = -4/10 = -0.4")

def graphing_problem(problem_type):
    if problem_type == "y_intercept":
        st.write("The equation is: y = ax^2 + bx + c.")
        st.write("Where does this graph cross the y-axis?")
        
        st.write("Can you recall what happens when the graph crosses the y-axis?")
        st.write("At the y-axis, the value of x is 0.")
        
        # Step 2: Substitute x = 0 into the equation
        st.write("Let’s substitute x = 0 into the equation. What does the equation become?")
        
        st.write("y = a(0)^2 + b(0) + c. So the y-intercept is y = c.")
        
        # Conclusion
        st.write("Therefore, the graph crosses the y-axis at y = c.")

def main():
    st.title("Socratic Steering Math Tutor")

    problem_type = st.selectbox("Choose a problem type", ["Streetlight and Shadow", "Algebra Equation", "Graphing Equation"])
    
    if problem_type == "Streetlight and Shadow":
        socratic_steering("streetlight_and_shadow")
    elif problem_type == "Algebra Equation":
        algebra_problem("algebra_equation")
    elif problem_type == "Graphing Equation":
        graphing_problem("y_intercept")

if __name__ == "__main__":
    main()
