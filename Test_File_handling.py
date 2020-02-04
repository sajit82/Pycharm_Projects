import os

fhand=open('File_Testing.txt')
fhand=fhand.read()
length=len(fhand)

print(length)
print(fhand[0:5])
if fhand.startswith("K"):
    print(fhand[0])
else:
    print("Incorrect file")
filename ='Test_Sample.txt'
os.chdir('C:\\Users\Sajit Babu\Desktop')
fdata = open('Test_Sample.txt')
fdata =fdata.read()
print(len(fdata))
