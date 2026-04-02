# pip install requests

import requests

# Paste your access token here
access_token = "EAAR0ZAhPwkuEBRDFIvojUZCZBAwsOtUGIfNTZBK5DCZAShuczZAnTqbMmSdu114x4kAkrqoH4e90snkctj7jP7iRk7mMlTk0kSY8fdIr9YZAupvSDZBCW23YMR3mRkCNsZADZBoKNquDk5kO4sNaRbfVZCV3NwG3YjiYQeQGB4FQW9Hb6ZC533zjpc8ZCozO2exEdLZBr6"

# Get basic profile data
url = "https://graph.facebook.com/me?access_token=" + access_token

response = requests.get(url)
data = response.json()

# Print output
print("Name:", data["name"])
print("ID:", data["id"])
