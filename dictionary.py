"""
It is always represent in the form of:
my_dictionary = {"key":"Value"}
"""

# why we need dicionary?
#--> To overcome the prblem exist in list.
#For eg:
# user_detail=["Kasmi","Thapa",20,["English","Nepali","Japnese"],9845141112,["Burger","Pizza","Mo mo"]]

user_details = {
    "first_name":"Kasmi",
    "last_name":"Thapa",
    "Language_spoken":["English","Nepali","Japnese"],
    "contact":9845141112,
    "fav_food":["Burger","Pizza","Mo mo"]
}

# print(user_details["first_name"])


for key,value in user_details.items():
    print(f"The key is:{key} and its value is: {value}")


for key in user_details.keys():
    print(f"The key is:{key} ")


for value in user_details.values():
    print(f"And its value is: {value}")