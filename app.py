 
process = st.selectbox("Choose a document to generate:", [
    "Pre-Action Notice",
    "Writ of Summons"
])

if process == "Pre-Action Notice":
    st.header("📌 Pre-Action Notice Generator")

    court_name = st.text_input("Court Name")
    suit_number = st.text_input("Proposed Suit Number (Optional)")
    claimant = st.text_input("Claimant's Full Name")
    defendant = st.text_input("Defendant's Full Name")
    defendant_address = st.text_area("Defendant's Address")
    subject_matter = st.text_area("Subject Matter of the Intended Action")
    reliefs = st.text_area("Summary of Reliefs You Intend to Seek in Court")
    days_notice = st.number_input("Length of Notice (in days)", min_value=7, max_value=90, value=30)
    date_today = st.date_input("Date of Letter", value=date.today())
    submit = st.button("Generate Document")

    if submit:
        document = f"""
{date_today.strftime('%d %B %Y')}

To:  
{defendant}  
{defendant_address}

RE: NOTICE OF INTENTION TO COMMENCE LEGAL PROCEEDINGS

Take notice that I, {claimant}, intend to institute an action against you in the {court_name} in respect of the following subject matter:

{subject_matter}

The reliefs I intend to claim in the suit include but are not limited to:

{reliefs}

You are hereby given {days_notice} days from the date of this notice to resolve the above-mentioned issue(s) to my satisfaction. Failure to do so will leave me with no option but to commence legal action against you without further notice.

This notice is issued in good faith and in compliance with the rules of court regarding pre-action protocols.

Yours faithfully,  
{claimant}
        """
        st.success("✅ Pre-Action Notice Generated")
        st.text_area("📄 Preview", document, height=400)

elif process == "Writ of Summons":
    st.header("🧾 Writ of Summons Suite")

    court = st.text_input("Court Name")
    division = st.text_input("Judicial Division / Registry")
    suit_number = st.text_input("Suit Number")
    claimant = st.text_input("Claimant's Full Name")
    claimant_address = st.text_input("Claimant's Address")
    defendant = st.text_input("Defendant's Full Name")
    subject = st.text_area("Brief Subject Matter")
    reliefs = st.text_area("Reliefs Being Sought")
    witnesses = st.text_area("List of Witnesses (comma separated)")
    documents = st.text_area("List of Documents (comma separated)")
    today = date.today().strftime("%B %d, %Y")

    if st.button("Generate All Documents"):
        heading = f"IN THE {court.upper()}\\nIN THE {division.upper()} DIVISION\\nSUIT NO: {suit_number}\\n\\nBETWEEN\\n{claimant.upper()} - CLAIMANT\\nAND\\n{defendant.upper()} - DEFENDANT"

        writ = f"""{heading}

WRIT OF SUMMONS

To: {defendant}

You are hereby commanded that within 30 days after the service of this writ on you, inclusive of the day of such service, you do cause an appearance to be entered for you in an action at the suit of {claimant}, and take notice that in default of your doing so, the Claimant may proceed therein, and judgment may be given in your absence.

Dated this {today}
"""

        claim = f"""{heading}

STATEMENT OF CLAIM

1. The Claimant is {claimant}, of {claimant_address}.
2. The Defendant is {defendant}.
3. The cause of action is as follows:
   {subject}

4. The Claimant claims the following reliefs:
   {reliefs}

WHEREOF the Claimant claims as per the reliefs stated above.

Dated this {today}
"""

        witness_list = f"""{heading}

LIST OF WITNESSES

1. {witnesses.replace(',', '\\n2. ')}
"""

        doc_list = f"""{heading}

LIST OF DOCUMENTS TO BE RELIED UPON

1. {documents.replace(',', '\\n2. ')}
"""

        oath = f"""{heading}

CLAIMANT’S WRITTEN STATEMENT ON OATH

I, {claimant.upper()}, of {claimant_address}, do hereby make oath and state as follows:

1. That I am the Claimant in this suit.
2. That I have read the Statement of Claim and the facts stated therein are true and correct to the best of my knowledge, information, and belief.
3. That I depose to this affidavit in good faith conscientiously believing the contents to be true and correct and in accordance with the Oaths Act.

DEPONENT: ________________________
DATE: {today}

BEFORE ME:
COMMISSIONER FOR OATHS: ________________________
"""

        st.success("✅ All Court Documents Generated")
        st.subheader("📜 Writ of Summons")
        st.text_area("Writ Preview", writ, height=250)

        st.subheader("📄 Statement of Claim")
        st.text_area("Claim Preview", claim, height=300)

        st.subheader("🧾 List of Witnesses")
        st.text_area("Witness List", witness_list, height=200)

        st.subheader("📂 List of Documents")
        st.text_area("Document List", doc_list, height=200)

        st.subheader("📝 Claimant’s Statement on Oath")
        st.text_area("Statement on Oath", oath, height=350)
