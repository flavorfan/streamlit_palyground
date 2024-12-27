import streamlit as st

import datetime


users_collection = [
    {
        "username": "admin",
        "password": "123456"
    },
    {
        "username": "guest",
        "password": "12345",
    },
    {
        "username": "user",
        "password": "123",
    }
]

def login_user(username, password):
    user = next((user for user in users_collection if user["username"] == username), None)
    if user and user["password"] == password:
        st.session_state["authenticated"] = True
        st.session_state["user"] = user['username']
        st.rerun()
    else:
        st.error("Invalid username or password. Please try again.")


def logout():
    del st.session_state["user"]
    st.rerun()





def login_required(protected_page):
    def wrapper():
        if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
            username = st.text_input("Username", value="")
            password = st.text_input("Password", value="", type="password")
            if st.button("Login"):
                login_user(username, password)
        else:
            protected_page()
    return wrapper
