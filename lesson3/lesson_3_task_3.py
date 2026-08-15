from address import Address
from mailing import Mailing

adr_from = Address("159357", "Москва", "Солнечная", "18", "9")

adr_to = Address("789456", "Краснодар", "Красная", "85", "50")

mail = Mailing(
    to_address=adr_to,
    from_address=adr_from,
    cost=570,
    track="TRACK7895641"
)

print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
