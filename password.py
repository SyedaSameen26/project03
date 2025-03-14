import streamlit as st
def check_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z)")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")
    
    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9)")
    
    # Check for special characters
    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*)")
    
    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"
    
    return score, strength, feedback, color

def main():
    # Streamlit app configuration
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
    
    # Title and description
    st.title("🔒 Password Strength Meter")
    st.write("### Enter a password to check its strength based on security criteria.")
    
    # Input field for password
    password = st.text_input("Enter your password:", type="password")
    
    # Analyze button
    if st.button("Check Strength"):
        if password:
            # Get password analysis
            score, strength, feedback, color = check_password_strength(password)
            
            # Display results
            st.markdown(f"### Password Strength: <span style='color:{color}'>{strength}</span>", 
                       unsafe_allow_html=True)
            st.write(f"Score: {score}/5")
            
            # Display feedback
            if strength == "Strong":
                st.success("Great job! Your password meets all security criteria!")
            else:
                st.warning("Suggestions to improve your password:")
                for suggestion in feedback:
                    st.write(f"- {suggestion}")
            
            # Display criteria
            with st.expander("Password Requirements"):
                st.write("""
                A strong password should:
                - Be at least 8 characters long
                - Contain uppercase letters (A-Z)
                - Contain lowercase letters (a-z)
                - Include at least one digit (0-9)
                - Have at least one special character (!@#$%^&*)
                """)
        else:
            st.error("Please enter a password to analyze!")
    
    # Add some styling
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()