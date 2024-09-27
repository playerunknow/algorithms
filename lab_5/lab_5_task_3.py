

def lz77_compress(data):
    compressed = []
    i = 0
    n = len(data)

    while i < n:
        # Ініціалізація параметрів для пошуку
        match = ""
        match_position = 0

        # Вікно для пошуку
        search_start = max(0, i - 255)  # обмежимо пошук 255 символами назад
        search_end = i

        # Пошук найкращого збігу
        for j in range(search_start, search_end):
            k = 0
            # Поки символи збігаються
            while (i + k < n) and (data[j + k] == data[i + k]):
                k += 1
                if (j + k) >= i:  # щоб уникнути посилання на себе
                    break

            # Якщо знайдено кращий збіг
            if k > len(match):
                match = data[j:j + k]
                match_position = j

        # Додати до стисненого результату
        if match:
            # Додамо (позиція, довжина, символ після збігу)
            next_char = data[i + len(match)] if (i + len(match)) < n else ""
            compressed.append((match_position, len(match), next_char))
            i += len(match) + 1  # переходимо до наступного символу
        else:
            compressed.append((0, 0, data[i]))  # не знайдено збігу
            i += 1

    return compressed

# Приклад використання
data = "ABABABABA"
compressed_data = lz77_compress(data)
print('Дані до стиснення:', data)
print("Стиснені дані:", compressed_data)
