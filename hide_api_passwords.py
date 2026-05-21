import os

db_user = os.environ.get('USER_DB')
db_password = os.environ.get('USER_PASS')

print(db_user, db_password)

# this is done to hide passwords and api keys when pushing into repos and sharing the code with others