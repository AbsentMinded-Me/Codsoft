import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all the character sets
    all_characters = lowercase + uppercase + numbers + special_chars
    
    # Ensure the password has at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special_chars:
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string and return
    return ''.join(password)

def main():
    # Prompt the user for the desired password length
    length = int(input("Enter the desired length of the password: "))
    
    # Optionally, you can ask the user about complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    # Display the generated password
    print(f"Generated Password: {password}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
