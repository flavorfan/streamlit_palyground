import streamlit as st

# def login():
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     if st.button("Login"):
#         if username == "admin" and password == "password":
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("Login successful")
#         else:
#             st.error("Login failed")


def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["password"].strip() == "123465":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["password"]:
            st.warning("Please enter your password")
        elif not st.session_state["user"]:
            st.warning("Please enter your username")
        else:
            st.error("Invalid username or password")


def authenticate():
    if "authenticated" not in st.session_state:
        st.text_input("Username", value="",key="user", on_change=creds_entered)
        st.text_input("Password", value="", key="password", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input("Username", value="",key="user", on_change=creds_entered)
            st.text_input("Password", value="", key="password", type="password", on_change=creds_entered)
            return False

if authenticate():
    st.write("Authenticated")
else:
    st.write("Not authenticated")

# st.title("hello world")

