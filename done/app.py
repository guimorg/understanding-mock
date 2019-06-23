from datetime import datetime


def is_it_friday(
    date: str
):
    """
        Takes a date as a str and returns if it is friday or not.
    """
    if not isinstance(date, str):
        raise TypeError("You must provide a str!")
    datetime_date = datetime.strptime(date, '%d-%m-%Y')
    if datetime_date.weekday() == 4:  # Weekday 0-6 where 0 = Monday
        return True
    return False


from datetime import date


def is_today_friday():
    """
        Returns if today is friday or not.
    """
    if date.today().weekday() == 4:  # Weekday 0-6 where 0 = Monday
        return True
    return False
