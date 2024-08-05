import re

def assess_password_strength(password):
    # Criteria for the password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Count number of fulfilled criteria
    fulfilled_criteria = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])
    
    # Provide feedback based on the number of fulfilled criteria
    if fulfilled_criteria == 5:
        return "Very Strong", "Your password is very strong!"
    elif fulfilled_criteria == 4:
        return "Strong", "Your password is strong."
    elif fulfilled_criteria == 3:
        return "Moderate", "Your password is moderate. Consider adding more characters, including uppercase letters, digits, and special characters."
    else:
        return "Weak", "Your password is weak. Ensure it has at least 8 characters, including uppercase and lowercase letters, digits, and special characters."

def main():
    while True:
        password = input("Enter a password to assess (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Goodbye!")
            break
        
        strength, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength}")
        print(f"Feedback: {feedback}\n")

if __name__ == "__main__":
    main()
