import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Upper and lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1

    # Number check
    if re.search(r'\d', password):
        strength += 1

    # Special character check
    if re.search(r'[@$!%*?&#]', password):
        strength += 1

    # Determine strength level
    if strength <= 1:
        return "Weak"
    elif strength == 2:
        return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    password = input("Enter a password: ")
    print("Password Strength:", check_password_strength(password))
