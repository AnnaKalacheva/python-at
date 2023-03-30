


theater_name = 'XYZ'
rated_r_age_limit = 18

print(f"Welcome to {theater_name} theatres!") #py3

user_input = input("Enter your age:")
print(f"User input is: {user_input}")

if int(user_input) >= rated_r_age_limit:
    print('Enjoy the movie')
else:
  adult_present = input('Is another adult with you? yes or no:')
  if adult_present.lower() == "yes":
    print('Enjoy the movie')
  else:
    print(f"You must watch 18 yo to watch the movie or to be with an adult.")
