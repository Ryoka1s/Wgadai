import random
import tkinter as tk

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def get_guess():
    """Отримати введену користувачем літеру."""
    global entry
    guess = entry.get().lower()
    return guess

def check_guess():
    """Перевірити введену користувачем літеру."""
    global letter, entry, result_label
    guess = get_guess()
    if len(guess) != 1:
        result_label.config(text="Введіть лише одну букву!", fg="black", bg="yellow")
    elif guess not in ALPHABET:
        result_label.config(text="Будь ласка, введіть літеру з латинського алфавіту!", fg="black", bg="yellow")
    elif guess == letter:
        result_label.config(text=f"Вгадали! Буква була {letter}", fg="black", bg="green")
    else:
        result_label.config(text=f"Не вгадали! Буква була {letter}", fg="black", bg="orange")

def play_game():
    """Почати нову гру."""
    global letter, entry, result_label
    letter = random.choice(ALPHABET)
    result_label.config(text="", bg="black")
    entry.delete(0, tk.END)

def main():
    """Головна функція для запуску гри."""
    global entry, result_label, letter
    root = tk.Tk()
    root.title("Гра вгадування букви")
    root.geometry("400x200")
    root.configure(bg="black")  # Змінено фон вікна на чорний колір

    letter = random.choice(ALPHABET)

    label = tk.Label(root, text="Вгадайте букву:", fg="black", bg="yellow")  # Змінено колір тексту та фону Label
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    check_button = tk.Button(root, text="Перевірити", command=check_guess)
    check_button.pack()

    result_label = tk.Label(root, text="", fg="black", bg="black")  # Змінено колір тексту та фону Label
    result_label.pack()

    play_game_button = tk.Button(root, text="Грати ще раз", command=play_game)
    play_game_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
