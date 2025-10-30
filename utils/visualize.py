import streamlit as st

def show_dashboard(summaries):
    st.title("Research Copilot Dashboard")
    for i, summary in enumerate(summaries):
        st.markdown(f"### Paper {i+1}")
        st.write(summary)
