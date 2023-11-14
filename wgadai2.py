import random

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def get_guess():
    # Функція для отримання введення користувача та перетворення на нижній регістр
    guess = input("Вгадайте букву: ")
    return guess.lower()

def check_guess(guess, letter):
    # Перевірка введеного значення на коректність та порівняння з випадковою буквою
    if len(guess) != 1:
        return False, "Ви ввели не одну букву!"
    elif guess not in ALPHABET:
        return False, "Будь ласка, введіть літеру з латинського алфавіту!"
    elif guess == letter:
        return True, f"Вгадали! Буква була {letter}"
    else:
        return False, f"Не вгадали! Буква була {letter}"

def main():
    letter = random.choice(ALPHABET)

    while True:
        guess = get_guess()  # Отримання введеної користувачем літери
        correct, message = check_guess(guess, letter)  # Перевірка введеної літери
        print(message)  # Вивід повідомлення про результат відповіді
        if correct:
            break

if __name__ == "__main__":
    main()
