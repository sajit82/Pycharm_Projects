# Implementation of dictionaries

purse = dict()
purse['money']=12
purse['candy']=3
print(purse)
print(purse['money'])
print(purse['candy'])

#getting the count of items in a dict using get() method

count = dict()
number =['343','234', '444','432','343']
print(count)

for num in number:
    count[num]=count.get(num,0)+1
print(count)

