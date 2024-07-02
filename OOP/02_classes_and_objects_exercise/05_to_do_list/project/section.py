from typing import List
from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task_: Task) -> str:
        if task_ in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(task_)

        return f"Task {task_.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        curr_task = next((t for t in self.tasks if t.name == task_name), None)

        if curr_task not in self.tasks:
            return f"Could not find task with the name {task_name}"

        curr_task.completed = True

        return f"Completed task {curr_task.name}"

    def clean_section(self) -> str:
        counter = 0

        for task_ in self.tasks:
            if task_.completed:
                self.tasks.remove(task_)
                counter += 1

        return f"Cleared {counter} tasks."

    def view_section(self) -> str:
        result = '\n'.join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n" \
               f"{result}"
