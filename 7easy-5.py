'''Easy Question #5
Create a function vowel_or_cons that takes in a letter of the alphabet. If the letter is a, e, i, o or u, then your function should return the string 'vowel'. If the letter is y then your function should return the string 'vowel or consonant'. Otherwise your function should return the string 'consonant'.

For example:
vowel_or_cons('a') # 'vowel'
vowel_or_cons('y') # 'vowel or consonant'
vowel_or_cons('h') # 'consonant'

'''

def vowel_or_cons(l):
  if l in ('a', 'e', 'i', 'o', 'u'):
    return 'vowel'
  elif l == 'y':
    return 'vowel or consonant'
  else:
    return  'consonant'

  
print(vowel_or_cons('a'))
print(vowel_or_cons('y'))
print(vowel_or_cons('h'))