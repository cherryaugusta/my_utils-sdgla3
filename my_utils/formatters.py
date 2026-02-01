"""
formatters.py

This module contains formatting-related utility functions.
"""

def format_dict_for_log(data_dict: dict) -> str:
    """
    Format a dictionary into a log-friendly multiline string.

    Each key-value pair is placed on a new line using the format:
    KEY => VALUE

    Parameters:
        data_dict (dict): Dictionary containing log data.

    Returns:
        str: A formatted string suitable for logging.

    Raises:
        TypeError: If the input is not a dictionary.
    """

    # Ensure input is a dictionary
    if not isinstance(data_dict, dict):
        raise TypeError("Input must be a dictionary")

    # Convert dictionary entries to formatted lines
    formatted_lines = [
        f"{key} => {value}"
        for key, value in data_dict.items()
    ]

    # Join lines into a single string
    return "\n".join(formatted_lines)
