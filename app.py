import streamlit as st
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Get URI from environment
uri = os.getenv("MONGODB_URI")

# Safe check
if not uri:
    st.error("MongoDB URI not found. Please set MONGODB_URI as an environment variable.")
    st.stop()

# Connect to MongoDB
client = MongoClient(uri)
db = client["testdb"]
collection = db["users"]

# Streamlit UI
st.title("MongoDB + Streamlit App")

# Show users from DB
st.subheader("All Users in DB:")
users = collection.find()
for user in users:
    st.write(user)

# Add new user
st.subheader("Add a New User")
name = st.text_input("Name")
email = st.text_input("Email")
if st.button("Add User"):
    collection.insert_one({"name": name, "email": email})
    st.success("User added successfully!")
