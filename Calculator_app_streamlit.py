import streamlit as st

# Function to perform calculations
def calculate(num1, num2, operator):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error! Division by zero is not allowed."
            else:
                return num1 / num2
        else:
            return "Invalid operator. Please choose one of +, -, *, /."
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.subheader("Welcome to Prem Mohan's Calculator")
st.title("📱 Friendly Calculator")

# Input fields for numbers and operator
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")
operator = st.selectbox("Choose the operator:", ["+", "-", "*", "/"])

# Perform calculation when button is clicked
if st.button("Calculate"):
    result = calculate(num1, num2, operator)
    st.write(f"**Result:** {result}")

# Friendly message at the end
st.info("Thank you for using this calculator! Feel free to try more calculations.")
