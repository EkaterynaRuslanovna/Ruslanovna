from Task_3_Class_Record import Record


class Phonebook:
    def __init__(self):
        self.__phonebook = {"101": Record(name="Пожарна служба", mobile_phone="101"), "102": Record(name="Поліція", mobile_phone="102"),
                            "103": Record(name="Швидка допомога", mobile_phone="103"), "104": Record(name="Газова служба", mobile_phone="104")}

    """Методи знаходження запису по імені, фамілії, номеру телефона, даті народження"""

    def find_record_by_name(self, name: str):
        record_lst = []
        for record in self.__phonebook.values():
            if record.name == name:
                record_lst.append(record)
        if len(record_lst) == 0:
            raise Exception(f"Запису з імʼям {name} не знайдено.")
        return record_lst

    def find_record_by_surname(self, surname: str):
        record_lst = []
        for record in self.__phonebook.values():
            if record.surname == surname:
                record_lst.append(record)
        if len(record_lst) == 0:
            raise Exception(f"Запису з фамілією {surname} не знайдено.")
        return record_lst

    def find_record_by_mobile_phone(self, mobile_phone: str):
        for record in self.__phonebook.values():
            if record.mobile_phone == mobile_phone:
                return record
        raise Exception(f"Запису з мобільним номером {mobile_phone} не знайдено.")

    def find_record_by_birthday(self, birthday: str):
        record_lst = []
        for record in self.__phonebook.values():
            if record.birthday == birthday:
                record_lst.append(record)
        if len(record_lst) == 0:
            raise Exception(f"Запису з датою народження {birthday} не знайдено.")
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
            if record.name == "Пожарна служба" or record.name == "Поліція" or record.name == "Швидка допомога" or record.name == "Газова служба":
                raise Exception("Екстренні контакти не дозволено редагувати!")
            else:
                record.name = new_name
                return record
        if new_surname:
            record.surname = new_surname
            return record
        if new_mobile_phone:
            if record.mobile_phone == "101" or record.mobile_phone == "102" or record.mobile_phone == "103" or record.mobile_phone == "104":
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
            if mobile_phone == "101" or mobile_phone == "102" or mobile_phone == "103" or mobile_phone == "104":
                raise Exception("Екстренні контакти не дозволено видаляти!")
            return self.__phonebook.pop(mobile_phone)

    def view_all_records(self):
        for record in self.__phonebook.values():
            print(
                f"Name: {record.name}, Surname: {record.surname}, Mobile Phone: {record.mobile_phone}, Birthday: {record.birthday}")
