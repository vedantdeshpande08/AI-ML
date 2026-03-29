import streamlit as st

def show():
    st.title("⚠️ Sprint Risk Predictor")

    attendance = st.slider("Attendance (%)", 0, 100)
    study_hours = st.slider("Study Hours per Day", 0, 10)
    avg_score = st.slider("Average Score", 0, 100)

    if st.button("Predict Risk"):
        risk = "Low"

        if attendance < 60 or study_hours < 2 or avg_score < 50:
            risk = "High"
        elif attendance < 75 or avg_score < 65:
            risk = "Medium"

        st.subheader(f"Risk Level: {risk}")

        if risk == "High":
            st.error("⚠️ You are at high risk! Increase study time and attendance.")
        elif risk == "Medium":
            st.warning("⚠️ Moderate risk. Stay consistent.")
        else:
            st.success("✅ You are doing well!")
