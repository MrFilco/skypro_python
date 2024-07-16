from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79167654321"))
catalog.append(Smartphone("Google", "Pixel 6", "+79161239876"))
catalog.append(Smartphone("Xiaomi", "Mi 12", "+79162345678"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79163456789"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
