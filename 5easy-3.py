'''
Easy Question #3
This is an extension of question #2. 
Given a list of dictionaries, write a function admin that returns the name and birthdate of all users that are marked as "admin".

For example:
users = [
    {
        'name': 'Homer', 
        'role': 'clerk', 
        'dob': '12/02/1988',
        'admin': False 
    }, 
    {
        'name': 'Lisa', 
        'role': 'staff', 
        'dob': '01/30/1965',
        'admin': False 
    }, 
    {
        'name': 'Marge', 
        'role': 'associate', 
        'dob': '09/10/1980',
        'admin': True 
    }
]

admin(users)
# Name: Marge 
# Dob: 09/10/1980

'''

users = [
    {
        'name': 'Homer', 
        'role': 'clerk', 
        'dob': '12/02/1988',
        'admin': False 
    }, 
    {
        'name': 'Lisa', 
        'role': 'staff', 
        'dob': '01/30/1965',
        'admin': False 
    }, 
    {
        'name': 'Marge', 
        'role': 'associate', 
        'dob': '09/10/1980',
        'admin': True 
    }
]
def admin(users):
    userString=""
    for user in users:
        userName = user.get("name")
        userDob = user.get("dob")
        if(user.get("admin") == True): # adding the condition 
        	userString = userString+"Name: "+ userName+"\n"+"Dob: " + userDob + "\n\n"
    return userString
print(admin(users))
        