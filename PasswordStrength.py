def main():
        email = input("Please enter your email: ")
        if "@" in email and "." in email:
            password()
        else:
            print("The email you entered is invalid, please try again.")
            main()
 
def password():
    password = input()
    special = "~!@#$%^&*()?"
    if len(password) < 8: 
        print("Your password is not long enough. (Minimum 8 characters in length)")
        password()
    if not password.islower() and not password.isupper() and not password.isalpha() and not password.isdigit() and any((c in special) for c in password):
        print("Strong enough password.")
    else:
        print("Weak Password, please try again.")
        password()

main()

#Need to make changes, not sure if this is actually going to generate a strong password.
