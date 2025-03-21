#  Imports
import re

def check_passwaord_strength(passward):
    score = 0

    # Length Check 
    if len(passward) >= 8:
        score +=1
    
    else:
        print("❌ Passward should be 8 characters long.")

    # Upper & Lower case check
    if re.search(r"[A-Z]", passward) and re.search(r"[a-z]", passward):
        score += 1

    else:
        print(" ❌ Include both uppercase and lowercase letter.")

    # Digit check
    if re.search(r"\d", passward):
        score += 1

    else:
        print("❌ Include at least one digit.")

    # Special character check
    if re.search(r"[!@#$%^&*_+]", passward):
        score += 1

    else:
        print("❌ Include at least one special character.")
    
    # Strength rating
    if score == 4:
        print("✅ Strong Passward!")

    elif score == 3:
        print("⚠️ Moderate Passward - Consider adding more security.")

    else:
        print("❌ Weak Passward - Improve it using above suggestions.")

# User Input
passward = input("Enter your passward: ")
check_passwaord_strength(passward)
    




