"""vowels =0
consonent=0

for letter in 'Hello':
    if letter.lower() in 'aeiou':
        vowels=vowels+1
    elif letter==" ":
        pass
    else :
        consonent=consonent+1
print("Vowels count :{}".format(vowels))
print("consonent count: {} ".format(consonent))
"""

Student_dict={
"Male":["Anant","Morris","Mith"],
"Female":["Vrushali","Tejashree","Kiara"]
}
print(Student_dict.keys())
val=Student_dict.values()

for key in Student_dict.keys():
 for val in Student_dict[key]:
  if "a" not in val:
     print(val)
 #else:
#     print('nothing found with "A"')
