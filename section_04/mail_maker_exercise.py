# Idea: Create an email generator script that returns a string after declaring 
# a name, a company name and a domain suffix, replacing spaces with dots
# at the name, removing the spaces in the company name and concatenating all
# asked elements.

# Example of input string:
#       name = 'Ubaldo Acosta Soto'
#       company = 'Global Mentoring'
#       domain = 'com.mx'

# Expected output string:
#       email = ubaldo.acosta.soto@globalmentoring.com.mx

# Expected output from prompt:
# *** Email Generator ***
# (Empty line)
# User Name: Ubaldo Acosta Soto
# Normalized User Name: ubaldo.acosta.soto
# (Empty line)
# Company Name: Global Mentoring
# Domain Extension: com.mx
# Normalized Email Domain: @globalmentoring.com.mx
# (Empty line)
# Final Generated Email: ubaldo.acosta.soto@globalmentoring.com.mx

# RESOLUTION SCRIPT
name = 'Ubaldo Acosta Soto'
company = 'Global Mentoring'
domain = 'com.mx'

# First we change the name to lower case and replace the spaces with dots
normalized_name = name.lower().strip().replace(' ', '.')

# Then we remove the spaces in the company name
normalized_company = company.lower().replace(' ', '')

# And concatenate with the domain extension
normalized_domain = '@' + normalized_company + '.' + domain

# Finally we concatenate all the elements and get the final email
final_email = normalized_name + normalized_domain

# Then proceed to print the result in the format requested
print("*** Email Generator ***\n")
print(f"User Name: {name}")
print(f"Normalized User Name: {normalized_name}\n")
print(f"Company Name: {company}")
print(f"Domain Extension: {domain}")
print(f"Normalized Email Domain: {normalized_domain}\n")
print(f"Final Generated Email: {final_email}")
# END OF SCRIPT