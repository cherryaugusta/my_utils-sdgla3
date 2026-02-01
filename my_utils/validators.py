"""
validators.py

This module contains validation-related utility functions.
"""

def is_valid_email(email_string: str) -> bool:
    """
    Validate an email address using simple structural rules.

    Validation rules:
    - Must contain exactly one '@' symbol
    - Must contain at least one '.' after the '@' symbol
    - Local and domain parts must be non-empty

    Parameters:
        email_string (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """

    # Ensure input is a string
    if not isinstance(email_string, str):
        return False

    # Email must contain exactly one '@'
    if email_string.count("@") != 1:
        return False

    # Split into local and domain parts
    local_part, domain_part = email_string.split("@")

    # Both parts must be non-empty
    if not local_part or not domain_part:
        return False

    # Domain must contain at least one dot
    if "." not in domain_part:
        return False

    # Dot cannot be at the beginning or end of the domain
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False

    return True
