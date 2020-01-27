while True:
      line =input('>' )
      if   line[0]=="#":
           continue
      elif line=="Done":
           break
      print(line)
print("Done!")

for i in [1,2,3,4,5]:
    print(i)

largest_nbr =-1
for the_num in [2,45,76,98,4]:
    if the_num>largest_nbr:
       largest_nbr=the_num
    print("Largest Nbr so far",largest_nbr)
print('Final Largest Number',largest_nbr)