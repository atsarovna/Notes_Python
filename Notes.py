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
        print()

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
            print()
    return notes

# функция создания новой заметки и добавления ее в список
def create_note(notes, title, body):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(len(notes) + 1, title, body, timestamp)
        notes.append(new_note)
        save_notes(notes)
        print("Заметка успешно создана.")
        print()
    except Exception as e:
        print(f"Ошибка при создании заметки: {e}")
        print()

# функция редактирования существующей заметки по ее ID 
def edit_note(notes, note_id, title, body):
    try:
        for note in notes:
            if note.id == note_id:
                note.title = title
                note.body = body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_notes(notes)
                print("Заметка успешно отредактирована и сохранена.")
                print()
                return
        print("Заметка с указанным ID не найдена.")
        print()
    except Exception as e:
        print(f"Ошибка при редактировании заметки: {e}")
        print()

# функция удаления заметки по ее ID
def delete_note(notes, note_id):
    try:
        notes = [note for note in notes if note.id != note_id]
        save_notes(notes)
        print("Заметка успешно удалена. Чтобы отобразить список без удаленной заметки, необходимо перезапустить программу.")
        print()
    except Exception as e:
        print(f"Ошибка удаления заметки: {e}")
        print()

# функция фильтра заметок по дате создания
def filter_notes_by_date(notes, target_date):
    try:
        # Проверяем, что введенное значение является корректной датой
        datetime.strptime(target_date, "%Y-%m-%d")
        # Фильтруем заметки по дате
        filtered_notes = [note for note in notes if note.timestamp.startswith(target_date)]
        return filtered_notes
    except ValueError:
        print("Ошибка: Введенная дата имеет некорректный формат (ожидается год-месяц-день).")
        print()
        return []

# функция вывода заметки по ID
def view_note_by_id(notes, note_id):
    for note in notes:
        if note.id == note_id:
            print(f"{note.id}: {note.title} ({note.timestamp})")
            print(note.body)
            print()
            return
    print("Заметка с указанным ID не найдена.")
    print()

# выводит список всех заметок
def list_notes(notes):
    if not notes:
        print("Список заметок пуст.")
        print()
    else:
        for note in notes:
            print(f"ID {note.id}: {note.title} ({note.timestamp})")
            print(note.body)
            print()

if __name__ == "__main__":
    notes = load_notes()

    while True:
        print("1. Создать заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Отфильтровать заметки по дате")
        print("5. Найти заметку по ID")
        print("6. Показать список заметок")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            create_note(notes, title, body)
        elif choice == "2":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Новый заголовок: ")
            body = input("Новое тело заметки: ")
            edit_note(notes, note_id, title, body)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(notes, note_id)
        elif choice == "4":
            target_date = input("Введите дату (год-месяц-день) для выборки заметок: ")
            filtered_notes = filter_notes_by_date(notes, target_date)
            list_notes(filtered_notes)
        elif choice == "5":
            note_id = int(input("Введите ID заметки для просмотра: "))
            view_note_by_id(notes, note_id)
        elif choice == "6":
            list_notes(notes)
        elif choice == "7":
            break
        else:
            print("Некорректная команда")
