
import streamlit as st
from datetime import date

st.set_page_config(page_title="Ezue Smart Legal Assistant", layout="centered")

st.title("⚖️ Ezue Smart Legal Assistant Suite")
st.markdown("AI-powered legal assistant for generating documents, letters, and filings — built by a lawyer for lawyers.")

# Sidebar for document selection
documents = [
    "Pre-Action Notice",
    "Statement of Claim",
    "Statement of Defence",
    "Reply to Statement of Defence",
    "Written Address",
    "Preliminary Objection",
    "Interrogatories",
    "Motion on Notice",
    "Motion Ex Parte",
    "Originating Motion",
    "Originating Summons",
    "Writ of Summons",
    "Reply on Point of Law",
    "Bail Application",
    "Notice of Appeal",
    "Appellant Brief",
    "Respondent Brief",
    "Fundamental Rights Enforcement",
    "Garnishee Proceedings",
    "Deed of Settlement"
]

selected = st.sidebar.selectbox("📄 Choose Document to Generate", documents)

# ----------- Document: Pre-Action Notice ------------
if selected == "Pre-Action Notice":
    st.subheader("📌 Pre-Action Notice Generator")
    st.markdown("This smart form will generate a complete pre-action notice based on your inputs.")

    with st.form("pre_action_notice"):
        st.subheader("⚖️ Case Details")
        court_name = st.text_input("Name of Court")
        suit_number = st.text_input("Proposed Suit Number (Optional)")
        claimant = st.text_input("Claimant's Full Name")
        defendant = st.text_input("Defendant's Full Name")
        defendant_address = st.text_area("Defendant's Address")
        subject_matter = st.text_area("Subject Matter of the Intended Action")
        reliefs = st.text_area("Summary of Reliefs You Intend to Seek in Court")
        days_notice = st.number_input("Length of Notice (in days)", min_value=7, max_value=90, value=30)
        date_today = st.date_input("Date of Letter", value=date.today())
        submit = st.form_submit_button("Generate Document")

    if submit:
        document = f"""
{date_today.strftime('%d %B %Y')}

To:  
{defendant}  
{defendant_address}

**Dear {defendant},**

**RE: NOTICE OF INTENTION TO COMMENCE LEGAL PROCEEDINGS**

Take notice that I, **{claimant}**, intend to institute an action against you in the **{court_name}** in respect of the following subject matter:

> {subject_matter}

The reliefs I intend to claim in the suit include but are not limited to:

> {reliefs}

You are hereby given **{days_notice} days** from the date of this notice to resolve the above-mentioned issue(s) to my satisfaction. Failure to do so will leave me with no option but to commence legal action against you without further notice.

This notice is issued in good faith and in compliance with the rules of court regarding pre-action protocols.

Yours faithfully,  
**{claimant}**
        """

        st.success("✅ Pre-Action Notice Generated")
        st.download_button("📥 Download Notice as Text", document, file_name="pre_action_notice.txt")
        st.text_area("📄 Preview", document, height=400)

# ------------- Placeholders for Other Documents ---------------
else:
    st.subheader(f"📄 {selected}")
    st.write("🚧 This document is coming soon. Stay tuned!")
