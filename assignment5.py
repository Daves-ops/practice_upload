# Initialize an empty list to store users' information
usersList = []

# Prompt the user to create a username
userName = input('Create a username: ')
print(f'Welcome, {userName}! Let’s collect some additional information.')

# Collecting data for the user
print('\nCollecting data:')
    
# Collecting the user's name
name = input('Enter your full name: ')

# Collecting hair color and eye color, stored as a tuple
hair = input('Enter your hair color: ')
eye = input('Enter your eye color: ')
traits = (hair, eye)  # Store hair and eye colors in a tuple

# Collecting city and state, stored as a dictionary
city = input('Enter your city: ')
state = input('Enter your state: ')
location = {'city': city, 'state': state}  # Store city and state in a dictionary

# Creating a dictionary for the user's information
userInfo = {'username': userName, 'name': name, 'traits': traits, 'location': location}

# Append the user dictionary to the list
usersList.append(userInfo)

# Display collected user info
print('\nCollected user info:')
for user in usersList:
    print(user)
