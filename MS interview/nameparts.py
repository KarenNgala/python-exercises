# you can write to stdout for debugging purposes, e.g.
import re
server_names = [
    "Franklin D. Roosevelt",
    "Bobby Drop Tables",
    "Salvador Domingo Felipe Jacinto Dalí i Domènech",
    "Franklin Tables Salvador Bobby"
]

# import re
# re.split('[._]', email_parts[0])

def matchNames(email):
    matches = []
    email_parts = email.split('@')
    name_parts = re.split('[._]', email_parts[0])
    
    for name in server_names:
        individual_names = name.lower().split(" ")
        if name_parts[0] in individual_names and name_parts[1] in individual_names:
            matches.append(name, n)
