import os

# db_user = "my_db_user"
# db_password = "my_db_pass_123"
# Värdet är sparat i miljövariabel.

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

print(EMAIL_USER)
print(EMAIL_PASS)
