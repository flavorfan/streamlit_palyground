import pandas as pd
import streamlit as st

from authentication import login_required





# --- PAGE SETUP ---
profile_page = st.Page(
    "views/10_profile.py",
    title="profile",
    icon=":material/account_circle:",
    default=True,
)
about_page = st.Page(
    "views/20_about.py",
    title="About",
    icon=":material/bar_chart:",
)
project_1_page = st.Page(
    "views/30_project_1.py",
    title="Project_1",
    icon=":material/smart_toy:",
)
project_2_page = st.Page(
    "views/40_project_2.py",
    title="Project_2",
    icon=":material/smart_toy:",
)

pages_dict_admin = {
    "Info": [profile_page,about_page],
    "Projects": [project_1_page,project_2_page]
}

page_dict_user = {
    "Info": [profile_page,about_page]
}


# # --- NAVIGATION SETUP [WITH SECTIONS]---
# pg = st.navigation(
#     {
#         "Info": [login_page],
#         "Projects": [about_page, project_1_page],
#     }
# )
# # --- RUN NAVIGATION ---
# pg.run()

@login_required
def navigation_pages():
    if st.session_state["authenticated"] and st.session_state["user"] == "admin":
        print("----------------admin")
        pages_dict = pages_dict_admin
    else:
        print("***************user")
        pages_dict = page_dict_user
    pg = st.navigation(pages_dict)
    pg.run()     

navigation_pages()
