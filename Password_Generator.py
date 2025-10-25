import random
import pyperclip

#Colours
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

#Password Length
def get_password(length):
    letters_lower="abcdefghijklmnopqrstuvwxyz"
    letters_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="1234567890"
    symbols="!@#$%^&*()_-+="
    all_chars=letters_lower+letters_upper+numbers+symbols
    password_chars=[ # although it is slightly worse for security I have decided to keep this for the case that the user wants a password of length 4 as it'd save time in that case 
        random.choice(letters_lower),
        random.choice(letters_upper),
        random.choice(numbers),
        random.choice(symbols)
    ]
    if length<4:
        print(f"{RED}Password length should be atleast 4 to include all character types.{RESET}")
        return None
    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))
    random.shuffle(password_chars)
    password="".join(password_chars)
    return password

#Password Strength Checker
def password_checker(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper()for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()_-+=" for c in password)

    score = 3
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    # all of these if conditions are redundant as the password is hardcoded to meet all of these conditions to begin with, simply initialize score to 3 
    #if has_lower and has_upper:
    #    score += 1
    #if has_digit:
    #    score += 1
    #if has_symbol:
    #    score += 1

    return score

#Main Function
def main():
    try:
        length=int(input("Enter length of your password (12 or above is recommended, 4 is the minimum): "))
        password = get_password(length)
        if password:
            strength = password_checker(password)
            print(f"Password strength: {strength}/5 \n")
            print(f"\n{CYAN}Your generated password is: {RESET}{password}")
            
            copy = input("Do you want to copy password?(yes/no):")
            if copy.lower() in ['yes' or 'y']:
                pyperclip.copy(password)
                print(f"{GREEN}Password is copied to clipboard!{RESET}")
            else:
                print(f"{YELLOW}Password is not copied to clipboard!{RESET}")

    except ValueError:
        print(f"{RED}Please enter valid number for length.{RESET}")
if __name__=="__main__":
    while True:
        main()
        again=input("Do you want to generate another password?(yes/no): ")
        if again.lower() != 'yes':
            print(f"{CYAN}Exiting Password Generator{RESET}")

            break
