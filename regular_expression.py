# Simple script to practice regular expression
# Here, we are checking if a credit card number is found
import re


string = """A string we are using to filter specific items.
perhaps we would like to match credit card numbers
mistakenly entered into the user input. 4444 3232 1010 8989
and perhaps another? 9191 0232 9999 1111"""

# Define the searching pattern (e.g search for 4 digit followed by a space of more, 4 times)
pattern = '(([0-9](\s+)?){4}){4}'

found = re.search(pattern, string)

if found:
    print("Found a credit card number!")
else:
    print("No credit card numbers present in input")

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
     [a-zA-Z0-9.-]+     # domain name
     (\.[a-zA-Z]{2,4})  # dot-something
  )''', re.VERBOSE)

matches = []
text = """
An example text containing an email address, such as user@example.com or something like hello@example.com
"""

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# matches => ['user@example.com', 'hello@example.com']
print(matches)
