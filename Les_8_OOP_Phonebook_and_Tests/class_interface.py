"""

3.3 класс Интерфейс, который обеспечивает взаимодействие с пользователем, который вводит данные в терминал.
Обеспечить защиту от неверного ввода

3.4 В функции __main__() написать точку входа и выхода их программы(для ввода пользователя).

Данная программа должна обеспечить: добавление, удаление, редактирование записей с терминала.
По умолчание в справочнике есть номера экстренных служб,
которые нельзя удалить или изменить(ни юзеру, ни другому программисту).

"""
from class_phoneBook import Phonebook
from class_record import Record


class Interface:
    def __init__(self, phonebook: Phonebook):
        self.phonebook = phonebook

    def run(self):
        print('Вітаємо! В нас знайдеться все:)')
        while True:
            try:
                command = input('Оберіть опцію (1 - додати контакт, 2 - змінити контакт, 3 - знайти контакт, 4 - показати всі контакти, 5 - видалити контакт, 6 - вихід): ')
                if command == "1":
                    self.add_record()
                elif command == "2":
                    self.update_data()
                elif command == "3":
                    self.find_record()
                elif command == "4":
                    self.phonebook.view_all_records()
                elif command == "5":
                    self.delete_contact()
                elif command == "6":
                    print("Дякуємо, що обрали нас! До зустрічі:)")
                    break
                else:
                    print('Немає такої опції. Попробуйте знову.')
            except Exception as error:
                print(error)

    def add_record(self):
        name = input('Введіть імʼя: ')
        while not name:
            print('Імʼя є обовʼязковим.')
            name = input('Введіть імʼя: ')
        mobile_phone = input('Введіть мобільний номер телефону: ')
        if self.phonebook.find_record_by_mobile_phone(mobile_phone):
            raise Exception('Запис з таким номером вже існує.')
        while not mobile_phone:
            print('Мобільний номер телефону є обовʼязковим.')
            mobile_phone = input('Введіть мобільний номер телефону: ')
        surname = input('Введіть прізвище (необовʼязково): ')
        birthday = input('Введіть дату народження (необовʼязково в форматі ДД.ММ.ГГ): ')
        record = Record(name, mobile_phone, surname, birthday)
        self.phonebook.add_record(record)
        print('Дані успішно додані в довідник.')

    def find_record(self):
        try:
            command = input('Введіть варіант, по якому хочете знайти запис (1 - name, 2 - surname, 3 - mobile_phone, 4 - birthday): ')
            if command == "1":
                name = input('Введіть імʼя: ')
                records = self.phonebook.find_record_by_name(name)
                self.show_founded(records)
                return records
            elif command == "2":
                surname = input('Введіть прізвище: ')
                records = self.phonebook.find_record_by_surname(surname)
                self.show_founded(records)
                return records
            elif command == "3":
                mobile_phone = input('Введіть мобільний номер телефону: ')
                record = self.phonebook.find_record_by_mobile_phone(mobile_phone)
                self.show_founded(record)
                return record
            elif command == "4":
                birthday = input('Введіть дату народження в форматі ДД.ММ.ГГ: ')
                records = self.phonebook.find_record_by_birthday(birthday)
                self.show_founded(records)
                return records
            else:
                print('Немає такої опції. Попробуйте знову.')
        except Exception as error:
            print(error)

    def update_data(self):
        try:
            mobile_phone = input('Введіть мобільний номер телефону: ')
            if 101 <= int(mobile_phone) <= 104:
                raise Exception("Екстренні контакти не дозволено редагувати!")
            command = input('Введіть, які дані ви хочете оновити (1 - name, 2 - surname, 3 - mobile_phone, 4 - birthday): ')
            if command == "1":
                new_name = input('Введіть імʼя, на яке хочете змінити: ')
                return self.phonebook.update_record(mobile_phone=mobile_phone, new_name=new_name)
            elif command == "2":
                new_surname = input('Введіть прізвище, на яке хочете змінити: ')
                return self.phonebook.update_record(mobile_phone=mobile_phone, new_surname=new_surname)
            elif command == "3":
                new_mobile_phone = input('Введіть мобільний номер телефону, на який хочете змінити: ')
                return self.phonebook.update_record(mobile_phone=mobile_phone, new_mobile_phone=new_mobile_phone)
            elif command == "4":
                new_birthday = input('Введіть дату народження в форматі ДД.ММ.ГГ, на яке хочете змінити: ')
                return self.phonebook.update_record(mobile_phone=mobile_phone, new_birthday=new_birthday)
            else:
                print('Немає такої опції. Попробуйте знову.')
        except Exception as error:
            print(error)

    def delete_contact(self):
        try:
            mobile_phone = input('Введіть мобільний номер телефону, який хочете видалити: ')
            if mobile_phone:
                self.phonebook.delete_record(mobile_phone)
            print("Контакт видалено.")
        except Exception as error:
            print(error)

    @staticmethod
    def show_founded(records):
        for record in records:
            print(
                f"Імʼя: {record.name}, Прізвище: {record.surname}, Номер телефону: {record.mobile_phone}, Дата народження: {record.birthday}")
