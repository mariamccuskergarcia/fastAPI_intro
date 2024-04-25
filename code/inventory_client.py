import requests

# # Getting all items
# r = requests.get(r'http://localhost:8000/items')

# print("--------------------------")
# print("Getting all items:")
# print(r.text)
# print("--------------------------")

# # Posts a new item
# new_item = {
#         "tag": "appletv3",
#         "price": 300,
#         "name": "Apple TV"
# }

# r = requests.post(r'http://localhost:8000/items', json=new_item)

# print("--------------------------")
# print("Posting a new item to my api, response is:")
# print(r.text)
# print("The response code:")
# print(r.status_code)
# print("--------------------------")

# # Update item
# updated_item = {
#         "tag": "appletv3",
#         "price": 400,
#         "name": "Apple TV"
# }

# r = requests.put(r'http://localhost:8000/items/appletv3', json=updated_item)

# print("--------------------------")
# print("Updating an item, response is:")
# print(r.text)
# print("The response code:")
# print(r.status_code)
# print("--------------------------")

# Delete item
r = requests.delete(r'http://localhost:8000/items/appletv3')

print("--------------------------")
print("Deleting an item, response is:")
print(r.text)
print("The response code:")
print(r.status_code)
print("--------------------------")

