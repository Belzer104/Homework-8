from datetime import datetime

def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    b_day = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday":[],
    "Thursday":[],
    "Friday":[],
    "Saturday":[],
    "Sunday":[],
  }
    
    for items in users:
        for keys, values in items.items():
            if keys == "birthday":
                birthday_date = values.replace(year=current_datetime.year)
                items["birthday"] = birthday_date

        for keys, values in items.items():
            if current_datetime > birthday_date:
                birthday_date = birthday_date.replace(year=current_datetime.year + 1)

            delta = birthday_date - current_datetime
            if delta.days < 7:
                if keys == "name":
                    b_day.setdefault(birthday_date.strftime('%A'), []).append(values)
        
    for day, names in b_day.items():
        if day == "Saturday" or day == "Sunday":
              b_day.setdefault("Monday", names).append(names)

    
    b_day.pop("Saturday") 
    b_day.pop("Sunday")
    b_day = {key:value for (key, value) in b_day.items() if value}

    for names in b_day.values():
        for name in names:
            if type(name) != str:
                names.extend(name)
                names.remove(name) 

    for names in b_day.values():
        for name in names:
            if type(name) != str:
                names.extend(name)
                names.remove(name)

    for days, name in b_day.items():
        names = ", ".join(name)
        congratulations = f'{days}: {names}'
        print(congratulations)
    



get_birthdays_per_week()

# get_birthdays_per_week([
# {"name":"Jill","birthday":datetime(day=10, month=11,year = 1999)}, 
# {"name":"Illia","birthday":datetime(day=7, month=11,year = 1999)}, 
# {"name":"Jullia","birthday":datetime(day=30,month=12,year = 1999)}, 
# {"name":"Ivan","birthday":datetime(day=6,month=11,year = 1999)}, 
# {"name":"Jeka","birthday":datetime(day=6,month=11,year = 1999)},
# {"name":"Jack","birthday":datetime(day=6,month=11,year = 1999)}, 
# {"name":"Jisus","birthday":datetime(day=14,month=11,year = 1999)}, 
# {"name":"Hulio","birthday":datetime(day=11,month=11,year = 1999)}
# ] 
# ) 
  