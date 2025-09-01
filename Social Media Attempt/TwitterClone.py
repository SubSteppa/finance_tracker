import hashlib
import os
import getpass

CREDENTIALS_FILE = "credentials.txt"


def hash_password(password):
    """Return SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


def signup():
    print("\n--- Signup ---")
    user_name = input("Enter Username: ")
    email = input("Enter Email Address: ")
    pwd = getpass.getpass("Enter Password: ")
    conf_pwd = getpass.getpass("Confirm Password: ")

    if pwd != conf_pwd:
        print("Passwords do not match!\n")
        return

    if len(pwd) < 4:
        print("Password too short! Must be at least 4 characters.\n")
        return

    # Check for duplicate email
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            users = f.readlines()
        existing_emails = [user.strip().split(",")[1]
                           for user in users if len(user.strip().split(",")) == 3]
    else:
        existing_emails = []

    if email in existing_emails:
        print("This email is already registered. Please use a different email.\n")
        return

    user_data = f"{user_name},{email},{hash_password(pwd)}\n"

    # Append user to the file
    with open(CREDENTIALS_FILE, "a") as f:
        f.write(user_data)

    print("You have registered successfully!\n")


def login():
    print("\n--- Login ---")
    email = input("Enter Email Address: ")
    pwd = getpass.getpass("Enter Password: ")
    pwd_hash = hash_password(pwd)

    if not os.path.exists(CREDENTIALS_FILE):
        print("No users registered yet!\n")
        return None  # return None if login fails

    with open(CREDENTIALS_FILE, "r") as f:
        users = f.readlines()

    for user in users:
        parts = user.strip().split(",")
        if len(parts) != 3:
            continue
        username_stored, email_stored, pwd_stored = parts
        if email == email_stored and pwd_hash == pwd_stored:
            print(f"Login successful! Welcome, {username_stored}\n")
            return username_stored  # return the username

    print("Invalid email or password.\n")
    return None


def post(user_name):
    content = input("Enter your post: ")

    if len(content) > 200:
        print('Maximum character limit is 200')
        return
    with open("tweets.txt", "a") as f:
        f.write(f"{user_name}: {content}\n")

    print("Tweet posted!")


def main():
    logged_in_user = None

    while True:
        if logged_in_user:
            # Logged-in menu
            print(f"\n--- Logged in as: {logged_in_user} ---")
            print("1. Post a Tweet")
            print("2. Logout")
            print("3. Exit")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                post(logged_in_user)
            elif ch == 2:
                print(f"{logged_in_user} logged out.\n")
                logged_in_user = None
            elif ch == 3:
                print("Goodbye!")
                break
            else:
                print("Wrong choice! Try again.\n")

        else:
            # Not logged-in menu
            print("\n********** Login System **********")
            print("1. Signup")
            print("2. Login")
            print("3. Exit")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                signup()
            elif ch == 2:
                username = login()
                if username:
                    logged_in_user = username  # User stays logged in
            elif ch == 3:
                print("Goodbye!")
                break
            else:
                print("Wrong choice! Try again.\n")


if __name__ == "__main__":
    main()
