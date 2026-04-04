import streamlit as st
from email_generator import generate_email

st.title("AI Email Writer")

topic = st.text_input("Email Topic")
recipient = st.text_input("Recipient")
points = st.text_area("Key Points")

tone = st.selectbox(
    "Select Email Tone",
    ["Friendly", "Formal", "Professional", "Apology", "Follow-up", "Sales"]
)

length = st.selectbox(
    "Select Email Length",
    ["Short", "Medium", "Detailed"]
)

template = st.selectbox(
    "Select Email Template",
    [
        "Leave request",
        "Job application",
        "Meeting request",
        "Follow-up email",
        "Complaint email"
    ]
)

if st.button("Generate Email"):
    email = generate_email(
        topic,
        tone,
        recipient,
        points,
        length,
        template
    )
    st.subheader("Generated Email")
    st.text_area("Email Output", email, height=300)
    st.download_button(
        label="Download Email as TXT",
        data=email,
        file_name="generated_email.txt",
        mime="text/plain"
    )
    st.success("Email generated successfully! You can copy or download it.")