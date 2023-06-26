from datetime import date


class Field:
    def __init__(self, value=None):
        self.__value = value

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__value == other

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self.__value = new_value

    def validate(self, value):
        pass


class Phone(Field):
    def validate(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Phone number must be a string")

        if value is not None and not value.isdigit():
            print("Warning: Invalid phone number. Only digits are allowed.")
            self.value = None


class Birthday(Field):
    def validate(self, value):
        if value is not None and not isinstance(value, date):
            raise ValueError("Birthday must be a date object")

        if value is not None and value > date.today():
            raise ValueError("Birthday cannot be in the future")


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value is None:
            return None

        today = date.today()
        next_birthday = date(
            today.year, self.birthday.value.month, self.birthday.value.day
        )

        if today > next_birthday:
            next_birthday = date(
                today.year + 1, self.birthday.value.month, self.birthday.value.day
            )

        days_left = next_birthday - today
        return days_left.days


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        self.records.remove(record)

    def iterator(self, page_size=10):
        total_records = len(self.records)
        num_pages = (total_records + page_size - 1) // page_size

        for page in range(num_pages):
            start_index = page * page_size
            end_index = min((page + 1) * page_size, total_records)
            yield self.records[start_index:end_index]


if __name__ == "__main__":
    phone = Phone("s")
    print(
        phone.value
    )  # Виводиться None, а також виводиться попередження про неправильний номер телефону
