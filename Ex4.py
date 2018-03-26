
task1 = {"todo": "call John for AmI project organization", "urgent": True}
task2 = {"todo": "buy a new mouse", "urgent": True}
task3 = {"todo": "find a present for Angelina’s birthday", "urgent": False}
task4 = {"todo": "organize mega party (last week of April)", "urgent": False}
task5 = {"todo": "book summer holidays", "urgent": False}
task6 = {"todo": "whatsapp Mary for a coffee", "urgent": False}

Dict = {}
Dict["task1"] = task1
Dict["task2"] = task2
Dict["task3"] = task3
Dict["task4"] = task4
Dict["task5"] = task5
Dict["task6"] = task6

NewDict = {}
for x in Dict:
    if Dict[x]["urgent"] == True:
        NewDict[x]=Dict[x]
for x in NewDict:
    print(NewDict[x])