# HW8.py
# Author: Bodhi Fox

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)
import streamlit as st
import datetime as dt

# Streamlit title, subtitle, date, and button

st.title("Date Counter Web Application")
st.subheader("This web app will count the number of days until a certain date")
date= st.date_input("Enter a date: ")
button= st.button("Calculate")

# The calculate_days function from Lab9.py

def calculate_days(date)->int:
    current_date= dt.datetime.now().date()
    days_difference= date- current_date
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past")
    return days_difference.days






# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.

def calculate_days_until_birthday(birthday: dt.date) -> int:
    current_date = dt.datetime.now().date()
    next_birthday = dt.date(current_date.year, birthday.month, birthday.day)

    if next_birthday < current_date:
        next_birthday = dt.date(current_date.year + 1, birthday.month, birthday.day)

    days_until_birthday = (next_birthday - current_date).days
    st.write(f"Your birthday is on {birthday}")
    st.write(f"Days until your birthday: {days_until_birthday}")
    return days_until_birthday




# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)

def days_until_semester_ends(current_date: dt.date) -> int:
    end_of_semester = dt.date(2023, 12, 8)
    days_until_semester = (end_of_semester - current_date).days
    st.write(f"Days until the end of the semester: {days_until_semester}")
    return days_until_semester



# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include 
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")

def days_until_new_years(current_date: dt.date) -> int:
    new_years = dt.date(current_date.year + 1, 1, 1)
    days_until_new_years = (new_years - current_date).days
    st.write(f"Days until New Year's Day: {days_until_new_years} 🎉")
    return days_until_new_years


# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.


# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉
if st.button("Days until New Year's Day"):
    current_date = dt.datetime.now().date()
    days_until_new_years(current_date)

# app function from Lab9.py
def app():
    if button and date is not None:  
        try:
            result = calculate_days(date)
        except ValueError:
            st.write("Please enter a valid date.")
            return

        st.write(f"Current date: {dt.datetime.now().date()}")
        st.write(f"Selected Date: {date}")
        st.write(f"Days until selected date: {result}")


    current_date = dt.datetime.now().date()
    calculate_days_until_birthday(current_date)
    days_until_semester_ends(current_date)


if __name__ == '__main__':
    app()