fruit ="banana"
'n' in fruit
print(fruit.upper())
#searching a string
pos =fruit.find("na")
print (pos)

# search and Replace

chng = fruit.replace('na','xa')
print(chng)

# stripping white space

greet = "   Hello    Sajit     "
print(greet)
greet.lstrip()
print(greet.lstrip())
greet.rstrip()
print(greet)

#Prefix

line ='Have a nice day'
print(line.startswith('h'))

#Parsing and Extracting

data ='smca041@gmail.com  5:24 pm'
atpos = data.find('@')
print(atpos)
sppos =data.find(' ',atpos)
print(sppos)
host =data[atpos+1:sppos]
print(host)