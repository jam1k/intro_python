# Write your solution here

# If you use the classes made in the previous exercise, copy them here
class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.tasks = []
 
    def add_order(self, description, programmer, workload):
        self.tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.tasks]))
 
    def mark_finished(self, id: int):
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        #raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)

print("commands:")
print("0 exit")
print("1 add order")
print("2 list finished tasks")
print("3 list unfinished tasks")
print("4 mark task as finished")
print("5 programmers")
print("6 status of programmer")
orders = OrderBook()
while True:
    command = input("command: ")
    
    try:
        command = int(command)
    except:
        print("erroneous input")
    if command == 0:
        break
    elif command == 1:
        description = input("description: ")
        input_str = input("programmer and workload estimate: ")
        try:
            programmer, workload = input_str.split(" ")
        except ValueError:
            programmer = ""
            workload = -1
        try:
            workload = int(workload)
        except ValueError:
            workload = -1
        if workload == -1:
            print("erroneous input")
        else:
            orders.add_order(description, programmer, workload)
            print("added!")
    elif command == 2:
        finished = orders.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)
    elif command == 3:
        unfinished = orders.unfinished_orders()
        if len(unfinished) == 0:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                    print(task)
    elif command ==  4:
        id = input("id: ")
        try:
            id = int(id)
        except ValueError:
            id = -1
        unfinished = orders.unfinished_orders()
        for task in unfinished:
            if task.id == id:
                break
            else:
                id = -1
        if id == -1:
            print("erroneous input")
        else:
            orders.mark_finished(id)
            print("marked as finished")

    
    elif command == 5:
        programmers = orders.programmers()
        for person in programmers:
            print(person)
    elif command == 6:
        programmer = input("programmer: ")
        programmers = orders.programmers()
        if programmer not in programmers:
            print("erroneous input")
        else:
            fin, notfin, hours_done, hours_scheduled = orders.status_of_programmer(programmer)
            print(f"tasks: finished {fin} not finished {notfin}, hours: done {hours_done} scheduled {hours_scheduled}")
    
    else:
        print ("erroneous input")