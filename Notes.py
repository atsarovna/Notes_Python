import json
import os
from datetime import datetime

# класс Note - структура хранения заметок
class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

# функция сохранения списка заметок в формате JSON
def save_notes(notes):
    try:
        with open("notes.json", "w") as file:
            json.dump([note.__dict__ for note in notes], file)
    except Exception as e:
        print(f"Ошибка при сохранении заметки: {e}")

# функция загрузки списка заметок из файла JSON
def load_notes():
    notes = []
    if os.path.exists("notes.json"):
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                for note_data in data:
                    notes.append(Note(**note_data))
        except Exception as e:
            print(f"Ошибка при загрузке заметок {e}")
    return notes

# функция создания новой заметки и добавления ее в список
def create_note(notes, title, body):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(len(notes) + 1, title, body, timestamp)
        notes.append(new_note)
        save_notes(notes)
        print("Заметка успешно создана.")
    except Exception as e:
        print(f"Ошибка при создании заметки: {e}")


# выводит список всех заметок
def list_notes(notes):
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"{note.id}:{note.title} ({note.timestamp})")
            print(note.body)
            print()

if __name__ == "__main__":
    notes = load_notes()

    while True:
        print("1. Создать заметку")
        print("2. Показать список заметок")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            create_note(notes, title, body)
        elif choice == "2":
            list_notes(notes)
            break
        else:
            print("Некорректная команда")
