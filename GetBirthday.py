from datetime import datetime
users = [
    {"name":"Jill","birthday":datetime(day=10, month=11,year = 1999)}, 
    {"name":"Illia","birthday":datetime(day=7, month=11,year = 1999)}, 
    {"name":"Jullia","birthday":datetime(day=30,month=12,year = 1999)}, 
    {"name":"Ivan","birthday":datetime(day=6,month=11,year = 1999)}, 
    {"name":"Jeka","birthday":datetime(day=6,month=11,year = 1999)},
    {"name":"Jack","birthday":datetime(day=12,month=11,year = 1999)}, 
    {"name":"Jisus","birthday":datetime(day=13,month=11,year = 1999)}, 
    {"name":"Hulio","birthday":datetime(day=11,month=11,year = 1999)}
    ] 
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
    # Начинаем итерацию по списку
    
    for user in users:
    # Приравниваем datetime из словарей текущий год 
        birthday_date = datetime(
                year=current_datetime.year,
                month=user.get('birthday').month,
                day=user.get('birthday').day
        )

    # Сравниваем текущий день и ДР
        if current_datetime > birthday_date:
            birthday_date = birthday_date.replace(year=current_datetime.year + 1)

    # Ищем разницу между ДР и текщим днем записываем в переменную delta
        delta = birthday_date - current_datetime
    
    # По услловию должны с текущего дня на последующие 7 дней вывести позравление по дням если такие имеются
        if delta.days < 7:
            for keys, values in user.items():
                if keys == "name":
                    b_day.setdefault(birthday_date.strftime('%A'), []).append(values)
    
    # По условию с субботы и воскресенья должны поздравить в понкдельник, тоесть всех именинников переносим в значение понедельника
    for day, names in b_day.items():
         if day in ('Saturday', 'Sunday'):
            b_day.setdefault("Monday", names).append(names)

    # Очищаем словарь от лишнего и от субботы с воскресеньем
    b_day.pop("Saturday") 
    b_day.pop("Sunday")
    b_day = {key:value for (key, value) in b_day.items() if value}

    # Для красоты вывода переводим все получившиеся списки в нутри списка-значения в строки 
    for names in b_day.values():
        for name in names:
            if not isinstance(name, str):
                names.extend(name)
                names.remove(name) 

    # Повторяем преддыдущий шаг
    for names in b_day.values():
        for name in names:
            if not isinstance(name, str):
                names.extend(name)
                names.remove(name) 

    # Финальные штрихи переводим в словаре значение в строки
    for days, name in b_day.items():
        names = ", ".join(name)
        congratulations = f'{days}: {names}'
        print(congratulations)
if __name__ == "__main__":
    get_birthdays_per_week(users) 
  