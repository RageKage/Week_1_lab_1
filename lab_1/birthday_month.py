
ask_name =  input("What is your name? ")

ask_born_month = input("What month were you born in? ")

print("Hello, " + ask_name + "!")

print ("")

print(f"Your name has {len(ask_name)} characters.")

print(ask_born_month.islower())

if ask_born_month.islower() == "a":
    print("Please enter your name in all lowercase letters.")

# if ask_born_month.islower() == "a":
#     print(f"Happy birthday, {ask_name}!")
    
    

