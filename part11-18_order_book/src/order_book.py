# Write your solution here:
import itertools
from unittest import result

class Task:
    newid = itertools.count(1)
    def __init__(self, description, programmer, workload) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = next(self.newid)
    
    def __str__(self) -> str:
        if self.finished == False:
            task_status = "NOT FINISHED"
        else:
            task_status = "FINISHED"
        return (f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {task_status}")
    
    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True

class OrderBook:

    def __init__(self) -> None:
        self.tasks = []
    def add_order(self, description, programmer, workload):
        self.tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.tasks

    def programmers(self):
        result = []
        for item in self.tasks:
            result.append(item.programmer)
        return list(set(result))
    
    def mark_finished(self, id: int):
        ids = []
        for task in self.tasks:
            ids.append(task.id)
            if task.id == id:
                task.mark_finished()
        if id not in ids:
            raise ValueError("ID is not found")

    def finished_orders(self):
        result = []
        for task in self.tasks:
            if task.finished == True:
                result.append(task)
        return result

    def unfinished_orders(self):
        result = []
        for task in self.tasks:
            if task.finished == False:
                result.append(task)
        return result

    def status_of_programmer(self, programmer: str):
        programmer_tasks = []
        for task in self.tasks:
            if task.programmer == programmer:
                programmer_tasks.append(task)
        finished_tasks = 0
        finished_hours = 0
        unfinished_tasks = 0
        unfinished_hours = 0
        if len(programmer_tasks) == 0:
            raise ValueError("No such programmer") 
        for item in programmer_tasks:
            if item.finished == True:
                finished_tasks += 1
                finished_hours += item.workload
            else:
                unfinished_tasks += 1
                unfinished_hours += item.workload
        return finished_tasks, unfinished_tasks, finished_hours, unfinished_hours
        

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)