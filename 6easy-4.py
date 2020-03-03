''' Easy Question #4
Write a function called odds_up_to that returns a list with every odd number up to a given digit.

For example:
odds_up_to(20) # [1,3,5,7,9,11,13,15,17,19]

1- Define a function that takes in a number.
2- create a list of element to store odd numbers .
3- For each number in the range, check if it is odd number.
4- Add the odd numbers to the resulting list.
5- Display all the the numbers within the list
6- Return the list of odd numbers
7- Call the function and display the result.

'''

def odds_up_to(numb):
    oddNumbers = []  # creating new list
    for i in range(1, numb+1):
        if i%2 != 0:
        	oddNumbers.append(i)
        	print(i, end = " ")
    return oddNumbers
    
print(odds_up_to(20))