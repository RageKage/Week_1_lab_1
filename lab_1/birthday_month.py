
from datetime import datetime, date, time, timezone

today_date = datetime.now()

tt = today_date.timetuple() # this tells us the current date



months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
          7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"} # a dict of the month names and their number


ask_name = input("What is your name? ")

ask_born_month = input("What month were you born in? ")


print("Hello, " + ask_name + "!")

print("")

print(f"Your name has {len(ask_name)} characters.")


if ask_born_month.lower() == "August" or ask_born_month.lower() == "august": # check if they were born in August
    print(f"Happy birthday, {ask_name}!")

print("")
for month in months:
    if tt.tm_mon == month: # check if the current month match that they entered
        print(f"we are in the same current month {months[month]}")
        break # break the loop
    else:
        print(
            f"we are not in the same current month you typed '{ask_born_month}' but we are current in  {months[month]} ")
        break # break the loop
