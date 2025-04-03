# Idea: Update the email generator script so the data is received by prompt,
# and the data use correspond to the first name and the last name of the user,
# a company name and the domain suffix, replacing spaces with dots
# at the first and last name, also joining it with a dot , removing the spaces in the company name
#  and concatenating all asked elements.

# Example of received data:
#       first name: > 'Juan Carlos'
#       last name: > 'Gomez Lara'
#       company name: > 'Global Mentoring'
#       domain extension: > 'com.mx'

# Expected output string:
#       email = juan.carlos.gomez.lara@globalmentoring.com.mx

# Expected output from prompt:
# *** Email Generator ***
# (Empty line)
# What is your First and Middle Name?: > Juan Carlos
# What is your Last Name?: > Gomez Lara
# What is your Company's Name?: > Global Mentoring
# What is the Domain Extension to use?: > com.mx
# (Empty line)
# Hello Juan,
# Your new email for the company Global Mentoring is:
# (Empty line)
#     ubaldo.acosta.soto@globalmentoring.com.mx
#     Congratulation!

# Request the data needed to the user
print("*** Email Generator System ***")
first_n_middle_name = input("What is your First and Middle Name?: ")
last_name = input("What is your Last Name?: ")
company_name = input("What is your Company's Name?: ")
domain = input("What is the Domain Extension to use?: ")

# Process the data received from the prompt
first_n_middle_name = first_n_middle_name.strip().lower()
first_name = first_n_middle_name.split(' ')[0].capitalize()
names_data = first_n_middle_name.replace(' ', '.')

last_name_data = last_name.strip().replace(' ','.').lower()

company_name_data = company_name.strip().replace(' ','').lower()
normalized_domain = '@' + company_name_data + '.' + domain

# Finally we concatenate all the elements and get the final email
final_email = f'{names_data}.{last_name_data}{normalized_domain}'

response_text = (f"\nHello {first_name},\n"
                 f"\tYour new email for the company {company_name} is:\n"
                 f"\t{final_email}\n"
                 "\tCongratulations!"
                 )
print(response_text)