import streamlit as st 

st.title("Unit Converter App")
st.markdown("## Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get converted results in real-time.")

# Corrected category selection
category = st.selectbox("Choose category", ["Length", "Weight", "Time"])

# Function for unit conversion
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24  # Fixed from /60
        elif unit == "Days to hours":
            return value * 24  # Fixed from *60

    return None  # If no conversion applies

# Selecting unit based on category
if category == "Length":
    unit = st.selectbox("Select conversion", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversion", [
        "Seconds to minutes", "Minutes to seconds",
        "Minutes to hours", "Hours to minutes",
        "Hours to days", "Days to hours"
    ])

# Taking user input
value = st.number_input("Enter the value to convert", min_value=0.0)

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion selected.")
