from task_3_class_record import Record


class Phonebook:
    def __init__(self):
        self.__phonebook = {"101": Record(name="Пожарна служба", mobile_phone="101"), "102": Record(name="Поліція", mobile_phone="102"),
                            "103": Record(name="Швидка допомога", mobile_phone="103"), "104": Record(name="Газова служба", mobile_phone="104")}

    """Методи знаходження запису по імені, фамілії, номеру телефона, даті народження"""

    def find_record_by_name(self, name: str):
        record_lst = []
        for record in self.__phonebook.values():
            if name.lower() in record.name.lower():
                record_lst.append(record)
        return record_lst

    def find_record_by_surname(self, surname: str):
        record_lst = []
        for record in self.__phonebook.values():
            if record.surname:
                if surname.lower() in record.surname.lower():
                    record_lst.append(record)
        return record_lst

    def find_record_by_mobile_phone(self, mobile_phone: str):
        for record in self.__phonebook.values():
            if record.mobile_phone == mobile_phone:
                return record

    def find_record_by_birthday(self, birthday: str):
        record_lst = []
        for record in self.__phonebook.values():
            if record.birthday == birthday:
                record_lst.append(record)
        return record_lst

    """Методи для дій з записом"""

    def add_record(self, record: Record):
        if record.mobile_phone in self.__phonebook:
            print(f'Номер {record.mobile_phone} вже існує в довіднику')
        else:
            self.__phonebook[record.mobile_phone] = record

    def update_record(self, mobile_phone: str, new_name: str = None, new_mobile_phone: str = None, new_surname: str = None, new_birthday: str = None):
        record = self.find_record_by_mobile_phone(mobile_phone)
        if new_name:
            if record.name in ["Пожарна служба", "Поліція", "Швидка допомога", "Газова служба"]:
                raise Exception("Екстренні контакти не дозволено редагувати!")
            else:
                record.name = new_name
                return record
        if new_surname:
            record.surname = new_surname
            return record
        if new_mobile_phone:
            if 101 <= int(record.mobile_phone) <= 104:
                raise Exception("Екстренні контакти не дозволено редагувати!")
            else:
                record.mobile_phone = new_mobile_phone
            return record
        if new_birthday:
            record.birthday = new_birthday
            return record
        else:
            raise Exception(f"Запису не знайдено.")

    def delete_record(self, mobile_phone: str = None):
        if mobile_phone:
            if 101 <= int(mobile_phone) <= 104:
                raise Exception("Екстренні контакти не дозволено видаляти!")
            return self.__phonebook.pop(mobile_phone)

    def view_all_records(self):
        for record in self.__phonebook.values():
            print(
                f"Імʼя: {record.name}, Фамілія: {record.surname}, Номер телефону: {record.mobile_phone}, Дата народження: {record.birthday}")