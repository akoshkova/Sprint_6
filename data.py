class ValidData:
    name = "Иван Петров"
    phone = "+79991234567"
    address = "г. Москва, ул. Ленина, д. 1"

class InvalidData:
    name_too_short = "И"
    name_special_chars = "Иван@Петров"
    phone_invalid = "1234567"
    phone_letters = "abcdefg"
    address_too_short = "ул."

def order_data():
    return [
        {
            "name": "Иван Петров",
            "phone": "+79991234567",
            "address": "г. Москва, ул. Ленина, д. 1",
            "metro_station": "ВДНХ",
            "delivery_date": "завтра",
            "delivery_time": "12:00",
            "comment": "Доставить до двери"
        },
        {
            "name": "Анна Смирнова",
            "phone": "+79997654321",
            "address": "г. Санкт-Петербург, пр. Ленина, д. 2",
            "metro_station": "Технологический институт",
            "delivery_date": "послезавтра",
            "delivery_time": "14:00",
            "comment": "Оставить у двери"
        }
    ]