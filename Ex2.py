from sys import argv

task = []
exit_status = 0

def insert(st):
    task.append(st)

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
        print("Insert name: ")
        name = input()
        if name not in task:
            print("Not found")
        else:
            task.remove(name)

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
