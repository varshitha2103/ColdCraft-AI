import streamlit as st
from email_variants import generate_email_variant
from tracker import log_result, load_results
import pandas as pd

st.set_page_config(page_title="Cold Email A/B Tester", layout="centered")
st.title("📧 Cold Email A/B Testing Assistant")

offer = st.text_input("Your Offer")
lead_type = st.text_input("Lead Type (e.g. 'startup founder')")

if st.button("Generate Email Variants"):
    if offer and lead_type:
        email_a = generate_email_variant(offer, lead_type, "A")
        email_b = generate_email_variant(offer, lead_type, "B")
        
        st.subheader("✉️ Variant A")
        st.code(email_a)
        
        st.subheader("✉️ Variant B")
        st.code(email_b)
    else:
        st.warning("Please enter both offer and lead type.")

st.markdown("---")
st.header("📊 Log Outcomes")

version = st.selectbox("Version", ["A", "B"])
outcome = st.selectbox("Outcome", ["Opened", "Replied", "Ignored"])

if st.button("Log Result"):
    log_result(version, outcome)
    st.success("Logged successfully.")

df = load_results()
if not df.empty:
    st.markdown("### 📈 Performance Summary")
    summary = df.groupby(["version", "outcome"]).size().reset_index(name='count')
    st.dataframe(summary)
