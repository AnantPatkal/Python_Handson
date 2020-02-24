#String methods:
x=""" 3 Romeo and Juliet is a play written by Shakespeare. It is a tragic love story where the two main characters,
 Romeo and Juliet,  are supposed to be sworn enemies but fall in love. ...
 Romeo and Juliet is a Shakespearean tragedy. Two wealthy families, the Montagues and the Capulets, have another brawl in the city of Verona."""
#print(x)
#up=x.upper()
#print()
#print()
#print(up)
#print(x.index("brawl"))
#print(x.find("sense"))
#print(x.isalpha())
#print(x.isdecimal())#

#print(x.istitle())
#print(x.isdecimal())
#print(x.isdigit())

# slice example
word='Ihelpyouwhenyouneeditsochill'
print(word[0:-5:1])
#format =var[0:end:step]
print(word[1:5])
#reverse retrieval of slice
print(word[::-5])

#Slice using index()
print(word[word.index('you'):word.index('need')])
