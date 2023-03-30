
# main_number = 15
# user_input = 0
# while user_input != main_number:
#     user_input = input("Guess a number 0 to 20:")
#     user_input = int(user_input)
#     print(f"You entered: {user_input}")
#     print(user_input != main_number)
# print("Done!")

# Example 1
# main_number = 15
# while True:
#     user_input = input("Guess a number 0 to 20:")
#     print(f"You entered: {user_input}")
#     if int(user_input) == main_number:
#         break
#     # else:
#     #     continue
#
# print("Done!")


# # Example 2
# # given a country print its capital city if it is in the given set of data, else print 'unknown'.
# capitals = {
#     "Peru": "Lima",
#     "Philippines": "Manila",
#     "Spain": "Madrid",
#     "Ethiopia": "Addis Ababa",
#     "Ghana": "Accra",
#     "USA": ""
# }
# user_input = 'usa'
# for k, v in capitals.items():   #k -countries, v-capitals
#     # print("current country: " + k)
#     if user_input.lower() == k.lower():
#         if v:
#             print("capital is: " + v)
#         else:
#             print('Unknown')
#         break #exit


# Example 3
# given a dictionary with book prices and list of courses, calculate total cost of books
book_prices = {"calculus": 300, "physics": 255, "chemistry": 400, "english": 150, "theater": 100} #dictionary
my_courses = ["physics", "english", "psychology", "calculus", "history"] #list
total_cost = 0
for course in my_courses:
    if course in book_prices:
        total_cost = total_cost + book_prices[course]

# print("Total books cost: {}".format(total_cost))
#or
print( f"Total books cost: {total_cost}")