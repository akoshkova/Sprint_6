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