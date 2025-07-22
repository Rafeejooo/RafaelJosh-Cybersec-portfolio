import re
import math

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'[0-9]', password):
        charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset += 32
    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return entropy

def strength_level(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    entropy = calculate_entropy(password)
    level = strength_level(entropy)
    print(f"\nPassword Entropy: {entropy:.2f} bits")
    print(f"Strength: {level}")

if __name__ == "__main__":
    main()
