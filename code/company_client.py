import requests

# # Request the root
# r = requests.get(r'http://localhost:8000/')

# print("--------------------------")
# print("Requesting root of my api, response is:")
# print(r.text)
# print("--------------------------")

# # Request all companies
# r = requests.get(r'http://localhost:8000/companies')

# print("--------------------------")
# print("Requesting all companies of my api, response is:")
# print(r.text)
# print("--------------------------")

# # Posts a new company
# company_details = {
#     "ticker": "PYPL",
#     "name": "PayPal",
#     "website": "www.paypal.com"
# }

# r = requests.post(r'http://localhost:8000/companies/', json=company_details)

# print("--------------------------")
# print("Posting a company to my api, response is:")
# print(r.text)
# print("--------------------------")

# # Request all companies
# r = requests.get(r'http://localhost:8000/companies')

# print("--------------------------")
# print("Requesting all companies of my api, response is:")
# print(r.text)
# print("--------------------------")

# # Posts an invalid company
# company_details = {
#     "code": "PYPL",
#     "name": "PayPal",
#     "website": "www.paypal.com"
# }

# r = requests.post(r'http://localhost:8000/companies/', json=company_details)

# print("--------------------------")
# print("Posting a company to my api, response is:")
# print(r.text)
# print("--------------------------")

# # Put request to update amazon to amazon.co.uk
# company_details = {
#     "ticker": "AMZN",
#     "name": "Amazon",
#     "website": "www.amazon.com"
# }

# r = requests.put(r'http://localhost:8000/companies/AMZN', json=company_details)

# print("--------------------------")
# print("Posting a company to my api, response is:")
# print(r.text)
# print("--------------------------")

# Delete a company by ticker
r = requests.delete(r'http://localhost:8000/companies/MSFT')

print("--------------------------")
print("Daleting a company of my api, response is:")
print(r.text)
print("--------------------------")
