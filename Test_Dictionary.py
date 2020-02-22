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

#Writing a program to read through a sentence and print the count of each words used in the sentence

count = dict()
sentence = input()
words = sentence.split()
print('Words:-',words)

for word in words:
    count[word]=count.get(word,0)+1
print('Counts:-',count)

for key in count:
    print(key,count[key])

# to print the keys,Values & Items using list
print(count.keys())
print(count.values())
print(count.items())
