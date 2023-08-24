
from datetime import datetime, date, time, timezone



# ask_name =  input("What is your name? ")

# ask_born_month = input("What month were you born in? ")

# print("Hello, " + ask_name + "!")

# print ("")

# print(f"Your name has {len(ask_name)} characters.")



# if ask_born_month.lower() == "August" or ask_born_month.lower() == "august":
#     print(f"Happy birthday, {ask_name}!")

today_date = datetime.now()

tt = today_date.timetuple()

a = 8


months = [{1, "January"}, { 2, "February"}, { 3, "March"}, { 4, "April"}, { 5, "May"}, { 6, "June"}, { 7, "July"}, { 8, "August"}, { 9, "September"}, { 10, "October"}, { 11, "November"}, { 12, "December"}]


print(tt.tm_mon)



    


    
    

