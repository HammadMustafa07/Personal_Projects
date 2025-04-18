import streamlit as st
import random
import time

st.title("🐍 Simple Python Quiz")

# Questions List
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pyth", ".pt", ".py", ".pyt"],
        "answer": ".py",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def",
    },
    {
        "question": "How do you insert comments in Python code?",
        "options": ["// This is a comment", "# This is a comment", "/* comment */", "-- comment"],
        "answer": "# This is a comment",
    },
    {
        "question": "What is the output of: print(2 + 3 * 2)?",
        "options": ["10", "12", "8", "7"],
        "answer": "8",
    },
    {
        "question": "What data type is x = 'Hello World'?",
        "options": ["int", "str", "bool", "float"],
        "answer": "str",
    },
    {
        "question": "Which one is a list in Python?",
        "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "<1, 2, 3>"],
        "answer": "[1, 2, 3]",
    },
    {
        "question": "Which function gets user input?",
        "options": ["input()", "get()", "read()", "scan()"],
        "answer": "input()",
    },
    {
        "question": "How do you start a while loop?",
        "options": ["loop while", "while x > 0", "while (x > 0)", "while: x > 0"],
        "answer": "while x > 0",
    },
    {
        "question": "How do you start a for loop?",
        "options": ["loop x in y", "foreach x in y", "for x to y", "for x in y"],
        "answer": "for x in y",
    },
    {
        "question": "Which symbol checks equality?",
        "options": ["=", "==", "===", "!="],
        "answer": "==",
    },
    {
        "question": "Create a variable with value 5?",
        "options": ["x = 5", "x := 5", "int x = 5", "num x = 5"],
        "answer": "x = 5",
    },
    {
        "question": "Data type for decimal numbers?",
        "options": ["int", "str", "bool", "float"],
        "answer": "float",
    },
    {
        "question": "Operator for exponentiation?",
        "options": ["^", "**", "^^", "exp()"],
        "answer": "**",
    },
    {
        "question": "What does len() do?",
        "options": ["Find size of file", "Calculate sum", "Length of object", "Log errors"],
        "answer": "Length of object",
    },
    {
        "question": "Convert string to integer?",
        "options": ["int()", "float()", "str()", "bool()"],
        "answer": "int()",
    },
    {
        "question": "Which is a tuple?",
        "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "<1, 2, 3>"],
        "answer": "(1, 2, 3)",
    },
    {
        "question": "Keyword to handle exceptions?",
        "options": ["try", "check", "error", "except"],
        "answer": "except",
    },
    {
        "question": "Output of print(type(10))?",
        "options": ["int", "<class 'int'>", "type int", "number"],
        "answer": "<class 'int'>",
    },
    {
        "question": "Which is NOT a valid Python data type?",
        "options": ["list", "float", "array", "bool"],
        "answer": "array",
    },
    {
        "question": "Check if a != b?",
        "options": ["a != b", "a =! b", "a <> b", "a not = b"],
        "answer": "a != b",
    },
]

# Initialize session state variables
if "question_order" not in st.session_state:
    st.session_state.question_order = random.sample(range(len(questions)), len(questions))  # shuffled index list
    st.session_state.question_index = 0  # current question index
    st.session_state.score = 0

# Check if quiz is complete
if st.session_state.question_index >= len(questions):
    st.success(f"🎉 Quiz complete! Your score: {st.session_state.score} / {len(questions)}")
    if st.button("Restart Quiz"):
        st.session_state.question_order = random.sample(range(len(questions)), len(questions))
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.rerun()
else:
    # Get current question based on shuffled order
    q_index = st.session_state.question_order[st.session_state.question_index]
    current_q = questions[q_index]

    # Display question
    st.subheader(f"Question {st.session_state.question_index + 1}:")
    st.write(current_q["question"])
    selected = st.radio("Choose your answer:", current_q["options"], key=st.session_state.question_index)

    if st.button("Submit Answer"):
        if selected == current_q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! Correct answer: {current_q['answer']}")

        time.sleep(2)
        st.session_state.question_index += 1
        st.rerun()







# this code randomly showes questions where one question can be showed multiple times


# import streamlit as st # for the web interface
# import random # for randomizing the questions
# import time # for the timer

# # Title of the Application
# st.title("📝 Quiz Application")

