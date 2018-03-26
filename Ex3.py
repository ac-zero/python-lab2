from sys import argv

task = []
exit_status = 0

def insert(st):
    task.append(st)

def remove(name):
    if name not in task:
        print("Not found")
    else:
        task.remove(name)

def save(n,filename):
    inpt=open(filename, "w")
    for x in n:
        inpt.write(x+"\n")
    inpt.close()

filename = argv[1]
inpt = open(filename)

for line in inpt:
    insert(line.strip())
inpt.close()

while exit_status == 0:
    print("To-do Manager:")
    print("1. Insert new task")
    print("2. Remove task")
    print("3. Show all tasks")
    print("4. Exit")


    choice = int(input())

    if choice == 1:
        print("Insert name: ")
        name = input()
        insert(name)

    elif choice == 2:
        print("1. Remove all tasks that contain a string")
        print("2. Remove task")
        choice = int(input())
        string = input("Insert string:")

        if choice == 1:
            for x in task:
                if string in x:
                    remove(x)
        elif choice == 2:
            remove(string)
        else :
            print("Wrong choice")

    elif choice == 3:
        a = 1
        for x in sorted(task):
            print(str(a) + ")", x)
            a += 1
    elif choice == 4:
        exit_status = 1
        save(task,filename)
    else:
        print("Wrong number!")
