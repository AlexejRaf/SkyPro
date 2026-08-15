from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 17 Pro Max", "+79165448765"))
catalog.append(Smartphone("Samsung", "Galaxy S25 Ultra", "+79794980026"))
catalog.append(Smartphone("Huawei", "Pura 80 Ultra", "+79881569928"))
catalog.append(Smartphone("Xiaomi", "15", "+79185479116"))
catalog.append(Smartphone("Realme", "GT 8 Pro", "+79889461313"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.subscriber_number}")
