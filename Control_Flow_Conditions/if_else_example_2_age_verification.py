
theater_name = 'XYZ'
rated_r_age_limit = 18

print(f"Welcome to {theater_name} theatres!") #py3
# print("Welcome to {} theatres!".format(theater_name)) #py2 ana py3


user_input = input("Enter your age:")
print(f"User input is: {user_input}")

if int(user_input) >= rated_r_age_limit:
    print('Enjoy the movie')
else:
    if int(user_input) < rated_r_age_limit:
        print ('Sorry, you must be 18 yo to watch the movie.')
