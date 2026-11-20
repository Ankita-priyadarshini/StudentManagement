def register():
    """
    Function to handle user registration.
    This function collects user information, validates it, and stores it in the database.
    """
    # Collect user information
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")

    # Validate user information
    if not username or not password or not email:
        print("All fields are required.")
        return

    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return

    # Store user information in the database (pseudo code)
    try:
        # Assuming we have a function `save_user_to_db` that saves the user info
        save_user_to_db(username, password, email)
        print("Registration successful!")
    except Exception as e:
        print(f"An error occurred during registration: {e}")