'''Medium Question #1
Write a function called to_rodcase that takes in a string and returns it as a camelcased string with the 'ROD' between each word instead of spaces.

Example:
to_rodcase("Hello there stealth warrior") // should return 'helloRODThereRODStealthRODWarrior'
to_rodcase("I am excited to learn how to code") // should return 'iRODAmRODExcitedRODToRODLearnRODHowRODToRODCode'

other option:
def to_rodcase(word):
        import re
        str1 =(('ROD'.join(x.capitalize() for x in word.split(' ') )))
        print(str1[0:1].lower() + str1[1:]))
to_rodcase('Hello there stealth warrior')
to_rodcase('I am excited to learn how to code')


'''

def to_rodcase(string):
    word_list=string.split() #split the string into list of words
    rodcase_string=word_list[0].lower() #lowercase the first word

    for i in range(1,len(word_list)): #for each word from second word
        rodcase_string=rodcase_string+'ROD'+word_list[i].title() #append 'ROD' and uppercase the first letter of word
    return rodcase_string #return new_string

print(to_rodcase("Hello there stealth warrior"))
print(to_rodcase("I am excited to learn how to code"))