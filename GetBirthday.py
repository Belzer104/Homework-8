from datetime import datetime

def get_birthdays_per_week(li):
    d = dict()
    for item in li:
        
        for key, value in item.items():
            birthday_date = datetime.strptime(value, '%d.%m')
            current_date = datetime.now()

            birthday_date = birthday_date.replace(year=current_date.year)
            if current_date > birthday_date:
                birthday_date = birthday_date.replace(year=current_date.year + 1)
            delta = birthday_date - current_date
            if delta.days <= 7:
               d.setdefault(birthday_date.strftime('%A'),[]).append(key)
    for k, v in d.items():
        name = ", ".join(v)
        print(f"{k}: {name}")
            
            

get_birthdays_per_week([{"Jill": "07.11"}, {"Illia":"07.11"}, {"Jullia":"30.11"}, {"Ivan":"12.11"},{"Jeka":"30.10"},{"Jack":"08.11"}, {"Jisus":"09.11"}, {"Hulio":"11.11"}])
  