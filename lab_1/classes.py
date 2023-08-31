

print("Enter all of the current classes your taking this year")


num_of_classes = int(input("How many classes are you taking this year? "))

classes = [] # an empty list to store the classes

for i in range(num_of_classes):
    classes.append(input("Enter a class: ")) # append the class to the list
for i in classes:
    print(i)