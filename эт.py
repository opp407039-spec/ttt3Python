class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.done = False

    def __str__(self):
        status = "виконано" if self.done else "не виконано"
        return f"{self.title} | {self.description} | дедлайн: {self.deadline} | {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return
        print("Завдання не знайдено")

    def mark_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.done = True
                return
        print("Завдання не знайдено")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній")
        for number, task in enumerate(self.tasks, 1):
            print(f"{number}. {task}")


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task(Task("Домашнє завдання", "Зробити ДЗ з Python", "25.11.2026"))
    manager.add_task(Task("Спорт", "Піти в зал", "26.11.2026"))
    manager.mark_done("Спорт")
    manager.show_tasks()
    manager.remove_task("Спорт")
    manager.show_tasks()