# To - Do list
import sys
print("         ....TO - DO LIST APPLICATION....")
tasks=[]
completed_tasks=[]
priority_tasks=[]
while(True):
    print("------------------ Options -------------------------")
    print("1.Add a task")
    print("2.Update a task")
    print("3.Mark as complete")
    print("4.Delete the task")
    print("5.View the TO-DO List")
    print("6.View completed tasks")
    print("7.Exit")
    try:
        ch = int(input("Enter your choice(1-7)>>> "))
    except:
        print("Enter only integer values ranging from 1 to 6 :)")
    if ch==1:
        task=input("Enter the task>>> ")
        tasks.append(task)
    elif ch==2:
        task=input("Enter the task that u want to update it>>> ")
        if task in tasks:
            new_task=input("Enter the new task>>> ")
            for i in range(len(tasks)):
                if tasks[i] == task:
                    tasks[i]=new_task
                    break
                print("Task updated successfully...")

        else:
            print("Enter the task from the list:",tasks)
    elif ch==3:
        task=input("Enter the task that u want to mark as completed>>> ")
        if task in tasks:
            print(f"{task} task is completed successfully it will be deleted afterwards")
            tasks.remove(task)
            completed_tasks.append(task)
        else:
            print("Enter the task from the list:",tasks)
    elif ch==4:
        task=input("Enter the task that u want to  be deleted>>> ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Enter the task from the list:",tasks)
    elif ch==5:
        if tasks:
            print("To-DO List as follows>>>")
            for i,task in enumerate(tasks):
                    print(f"{i+1} -> {task}")
        else:
            print("Your TO-DO List is empty....")
    elif ch==6:
        if completed_tasks:
            print("\nCompleted Tasks:")
            for i, task in enumerate(completed_tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks has been marked as completed yet..")
    elif ch==7:
        print("Exiting...")
        sys.exit(0)
    else:
        print("Enter your choice (1-5) renter....")