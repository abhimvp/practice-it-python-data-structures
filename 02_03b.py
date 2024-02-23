from collections import deque

class Task(object):
    def __init__(self, taskDesc, hasPriority=False):
        self.taskDesc=taskDesc
        self.hasPriority=hasPriority
    #  The __str__ method defines how a Task object should be represented as a human-readable string. 
    # It's crucial for debugging and when you want to print or display a Task object in a meaningful way.
    def __str__(self):
        return "Task : {0}, Priority: {1}".format(self.taskDesc,self.hasPriority)
    #  These special methods (also called "dunder" methods because of the double underscores) 
    # allow you to customize the behavior of your classes in Python.
    
task_queue=deque()

def add_task(task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_tasks():
    for t in task_queue:
        print(t.taskDesc)

def main():
    #add code here
    add_task(Task("Make List"))
    add_task(Task("Make Breakfast"))
    add_task(Task("Respond to emials",True))
    add_task(Task("Go to restroom first",True))
    add_task(Task("Chill out"))
    add_task(Task("Holla Amigo's",True))
    print_tasks()
    myTask = Task("Write report", True)  # Create a task with priority
    print(myTask)  # Output: Task : Write report, Priority: True
    do_task()
    print_tasks()

    # return

if __name__ == "__main__":
    main()