# # Define quiz questions, options, and answer in the form of a list of dictionaries
# # questions = [
# #     {
# #         "question": "What is the capital of Pakistan?",
# #         "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
# #         "answer": "Islamabad",
# #     },
# #     {
# #         "question": "Who is the founder of Pakistan?",
# #         "options": [
# #             "Allama Iqbal",
# #             "Liaquat Ali Khan",
# #             "Muhammad Ali Jinnah",
# #             "Benazir Bhutto",
# #         ],
# #         "answer": "Muhammad Ali Jinnah",
# #     },
# #     {
# #         "question": "Which is the national language of Pakistan?",
# #         "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
# #         "answer": "Urdu",
# #     },
# #     {
# #         "question": "What is the currency of Pakistan?",
# #         "options": ["Rupee", "Dollar", "Taka", "Riyal"],
# #         "answer": "Rupee",
# #     },
# #     {
# #         "question": "Which city is known as the City of Lights in Pakistan?",
# #         "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
# #         "answer": "Karachi",
# #     },
# # ]
# questions = [
#     {
#         "question": "What is the correct file extension for Python files?",
#         "options": [".pyth", ".pt", ".py", ".pyt"],
#         "answer": ".py",
#     },
#     {
#         "question": "Which keyword is used to define a function in Python?",
#         "options": ["function", "define", "def", "func"],
#         "answer": "def",
#     },
#     {
#         "question": "How do you insert comments in Python code?",
#         "options": ["// This is a comment", "# This is a comment", "/* comment */", "-- comment"],
#         "answer": "# This is a comment",
#     },
#     {
#         "question": "What is the output of: print(2 + 3 * 2)?",
#         "options": ["10", "12", "8", "7"],
#         "answer": "8",
#     },
#     {
#         "question": "What data type is the object below? \n x = 'Hello World'",
#         "options": ["int", "str", "bool", "float"],
#         "answer": "str",
#     },
#     {
#         "question": "Which one is a list in Python?",
#         "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "<1, 2, 3>"],
#         "answer": "[1, 2, 3]",
#     },
#     {
#         "question": "Which function is used to get input from a user?",
#         "options": ["input()", "get()", "read()", "scan()"],
#         "answer": "input()",
#     },
#     {
#         "question": "How do you start a 'while' loop in Python?",
#         "options": ["loop while", "while x > 0", "while (x > 0)", "while: x > 0"],
#         "answer": "while x > 0",
#     },
#     {
#         "question": "How do you start a 'for' loop in Python?",
#         "options": ["loop x in y", "foreach x in y", "for x to y", "for x in y"],
#         "answer": "for x in y",
#     },
#     {
#         "question": "Which symbol is used to check equality?",
#         "options": ["=", "==", "===", "!="],
#         "answer": "==",
#     },
#     {
#         "question": "How do you create a variable with the numeric value 5?",
#         "options": ["x = 5", "x := 5", "int x = 5", "num x = 5"],
#         "answer": "x = 5",
#     },
#     {
#         "question": "Which data type is used for decimal numbers?",
#         "options": ["int", "str", "bool", "float"],
#         "answer": "float",
#     },
#     {
#         "question": "Which operator is used for exponentiation (power)?",
#         "options": ["^", "**", "^^", "exp()"],
#         "answer": "**",
#     },
#     {
#         "question": "What does the len() function do?",
#         "options": ["Finds size of file", "Calculates sum", "Returns length of an object", "Logs errors"],
#         "answer": "Returns length of an object",
#     },
#     {
#         "question": "Which function converts a string to an integer?",
#         "options": ["int()", "float()", "str()", "bool()"],
#         "answer": "int()",
#     },
#     {
#         "question": "Which of the following is a tuple?",
#         "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "<1, 2, 3>"],
#         "answer": "(1, 2, 3)",
#     },
#     {
#         "question": "What keyword is used to handle exceptions?",
#         "options": ["try", "check", "error", "except"],
#         "answer": "except",
#     },
#     {
#         "question": "What is the output of: print(type(10))?",
#         "options": ["int", "<class 'int'>", "type int", "number"],
#         "answer": "<class 'int'>",
#     },
#     {
#         "question": "Which of the following is NOT a valid Python data type?",
#         "options": ["list", "float", "array", "bool"],
#         "answer": "array",
#     },
#     {
#         "question": "Which statement will check if `a` is not equal to `b`?",
#         "options": ["a != b", "a =! b", "a <> b", "a not = b"],
#         "answer": "a != b",
#     },
# ]


# # Initialize a random question if none exists in the session state
# if "current_question" not in st.session_state:
#     st.session_state.current_question = random.choice(questions)

# # Get the current question from session state
# question = st.session_state.current_question

# # Display the question
# st.subheader(question["question"])

# # Create radio buttons for the options
# selected_option = st.radio("Choose your answer", question["options"], key="answer")

# # Submit button the check the answer
# if st.button("Submit Answer"):
#     # check if the answer is correct
#     if selected_option == question["answer"]:
#         st.success("✅ Correct!")
#     else:
#         st.error("❌ Incorrect! the correct answer is " + question["answer"])
  
#     # Wait for 3 seconds before showing the next question
#     time.sleep(5)

#     # Select a new random question
#     st.session_state.current_question = random.choice(questions)

#     # Rerun the app to display the next question    
#     st.rerun()