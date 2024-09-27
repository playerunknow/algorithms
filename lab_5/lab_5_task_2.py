

class EncodingTable:
    def __init__(self):
        self.encoding = {}
        self.decoding = {}

    def add_encoding(self, char, code):
        """Додає кодування символу."""
        self.encoding[char] = code
        self.decoding[code] = char

    def encode(self, text):
        """Кодує текст, перетворюючи кожен символ у відповідний код."""
        encoded_text = []
        for char in text:
            if char in self.encoding:
                encoded_text.append(self.encoding[char])
            else:
                encoded_text.append(char)  # Залишає символ без змін, якщо кодування не знайдено
        return ''.join(encoded_text)

    def decode(self, encoded_text):
        """Декодує закодований текст, перетворюючи коди назад у символи."""
        decoded_text = []
        code = ''
        for char in encoded_text:
            code += char
            if code in self.decoding:
                decoded_text.append(self.decoding[code])
                code = ''  # Скидаємо код, коли він успішно декодований
        return ''.join(decoded_text)

# Приклад використання
if __name__ == "__main__":
    table = EncodingTable()

    # Додаємо кодування
    table.add_encoding('A', '01')
    table.add_encoding('B', '10')
    table.add_encoding('C', '11')

    # Кодуємо текст
    text = "ABCA"
    encoded_text = table.encode(text)
    print(f"Кодований текст: {encoded_text}")

    # Декодуємо текст
    decoded_text = table.decode(encoded_text)
    print(f"Декодований текст: {decoded_text}")
