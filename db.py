import os, streamlit as st
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Get Mongo URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["mlm_app"]  # Use your desired database name

# Collection for users
users_collection = db.users

# Register a new user
def register_user(username, email, password):
    if users_collection.find_one({"username": username}):
        return st.warning("Username already exists!")
    users_collection.insert_one({
        "username": username,
        "email": email,
        "password": password,
        "points": 0
    })
    return "User registered successfully!"

# Authenticate user
def authenticate_user(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    return bool(user)

# Add points to a user
def add_points_to_user(username, points):
    users_collection.update_one(
        {"username": username},
        {"$inc": {"points": points}}
    )

# Get user’s current points
def get_user_points(username):
    user = users_collection.find_one({"username": username})
    return user.get("points", 0) if user else 0
