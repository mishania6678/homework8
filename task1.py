import time


class Date:
    date = ''

    def __init__(self, date):
        Date.date = date

    @classmethod
    def split_date(cls) -> None:
        """Useless method"""
        try:
            cls.day, cls.month, cls.year = tuple(map(int, cls.date.split('-')))
            print(f'День: {cls.day}, месяц: {cls.month}, год: {cls.year}')
        except Exception:
            print(f'Неправильный формат входных данных ({Date.date})')

    @staticmethod
    def check_date() -> None:
        try:
            time.strptime(Date.date, '%d-%m-%Y')
            print(f'С датой {Date.date} все хорошо')
        except Exception:
            print(f'Даты {Date.date} не существует')


date1 = Date('30-11-2007')
date1.split_date()
date1.check_date()

print()

date2 = Date('31-11-2007')
date2.split_date()
date2.check_date()

print()

date3 = Date('15-03-kakoj-to bred')
date3.split_date()
date3.check_date()
