fruit = 'banana'

for letter in fruit:
    print(letter)
greet ='HELLO'
zap =greet.lower()
print(zap)
pos =greet.find('EL')
print(pos)
nstr=greet.replace('L','X')
print(nstr)
whtspc =greet. lstrip()
print(whtspc)
gmail='smca041@gmail.com'
atpos=gmail.find('@')
print(atpos)
sppos=gmail.find('.',atpos)
print(sppos)
data=gmail[atpos+1:sppos]
print(data)