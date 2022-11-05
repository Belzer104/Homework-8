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
            if delta.days < 7:
               d.setdefault(birthday_date.strftime('%A'),[]).append(key)

    for days, names in d.items():
        if days == "Saturday" :
            d.setdefault("Monday", names).append(names)
        

    for names in d.values():
        for name in names:
            if type(name) != str:
                names.extend(name)
                names.remove(name) 
    for names in d.values():
        for name in names:
            if type(name) != str:
                names.extend(name)
                names.remove(name)
         
    print(d)
    # for k, v in d.items():
    #     name = ", ".join(v)
    #     d = f'{k}: {name}'
    #     print(d)