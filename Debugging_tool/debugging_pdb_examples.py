
# Official doc = https://docs.python.org/3/library/pdb.html
# c = continue
# n = next
# l = show current line
# s = step
# h = help
# pp = pretty print
""""""
import pdb

import pdb

# # demo 1
# print("I am the 1st line")
# fname = "Anna"
# lname = "Kalacheva"
#
# pdb.set_trace() #key point
#
# print("I am the 2nd line") #enter n - next
# print("I am the 3rd line")
# print(f"first name is {fname} and last name is {lname}")


# demo 2
def get_user_name(name):              # function
    user_names = {"anna": "ak",       # dictionary
                  "joe": "joe99",
                  "mary": "marryrock2323"}
    print(f"The user {user_names[name]} is logged in.")
    #pdb.set_trace()

    return user_names[name]

user_1 = get_user_name("anna")
print("User 1:" + user_1)
pdb.set_trace()

user_2 = get_user_name("joe")
print("User 2:" + user_2)

user_3 = get_user_name("mary")
print("User 3:" + user_3)