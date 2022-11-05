from datetime import datetime

def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    print(current_datetime)
    for items in users:
        for keys, values in items.items():
            if keys == "birthday":
                birthday_date = values.replace(year=current_datetime.year)
                items["birthday"] = birthday_date
        print(items)





        
get_birthdays_per_week([
{"name":"Jill","birthday":datetime(day=10, month=11,year = 1999)}, 
{"name":"Illia","birthday":datetime(day=7, month=11,year = 1999)}, 
{"name":"Jullia","birthday":datetime(day=30,month=12,year = 1999)}, 
{"name":"Ivan","birthday":datetime(day=13,month=11,year = 1999)}, 
{"name":"Jeka","birthday":datetime(day=5,month=11,year = 1999)},
{"name":"Jack","birthday":datetime(day=9,month=11,year = 1999)}, 
{"name":"Jisus","birthday":datetime(day=14,month=11,year = 1999)}, 
{"name":"Hulio","birthday":datetime(day=11,month=11,year = 1999)}
]
) 
  