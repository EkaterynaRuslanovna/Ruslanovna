from datetime import datetime
import re

# 3. Написать три класса:
#
# 3.1 класс Справочник(Записная книга, Телефонная книга), описывающий взаимодействие с телефонным справочником.
# Объект этого класса агрегирует в себе объекты другого класса - Запись(множество записей)
#
# 3.2 класс Запись(Абонент), хранящий такие данные:
# Имя, Фамилия(необязательно), Телефон, Дата рождения(необязательно).
# Обеспечить валидацию данных и запрет на изменение этих данных другим классом
#
# 3.3 класс Интерфейс, который обеспечивает взаимодействие с пользователем, который вводит данные в терминал.
# Обеспечить защиту от неверного ввода
#
# 3.4 В функции __main__() написать точку входа и выхода их программы(для ввода пользователя).
#
# Данная программа должна обеспечить: добавление, удаление, редактирование записей с терминала.
# По умолчание в справочнике есть номера экстренных служб,
# которые нельзя удалить или изменить(ни юзеру, ни другому программисту).


class Record:
    def __init__(self, name: str, mobile_phone: str, surname: str = None, birthday: str = None):
        self.validate_name(name)
        self.validate_surname(surname)
        self.validate_mobile_phone(mobile_phone)
        self.validate_birthday(birthday)
        self.__name = name
        self.__mobile_phone = mobile_phone
        self.__surname = surname
        self.__birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.validate_name(name)
        self.__name = name

    @staticmethod
    def validate_name(name=None):
        if name:
            if name == "Пожарна служба" or name == "Поліція" or name == "Швидка допомога" or name == "Газова служба":
                return name
            if not re.match(r'^[A-Za-zА-Яа-яїєҐґ][А-Яа-яїєҐґA-Za-z- ]*$', name):
                raise ValueError(f"Імʼя може містити лише букви, пробіл та дефіс. Ви ввели {name}")
            return name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.validate_surname(surname)
        self.__surname = surname

    @staticmethod
    def validate_surname(surname=None):
        if surname:
            if not re.match(r'^[A-Za-zА-Яа-яїєҐґ][А-Яа-яїєҐґA-Za-z- ]*$', surname):
                raise ValueError(f"Фамілія може містити лише букви, пробіл та дефіс. Ви ввели {surname}")
            return surname

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone: str):
        self.validate_mobile_phone(mobile_phone)
        if mobile_phone != "101" or mobile_phone != "102" or mobile_phone != "103" or mobile_phone != "104":
            self.__mobile_phone = mobile_phone
        else:
            raise Exception("Екстренні контакти не дозволено редагувати!")

    @staticmethod
    def validate_mobile_phone(mobile_phone=None):
        if mobile_phone:
            if not mobile_phone.isdigit():
                raise ValueError(f"Телефон має містити лише цифри, ви ввели {mobile_phone}")
            if mobile_phone == "101" or mobile_phone == "102" or mobile_phone == "103" or mobile_phone == "104":
                return mobile_phone
            if len(mobile_phone) != 10:
                raise ValueError(f"Телефон має містити 10 цифр, ви ввели {len(mobile_phone)}")
            return mobile_phone

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: str):
        if birthday is None:
            self.__birthday = None
            return
        self.validate_birthday(birthday)
        self.__birthday = birthday

    @staticmethod
    def validate_birthday(birthday=None):
        if birthday:
            try:
                birthday_datetime = datetime.strptime(birthday, '%d.%m.%y')
                now = datetime.now()
                if birthday_datetime > now:
                    raise ValueError(f"День народження не може бути в майбутньому, ви ввели {birthday}")
                return birthday_datetime
            except ValueError:
                raise ValueError("Невірний формат. Введіть дату в форматі DD.MM.YY")
