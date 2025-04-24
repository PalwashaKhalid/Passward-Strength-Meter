#  Imports
import streamlit as st
import re

st.set_page_config(page_title = "Password Strength Meter, page_icon 🔒")
                   
st.title("🔐Password Strength Checker")
st.markdown("""
### Welcome to the ultimate password strength checker!🔥
use this simple tool to check the strength of your passward and get suggestion on how to make it stronger.
            we will give you tips to create a **Strong Password** 🔏""")

password = st.text_input("Enter your passward", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")

    if re.search(r'\d' , password):
        score += 1
    else:
        feedback.append("❌ Passord should contain at least 1 digit.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least 1 special character.")
    
    if score == 4:
        feedback.append("✅ Your Password is strong!🎉")

    elif score == 3:
        feedback.append("⚠️Your Password is medium strength. It could be Stronger.")

    elif score == 2:
        feedback.append("🟠 Your Password is moderate. It could be stronger.")

    else:
        feedback.append("🚫 Your Password is weak. Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions!")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your Passward to get started.")