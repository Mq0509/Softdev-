import random
krewes = { 2: ["Loser Fang", "b", "c"], 7: ["May", "Bri", "Gitae"], 8: ["Jeff", "bd", "cd"]}
period = list(krewes.keys())
lenp = len(period)
randp = random.randint(0,lenp-1)
devos = list(krewes.get(period[randp]))
lend = len(devos)
randd = random.randint(0,lend-1)
print(devos[randd])
