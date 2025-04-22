import time
import random
import streamlit as st
from db import register_user, authenticate_user, add_points_to_user, get_user_points
from dotenv import load_dotenv

# Load environment (needed if you want to use dotenv here too)
load_dotenv()

# Set up Streamlit page
st.set_page_config(page_title="EarniFy", layout="centered")

st.set_page_config(
    page_title="EarniFy",
    page_icon="💲"
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# Function to show registration form
def show_registration_form():
    st.title("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Register"):
        message = register_user(username, email, password)
        st.success(message)

# Function to show login form
def show_login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

# Function to show dashboard after login
def show_dashboard():
    st.title(f"Welcome, {st.session_state.username} 👋")
    points = get_user_points(st.session_state.username)
    st.info(f"Your current points: {points}")
    
     # Check if user has enough points for withdrawal
    if points >= 1000:
        if st.button("Withdraw Points"):
            # Redirect to another website
            st.markdown("[Proceed to Withdrawal](https://shahriarkabir.onrender.com)", unsafe_allow_html=True)
    else:
        st.warning("You need at least 1000 points to withdraw.")

    if st.button("Earn 10 Points"):
        st.markdown("[Click here to proceed to the next page](https://shahriarkabir.onrender.com)", unsafe_allow_html=True)
        st.warning("Please complete the task correctly to earn points. If you do anything wrong, you will be banned!")
        with st.spinner('Processing your task....'):
            time.sleep(30 + random.randint(0, 15))  # Simulate delay of 30 to 45 seconds
            
            # Simulate success or failure based on conditions you want to set
            success = True  # Set this based on actual task result

            if success:
                add_points_to_user(st.session_state.username, 10)
                st.success("You earned 10 points! Task completed successfully.")
            else:
                st.error("You have failed the task. You have been banned!")

            # After task completion, redirect the user to an external link
          
        st.rerun()

    if st.button("Earn 20 Points"):
        st.markdown("[Click here to proceed to the next page](https://shahriarkabir.onrender.com)", unsafe_allow_html=True)
        st.warning("Please complete the task correctly to earn points. If you do anything wrong, you will be banned!")
        with st.spinner('Processing your task....'):
            time.sleep(30 + random.randint(0, 15))  # Simulate delay of 30 to 45 seconds

            # Simulate success or failure based on conditions you want to set
            success = True  # Set this based on actual task result

            if success:
                add_points_to_user(st.session_state.username, 20)
                st.success("You earned 20 points! Task completed successfully.")
            else:
                st.error("You have failed the task. You have been banned!")
        
        st.rerun()

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.success("You’ve been logged out.")
        st.rerun()

st.markdown("""
    <p style="color: gray; font-family: Arial, sans-serif;">
       Made with ❤️ by 
       <a href="https://shahriarkabir.onrender.com" style="color: gray;">Shahriar Kabir</a> 
    </p>
""", unsafe_allow_html=True)
st.markdown("""
    <p style="color: gray; font-family: Arial, sans-serif;">
       If you are now logged in. No need to refresh the page.
    </p>
""", unsafe_allow_html=True)

# Main controller
def main():
    st.sidebar.title("EarniFy")
    if st.session_state.logged_in:
        show_dashboard()
    else:
        page = st.sidebar.radio("Choose Action", ["Login", "Register"])
        if page == "Register":
            show_registration_form()
        else:
            show_login_form()

if __name__ == "__main__":
    main()
