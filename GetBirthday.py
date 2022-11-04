from datetime import datetime

def get_birthdays_per_week(list):
    # user_input = input('Enter datetime in format dd.mm [-]: ')
    for item in list:
        for key, value in item.items():
            user_entered_date = datetime.strptime(value, '%d.%m')
            current_date = datetime.now()
            user_entered_date = user_entered_date.replace(year=current_date.year)
            if current_date > user_entered_date:
                user_entered_date = user_entered_date.replace(year=current_date.year + 1)
            delta = user_entered_date - current_date
            return f'{delta.days} days left'

print(get_birthdays_per_week([{"Jill": "07.11"}, {"Illia":"10.11"}, {"Jullia":"30.11"}, {"Ivan":"12.11"},{"Jeka":"30.10"},{"Jack":"08.11"}, {"Jisus":"09.11"}, {"Hulio":"11.11"}]))
    