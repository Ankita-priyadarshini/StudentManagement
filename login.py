def login():
    """
    Handles user login functionality.
    Prompts the user for their username and password, and verifies the credentials.
    If the credentials are valid, the user is logged in; otherwise, an error message is displayed.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Here you would typically check the credentials against a database or a predefined list
    if verify_credentials(username, password):
        print("Login successful!")
        # Proceed with the application flow after successful login
    else:
        print("Invalid username or password. Please try again.")