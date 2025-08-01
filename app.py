
import streamlit as st

st.title("Ezue Legal Assistant")

menu = st.sidebar.selectbox("Select a Court Document", [
    "Pre-Action Notice",
    "Originating Summons",
    "Originating Motion",
    "Writ of Summons",
    "Statement of Claim",
    "Statement of Defence",
    "Reply to Statement of Defence",
    "Reply on Point of Law",
    "Preliminary Objection",
    "Written Address",
    "Interrogatories",
    "Affidavit",
    "Motion Ex Parte",
    "Motion on Notice",
    "Bail Application",
    "Respondent’s Brief",
    "Fundamental Rights Enforcement",
    "Deed of Settlement / Out-of-Court Terms",
    "Letters (Demand, ADR, Follow-Up)",
    "Garnishee Proceedings"
])

def coming_soon():
    st.info("This document template is coming soon. Stay tuned.")

def affidavit():
    st.header("Affidavit Generator")
    name = st.text_input("Deponent's Full Name")
    age = st.number_input("Age", min_value=0)
    occupation = st.text_input("Occupation")
    address = st.text_area("Address")
    facts = st.text_area("Facts of the Affidavit")
    if st.button("Generate Affidavit"):
        st.subheader("Preview")
        st.write(f"I, {name}, aged {age}, a {occupation} of {address}, hereby depose and say as follows:")
        st.write(facts)
        st.success("Affidavit generated successfully.")

if menu == "Affidavit":
    affidavit()
elif menu == "Fundamental Rights Enforcement":
    st.header("Fundamental Rights Enforcement")
    coming_soon()
else:
    coming_soon()
