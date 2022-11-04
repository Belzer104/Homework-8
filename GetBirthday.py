from datetime import datetime

def get_birthdays_per_week(li):
    l = list()
    for item in li:
        
        for key, value in item.items():
            birthday_date = datetime.strptime(value, '%d.%m')
            current_date = datetime.now()

            birthday_date = birthday_date.replace(year=current_date.year)
            if current_date > birthday_date:
                birthday_date = birthday_date.replace(year=current_date.year + 1)
            delta = birthday_date - current_date
            if delta.days <= 7:
                l.append(f"{birthday_date.strftime('%A')}: {item[0]}")
    return l
            
            

print(get_birthdays_per_week([{"Jill": "07.11"}, {"Illia":"07.11"}, {"Jullia":"30.11"}, {"Ivan":"12.11"},{"Jeka":"30.10"},{"Jack":"08.11"}, {"Jisus":"09.11"}, {"Hulio":"11.11"}]))
    