def get_cats_info(path: str) -> list[dict]:
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                parts = line.split(',')
                if len(parts) != 3:
                    continue  # Skip lines that don't have exactly 3 parts

                cat_id, name, age = parts
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                })
        return cats

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Файл пошкоджено або виникла помилка: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")

    for cat in cats_info:
        print(cat)
