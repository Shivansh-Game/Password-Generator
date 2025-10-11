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
    password_chars=[
        random.choice(letters_lower),
        random.choice(letters_upper),
        random.choice(numbers),
        random.choice(symbols)
    ]
    if length<4:
        print(f"{RED}Password length should be atleast 4 to include all character types.{RESET}")
        return None
    all_chars=letters_lower+letters_upper+numbers+symbols
    for _ in range(length-4):
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

    score = 0
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if has_lower and has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return f"{RED}Weak{RESET}"
    elif score in [3, 4]:
        return f"{YELLOW}Medium{RESET}"
    else:
        return f"{GREEN}Strong{RESET}"

#Main Function
def main():
    try:
        length=int(input("Enter length of your password: "))
        password = get_password(length)
        if password:
            print(f"\n{CYAN}Your generated password is: {RESET}{password}")
            strength = password_checker(password)
            print(f"Password strength: {strength}\n")
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