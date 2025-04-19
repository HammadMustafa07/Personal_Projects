import streamlit as st

def main():
    # Page title
    st.title("🧠 Smart Calculator – Fast & Easy")

    st.markdown("### 💡 *Enter any two numbers below, choose your favorite operation, and let the magic happen!*")

    # Two columns for inputs
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("🔢 First Number", value=0.0)
    with col2:
        num2 = st.number_input("🔢 Second Number", value=0.0)

    # Operation selection with emojis
    operation = st.selectbox(
        "✨ What do you want to do?",
        ["➕ Add 'em", "➖ Subtract 'em", "✖️ Multiply 'em", "➗ Divide 'em"],
    )

    # Button to calculate
    if st.button("🚀 Let's Calculate!"):
        try:
            if operation == "➕ Add 'em":
                result = num1 + num2
                symbol = "+"
                message = "🎉 Boom! Here's your answer:"
            elif operation == "➖ Subtract 'em":
                result = num1 - num2
                symbol = "-"
                message = "🧮 Calculated difference:"
            elif operation == "✖️ Multiply 'em":
                result = num1 * num2
                symbol = "×"
                message = "✨ Total product:"
            else:
                if num2 == 0:
                    st.error("🚫 Whoops! You can't divide by zero.")
                    return
                result = num1 / num2
                symbol = "÷"
                message = "📘 Division done right!"

            st.success(f"{message} \n\n**{num1} {symbol} {num2} = {result}**")

        except Exception as e:
            st.error(f"⚠️ Something went wrong: {str(e)}")

if __name__ == "__main__":
    main()
