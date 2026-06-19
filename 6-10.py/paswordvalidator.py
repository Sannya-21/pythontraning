import random
import string

# Custom Exception
class PasswordValidationError(Exception):
    pass


def generate_password(length=12):
    """Generate a strong random password."""
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def validate_password(password):
    """Validate password according to rules."""

    if len(password) < 8:
        raise PasswordValidationError(
            "Password must be at least 8 characters long."
        )

    if not any(char.isupper() for char in password):
        raise PasswordValidationError(
            "Password must contain at least one uppercase letter."
        )

    if not any(char.islower() for char in password):
        raise PasswordValidationError(
            "Password must contain at least one lowercase letter."
        )

    if not any(char.isdigit() for char in password):
        raise PasswordValidationError(
            "Password must contain at least one digit."
        )

    special_chars = string.punctuation
    if not any(char in special_chars for char in password):
        raise PasswordValidationError(
            "Password must contain at least one special character."
        )

    return True


# Main Program
print("Generated Strong Password:")
generated = generate_password()
print(generated)

print("\nPassword Validation")

user_password = input("Enter a password: ")

try:
    if validate_password(user_password):
        print("Password is valid and strong!")

except PasswordValidationError as e:
    print("Validation Error:", e)

except Exception as e:
    print("Unexpected Error:", e)