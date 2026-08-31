import streamlit as st

# Page title
st.title("BMI Calculator")

st.write("Enter your height and weight to calculate your BMI.")

# User inputs
weight = st.number_input(
    "Enter your weight (kg)",
    min_value=1.0,
    value=60.0,
    step=0.1
)

height_cm = st.number_input(
    "Enter your height (cm)",
    min_value=1.0,
    value=170.0,
    step=0.1
)

# Calculate button
if st.button("Calculate BMI"):

    # Convert cm to meters
    height_m = height_cm / 100

    # BMI Formula
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI is: {bmi:.2f}")

    # BMI Category
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")