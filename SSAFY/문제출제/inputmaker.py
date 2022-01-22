import random
DAY = range(1,100)
hmd = range(21,80)


for db in range(10):
    pick_day = random.choice(DAY)
    pick_hmd = random.choice(hmd)
    Max = range(20, pick_hmd)
    pick_Max = random.choice(Max)
    day_hmd = range(pick_hmd-pick_Max,pick_hmd)
    pick_day_hmdlist = []
    for i in range(pick_day):
        pick_day_hmdlist.append(random.choice(day_hmd))

    print(db+1)
    print(pick_day, pick_Max, pick_hmd)
    for i in range(len(pick_day_hmdlist)):
        print((pick_day_hmdlist[i]))
