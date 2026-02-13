import re


print("\nВітаю, я ваш бот-помічник для керування контактами\n")


def show_menu():  # Функція для показу меню користувачу
    print("\n1 - Додайте контакт")
    print("2 - Змініть контакт")
    print("3 - Видаліть контакт")
    print("4 - Показати номер контакту")
    print("5 - Показати всі контакти")
    print("6 - Вихід")


# Функція для уніфікації номера телефону
def uniform_number(phone_number: str) -> str:
    phone_number = phone_number.strip()
    phone_number = re.sub(r"[^0-9+]", "", phone_number)

    if phone_number.startswith("+380"):
        normalized = phone_number
    elif phone_number.startswith("380"):
        normalized = "+" + phone_number
    elif phone_number.startswith("0"):
        normalized = "+38" + phone_number
    else:
        return None

    if re.fullmatch(r"\+380\d{9}", normalized):
        return normalized
    return None


def load_contacts() -> dict:  # Функція для завантаження контактів з файлу
    contacts = {}
    try:
        with open("contacts.txt", "r", encoding="utf-8") as contact:
            for line in contact:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        print("Файл 'contacts.txt' не знайдено.")
    return contacts


def save_contacts(contacts: dict):  # Функція для збереження контактів у файл
    with open("contacts.txt", "w", encoding="utf-8") as contact:
        for name, phone in contacts.items():
            contact.write(f"{name},{phone}\n")


if __name__ == "__main__":
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("\nВиберіть дію (1-6): ")

        if choice == "1":
            name = input("\nВведіть імʼя контакту >>> ")
            phone = input("Введіть номер телефону контакту >>> ")
            phone = uniform_number(phone)

            if not phone:
                print("Невірний формат номеру, повинен бути в форматі +380XXXXXXXXX")
                continue

            contacts[name] = phone
            save_contacts(contacts)
            print(f"Контакт {name} {phone} додано")

        elif choice == "2":
            name = input("\nВведіть імʼя для зміни контакту >>> ")
            if name not in contacts:
                print("\nКонтакту не знайдено")

            new_phone = input("\nВведіть новий номер телефону >>> ")
            new_phone = uniform_number(new_phone)

            if not new_phone:
                print("\nНевірний формат номеру, повинен бути в форматі +380XXXXXXXXX")
                continue

            contacts[name] = new_phone
            save_contacts(contacts)
            print(f"\nВ контакта {name} змінено номер на {new_phone}")

        elif choice == "3":
            name = input("\nВведі імʼя контакту для видалення >>> ")
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print(f"\nКонтакт {name} видалено.")
            else:
                print("\nКонтакт не знайдено")

        elif choice == "4":
            name = input("\nВведіть ім'я контакту для показу номера: ")
            if name in contacts:
                print(f"\nНомер контакту {name}: {contacts[name]}")
            else:
                print("\nКонтакт не знайдено.")

        elif choice == "5":
            if contacts:
                print("\nСписок контактів:")
                for name, phone in contacts.items():
                    print(f"\n{name}: {phone}")
            else:
                print("\nКонтакти відсутні.")

        elif choice == "6":
            print("\nДо побачення!\n")
            break

        else:
            print("\nНевірний вибір. Введіть число від 1 до 6.")
