from datetime import datetime

def get_birthdays_per_week():
    user_input = input('Enter datetime in format dd.mm [-]: ')
    user_entered_date = datetime.strptime(user_input, '%d.%m')
    print(user_entered_date)

    


if __name__ == '__main__':
    get_birthdays_per_week()