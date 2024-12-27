import streamlit as st
# import pandas as pd
# import numpy as np





# def logout():
#     del st.session_state["user"]
#     st.rerun()


# def user_profile(user_id):
#     _user_id = ObjectId(user_id)

#     if "user" not in st.session_state:
#         st.session_state.user = user
#     else:
#         user = get_user(_user_id)

#     # st.write(f"User ID: {user['_id']}")
#     st.write(f"Hi, {user['username']}")
#     st.image(user['picture'], width=100)
#     st.write(f"Email: {user['email']}")

#     if st.button("Logout"):
#         logout()


# def login_tab():
#     st.header("Login")
#     login_username = st.text_input("Username", key="login_username")
#     login_password = st.text_input("Password", type="password", key="login_password")
#     if st.button("Login"):
#         login_user(login_username, login_password)





st.title("User Profile")
# login_tab()
st.json(st.session_state)