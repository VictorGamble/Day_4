const = "Victor Gamble"
#uppercase a string
#print(const.upper())

#capitalize string
#print(const.capitalize())

#reverse a string
#print(const[:: -1])

#translate
# word = "Victor Gamble"
# coverting_letters = ["A", "E", "G", "I", "O", "S", "T"]
# translators =       [4,3,6,2,0,5,7]
# transaltion = ""
# counter = 0

# while counter < len(word):
#     word.upper()
#     counter += 1
    




#Long-long vowels

vowels = "aeiou"
new_tex = ""
counter = 0

while counter < len(const):
    if const[counter] in vowels and (counter + 1) < len(const):
        if const[counter] == const[counter + 1]:
            new_tex = new_tex + (const[counter] * 3)
        else: 
            new_tex + const[counter]
    else:
    
        new_text = new_tex + const[counter]
        counter += 1
print(new_tex)












