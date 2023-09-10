# Script to generate a random strong password

import random
import string

word_length = 18

# Generate a list of letters, digits, and some punctuation
components = [string.ascii_letters, string.digits, "!@#$%&"]

# Flatten the components into a list of characters
chars = [item for list in components for item in list]

generated_password = "".join([random.choice(chars)
                             for i in range(word_length)])

print(generated_password)
