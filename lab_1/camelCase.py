# get the string
A = "fOnt proCESSOR and ParsER"


#split the string
B = A.split()




#convert the first letter of each word to uppercase
for i in range(len(B)):
    B[i] = B[i].capitalize()
   
    

# change the first index to lowercase
B[0] = B[0].lower()


# join the words

Camel = "".join(B)

print(Camel)



    