import streamlit as st
import pandas as pd

def show():
    st.title("📊 Progress Tracker")

    subject = st.text_input("Subject")
    score = st.number_input("Score (out of 100)", 0, 100)

    if st.button("Add Record"):
        st.session_state.progress.append({"Subject": subject, "Score": score})
        st.success("Record added!")

    if st.session_state.progress:
        df = pd.DataFrame(st.session_state.progress)
        st.write("### Your Progress")
        st.dataframe(df)

        st.write("### Average Score")
        st.info(df["Score"].mean())
