import streamlit as st
from pymongo import MongoClient

# Access MongoDB URI from Streamlit secrets
uri = st.secrets["MONGODB"]["URI"]

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
    if name and email:
        collection.insert_one({"name": name, "email": email})
        st.success("User added successfully!")
    else:
        st.warning("Please fill in both the name and email fields.")
