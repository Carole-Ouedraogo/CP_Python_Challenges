'''Easy Question #1
Write a function called product_of_values which takes in a dictionary of key/value pairs and multiplies the values together. You can assume that all keys are strings and all values are integers.

For example:
test_dictionary = {
    'a': 5, 
    'b': 12,
    'c': 3
}

product_of_values(test_dictionary) # should return 180 because 5 * 12 * 3 = 180
'''
def product_of_values(test_dictionary):
  values = test_dictionary.values()
  result =1;
  for value in values:
      result = result*value
  return result

test_dictionary = {'a' : 5, 'b' : 12, 'c' : 3}
result = product_of_values(test_dictionary)
print((result))