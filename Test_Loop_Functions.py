large_num = None
small_num = None

while True:
    # try:
    nbr = input("Enter Number")

    if nbr == "Done":
        break
    try:
        nbr=int(nbr)
    except:

         print('Enter Valid Nbr')
         continue
    if large_num is None:
        large_num = nbr
    elif large_num < nbr:
         large_num = nbr
    if small_num is None:
       small_num = nbr
    elif small_num > nbr:
         small_num = nbr
# Except:
# Print("Enter Valid nbr")


print("largest Number", large_num)
print("Smallest Number", small_num)
# print(line)
for i in [1, 2, 3, 4, 5]:
    print(i)

largest_nbr = -1
for the_num in [2, 45, 76, 98, 4]:
    if the_num > largest_nbr:
        largest_nbr = the_num
    print("Largest Nbr so far", largest_nbr)
print('Final Largest Number', largest_nbr)
