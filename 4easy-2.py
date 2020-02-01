'''
Easy Question #2
Given a list of users, write a function, names_and_roles that returns all of user's names and roles in a string with each value labeled.

For example:
users = [
    {
         'name': 'Homer', 
         'role': 'Clerk', 
         'dob': '12/02/1988',
         'admin': False 
    }, 
    {
         'name': 'Lisa', 
         'role': 'Staff', 
         'dob': '01/30/1965',
         'admin': False 
    }, 
    {
         'name': 'Marge', 
         'role': 'Associate', 
         'dob': '09/10/1980',
         'admin': True 
    }
]

names_and_roles(users)
# Name: Homer
# Role: Clerk

# Name: Lisa
# Role: Staff

# Name: Marge
# Role: Associate
'''

users = [
    {
         'name': 'Homer', 
         'role': 'Clerk', 
         'dob': '12/02/1988',
         'admin': False 
    }, 
    {
         'name': 'Lisa', 
         'role': 'Staff', 
         'dob': '01/30/1965',
         'admin': False 
    }, 
    {
         'name': 'Marge', 
         'role': 'Associate', 
         'dob': '09/10/1980',
         'admin': True 
    }
]


def names_and_roles(users):
    userString=""
    for user in users:
        userName = user.get("name")
        role = user.get("role")
        userString = userString + "Name: " + userName + "\n" + "Role: " + role+"\n\n"
    return userString
        
print(names_and_roles(users))