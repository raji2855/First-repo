import streamlit as st

# Page title
st.title("Student Grade System")

st.write("Enter the student's mark (0–100) to find the grade.")

# Get mark from user
mark = st.number_input(
    "Enter student mark:",
    min_value=0,
    max_value=100,
    value=50,
    step=1
)

# Calculate grade
if mark >= 90:
    grade = "A+"
elif mark >= 80:
    grade = "A"
elif mark >= 70:
    grade = "B"
elif mark >= 60:
    grade = "C"
elif mark >= 50:
    grade = "D"
else:
    grade = "F"

# Display result
if st.button("Calculate Grade"):
    st.success(f"Entered Mark: {mark}")
    st.info(f"Resulting Grade: {grade}")