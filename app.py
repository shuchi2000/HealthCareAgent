import streamlit as st

# Sidebar: Chatbot info and filters
st.sidebar.title("🏥 Health Metrics Chatbot")
st.sidebar.markdown("**For Non-Clinical Staff**")
hospital = st.sidebar.selectbox(
    "Select Hospital",
    [
        "All Hospitals",
        "All India Institute of Medical Sciences, Delhi",
        "Postgraduate Institute of Medical Education and Research",
        "Christian Medical College, Vellore",
        "Tata Memorial Hospital",
        "King George's Medical University",
        "Sir Ganga Ram Hospital",
        "Apollo Hospitals",
        "Fortis Memorial Research Institute",
        "Medanta - The Medicity",
        "Christian Medical College, Ludhiana"
    ]
)
department = st.sidebar.selectbox(
    "Select Department",
    [
        "All Departments",
        "Emergency Department",
        "Inpatient Ward",
        "Outpatient Department",
        "Surgery Department",
        "Radiology Department",
        "Laboratory Department",
        "Pharmacy Department",
        "ICU Department",
        "Administration",
        "Quality & Safety",
        "Finance & Billing",
        "Patient Experience"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Filters will be used for dataset queries.")

# Main: Chat UI
st.title("💬 MedMetricsBot")
st.markdown(f"**Hospital:** {hospital}  |  **Department:** {department}")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_bot_response(user_input):
    # Placeholder for actual agent connection
    return f"Echo: {user_input} (filtered by {hospital}, {department})"

with st.container():
    for chat in st.session_state.chat_history:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**Bot:** {chat['bot']}")

    user_input = st.text_input("Type your question about non-clinical metrics...", key="input")
    if st.button("Send") and user_input:
        bot_response = get_bot_response(user_input)
        st.session_state.chat_history.append({"user": user_input, "bot": bot_response})
        st.experimental_rerun()