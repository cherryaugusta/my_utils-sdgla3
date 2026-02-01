from my_utils import is_valid_email, format_dict_for_log

# Email validation tests
emails = [
    "user@example.com",
    "invalid-email",
    "user@domain",
    "@example.com",
    "user@.com",
]

for email in emails:
    print(f"{email} -> {is_valid_email(email)}")

print()

# Dictionary formatting test
log_data = {
    "status": "ERROR",
    "code": 500,
    "service": "authentication",
}

formatted_log = format_dict_for_log(log_data)
print(formatted_log)
