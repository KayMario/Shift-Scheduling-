#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
import calendar
import random
import pandas as pd
from datetime import datetime

# Names of company staff
staff_members = ["Kwadwo Baah", "Benjamine Sarfo", "Aboagye Hanson", "Yussif Prince", 
                 "Solomon Tetteh", "Osei Kwabena", "Enoch Atinyo", 
                 "Ohene Mesitso", "Prince Sey", "Edem Johnson", 
                 "Isaac Amoah", "Joseph Adam", "Richard Kwao"]

# Daily and Monthly Schedule
def generate_daily_schedule(weekday, previous_evening_shift, previous_off_shift,day,week_of_month,week_one_list_,week_two_list_,week_three_list_,week_four_list_):
    off_shift = []
    if week_of_month == 1:
        if weekday < 5: # Weekday (Monday to Friday) 
            if day == 1:            
                # Subtract individuals from the previous day's evening shift from the morning shift
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift)- set(previous_off_shift), 1)
                afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 5)
                evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 3)
                off_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - set(evening_shift),2)
                previous_off_shift = off_shift
                week_one_list_.append(off_shift)                
            elif weekday == 0 and day != 1:
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift)- set(previous_off_shift), 1)
                afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 5)
                evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 3)
                off_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - set(evening_shift),2)
                previous_off_shift = off_shift
                week_one_list_.append(off_shift)
            elif day == 2:
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift)- set(previous_off_shift), 1)
                afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift), 5)
                evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift), 3)
                off_shift = previous_off_shift
                week_one_list_.append(off_shift)
            elif day > 2 and day % 2 != 0:
                off_shift = random.sample(set(staff_members) - set(previous_off_shift)- {"Kwadwo Baah", "Benjamine Sarfo"},2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift) - set(off_shift), 1)
                afternoon_shift = random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(off_shift) , 5)
                evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - set(previous_off_shift), 3)
                week_one_list_.append(off_shift)
            elif day > 2 and day % 2 == 0:
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift)- set(previous_off_shift), 1)
                afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift), 5)
                evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift), 3)          
                off_shift = previous_off_shift
                week_one_list_.append(off_shift)
        else:  # Weekend (Saturday or Sunday)
            morning_shift = random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift), 3)
            off_shift = ["Kwadwo Baah", "Benjamine Sarfo"]
            afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 5)
            evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 3)
    
    elif week_of_month == 2:
        if weekday < 5:
            if weekday == 0:
                week_one_list = [name for sublist in week_one_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_one_list) - {"Kwadwo Baah", "Benjamine Sarfo"},2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_two_list_.append(off_shift)
                previous_off_shift = off_shift
            elif weekday != 0 and weekday % 2 != 0:
                off_shift = previous_off_shift
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift) -{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_two_list_.append(off_shift)
            elif weekday != 0 and weekday % 2 == 0:
                week_one_list = [name for sublist in week_one_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_one_list)- {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift),2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_two_list_.append(off_shift)
        else:
            morning_shift = random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift), 3)
            off_shift = ["Kwadwo Baah", "Benjamine Sarfo"]
            afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 5)
            evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 3)
    
    elif week_of_month == 3:
        if weekday < 5:
            if weekday == 0:
                week_two_list = [name for sublist in week_two_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_two_list) - {"Kwadwo Baah", "Benjamine Sarfo"},2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_three_list_.append(off_shift)
                previous_off_shift = off_shift
            elif weekday != 0 and weekday % 2 != 0:
                off_shift = previous_off_shift
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_three_list_.append(off_shift)
            elif weekday != 0 and weekday % 2 == 0:
                week_two_list = [name for sublist in week_two_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_two_list)- {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift),2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_three_list_.append(off_shift)
        else:
            morning_shift = random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift), 3)
            off_shift = ["Kwadwo Baah", "Benjamine Sarfo"]
            afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 5)
            evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 3)
    
    elif week_of_month == 4:
        if weekday < 5:
            if weekday == 0:
                week_three_list = [name for sublist in week_three_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_three_list) - {"Kwadwo Baah", "Benjamine Sarfo"},2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_four_list_.append(off_shift)
                previous_off_shift = off_shift
            elif weekday != 0 and weekday % 2 != 0:
                off_shift = previous_off_shift
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_four_list_.append(off_shift)
            elif weekday != 0 and weekday % 2 == 0:
                week_three_list = [name for sublist in week_three_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_three_list)- {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift),2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                week_four_list_.append(off_shift)
        else:
            morning_shift = random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift), 3)
            off_shift = ["Kwadwo Baah", "Benjamine Sarfo"]
            afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 5)
            evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 3)
    else:
        if weekday < 5:
            if weekday == 0:
                week_four_list = [name for sublist in week_four_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_four_list) - {"Kwadwo Baah", "Benjamine Sarfo"},2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
                previous_off_shift = off_shift
            elif weekday != 0 and weekday % 2 != 0:
                off_shift = previous_off_shift
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
            elif weekday != 0 and weekday % 2 == 0:
                week_four_list = [name for sublist in week_four_list_ for name in sublist]
                off_shift = random.sample(set(staff_members) - set(week_four_list)- {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_off_shift),2)
                morning_shift = ["Kwadwo Baah", "Benjamine Sarfo"] + random.sample(set(staff_members) - set(off_shift) - set(previous_evening_shift)-{"Kwadwo Baah", "Benjamine Sarfo"},1)
                afternoon_shift = random.sample(set(staff_members) - set(off_shift) - set(morning_shift),5)
                evening_shift = random.sample(set(staff_members)-set(off_shift)-set(morning_shift)-set(afternoon_shift),3)
        else:
            morning_shift = random.sample(set(staff_members) - {"Kwadwo Baah", "Benjamine Sarfo"} - set(previous_evening_shift), 3)
            off_shift = ["Kwadwo Baah", "Benjamine Sarfo"]
            afternoon_shift = random.sample(set(staff_members) - set(morning_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 5)
            evening_shift = random.sample(set(staff_members) - set(morning_shift) - set(afternoon_shift) - {"Kwadwo Baah", "Benjamine Sarfo"}, 3)

        
            
    return {"Morning": morning_shift, "Afternoon": afternoon_shift, "Evening": evening_shift, "Off": off_shift}

# Function to generate schedule for the entire month
def generate_monthly_schedule(year, month):
    # Get the number of days in the month
    num_days = calendar.monthrange(year, month)[1]

    # Initialize the schedule dictionary
    schedule = {}

    # Initialize the list to track individuals from the previous day's evening shift
    previous_evening_shift = []
    previous_off_shift = []
    previous_week_number = None
    week_of_month = 1
    week_one_list_ = []
    week_two_list_ = []
    week_three_list_ = []
    week_four_list_ = []

    # Generate schedule for each day
    for day in range(1, num_days + 1):
        date = f"{year}-{month:02d}-{day:02d}"
        weekday = calendar.weekday(year, month, day)
        date_object = datetime(year, month, day)
        week_num = date_object.isocalendar()[1] 
        
        if previous_week_number is None:
            previous_week_number = week_num
        elif week_num != previous_week_number:
            week_of_month += 1
            previous_week_number = week_num
        
        schedule[date] = generate_daily_schedule(weekday, previous_evening_shift, previous_off_shift,day,week_of_month,week_one_list_,week_two_list_,week_three_list_,week_four_list_)
        
        # Update the list of individuals from the previous day's evening shift
        previous_evening_shift = schedule[date]["Evening"]
        # Update the off_shift for the next iteration
        previous_off_shift = schedule[date]["Off"]

    return schedule

#Input Schedule Month
month_input = int(input("Enter the month: "))

# Generate and display the schedule for the month
monthly_schedule = generate_monthly_schedule(2024, month_input)

for date, shifts in monthly_schedule.items():
    print(date)
    print(f"Morning shift: {shifts['Morning']}")
    print(f"Afternoon shift: {shifts['Afternoon']}")
    print(f"Evening shift: {shifts['Evening']}")
    print(f"Off Day: {shifts['Off']}")
    print()

# Export to an Excel file
df = pd.DataFrame(monthly_schedule).transpose()
df.head()
df.to_excel("schedule.xlsx")

