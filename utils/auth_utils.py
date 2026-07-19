import streamlit as st


def login_user(user):
    """
    Store logged-in user in Streamlit session.
    """
    st.session_state["authenticated"] = True
    st.session_state["user"] = user


def logout_user():
    """
    Clear the current user session.
    """
    st.session_state.clear()


def is_authenticated():
    """
    Check whether the current user is authenticated.
    """
    return st.session_state.get("authenticated", False)


def require_login():
    """
    Protect pages that require authentication.
    """
    if not is_authenticated():
        st.error("🔒 Please login to continue.")
        st.switch_page("pages/3_🔐_Login.py")
        st.stop()