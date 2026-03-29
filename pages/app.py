import streamlit as st

st.set_page_config(
    page_title="AI Mentor Dashboard",
    page_icon="🧠",
    layout="wide"
)

# Session state
if "progress" not in st.session_state:
    st.session_state.progress = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
st.sidebar.title("🧠 AI Mentor Dashboard")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📊 Progress Tracker", "⚠️ Sprint Risk Predictor", "🤖 AI Mentor Chat"]
)

st.sidebar.markdown("---")
st.sidebar.info("Built with Python + Streamlit\nBYOP Project")

# Routing with error handling
try:
    if page == "🏠 Home":
        from pages.home import show
        show()
    elif page == "📊 Progress Tracker":
        from pages.tracker import show
        show()
    elif page == "⚠️ Sprint Risk Predictor":
        from pages.sprint_risk import show
        show()
    elif page == "🤖 AI Mentor Chat":
        from pages.chatbot import show
        show()
except Exception as e:
    st.error(f"Error loading page: {e}")

# Footer
st.markdown("---")
st.markdown("© 2026 AI Mentor Dashboard | VIT Bhopal")
