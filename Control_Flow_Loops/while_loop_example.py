#
# # infinite_loop
# wy_var = True
# while wy_var:
#     print('abc')


# # infinite_loop
# counter = 1
# while True:
#     print(counter)
#     counter = counter + 1

# # good_loop
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter = counter + 2

main_number = 9
user_input = 0
while user_input != main_number:
    user_input = input("Enter a number 0 to 10:")
    user_input = int(user_input)
    print(f"You entered: {user_input}")
    print(user_input != main_number)
print("Done!")