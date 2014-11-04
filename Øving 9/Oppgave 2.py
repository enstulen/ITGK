__author__ = "Morten Stulen"
cheeses = {
    "cheddar":
        ["A235-4", "A236-1", "A236-2", "A236-3", "A236-5", "C31-1", "C31-2"],
    "mozarella":
        ["Q456-9", "Q456-8", "A234-5", "Q457-1", "Q457-2"],
    "gombost":
        ["ZLAFS55-4", "ZLAFS55-9", "GOMBOS-7", "A236-4"],
    "geitost":
        ["SPAZ-1", "SPAZ-3", "EMACS45-0"],
    "port salut":
        ["B15-1", "B15-2", "B15-3", "B15-4", "B16-1", "B16-2", "B16-4"],
    "camembert":
        ["A243-1", "A234-2", "A234-3", "A234-4", "A235-1", "A235-2", "A235-3"],
    "ridder":
        ["GOMBOS-4", "B16-3"]}
#print(cheeses["port salut"])

cheeseList = list(cheeses.keys())
valueList = list(cheeses.values())

infected = ["A234", "A235", "B13", "B14", "B15", "C31"]

infected_cheese = set()
not_infected_cheese = []

for i in cheeses:
    for j in cheeses[i]:
        for k in infected:
            if k in j:
                infected_cheese.add(i)

for i in cheeses:
    if i not in infected_cheese:
        for j in cheeses[i]:
            #print(i,'  \t',j)
            not_infected_cheese.append([i,j])

print(infected_cheese)
print(not_infected_cheese)


# valueList2 = []
# for i in range(len(valueList)):
#     for j in range(len(valueList[i])):
#         #print(valueList[0][0])
#         valueList[i][j].replace(" -", "")
# print(valueList)
#






# dictlist = []
# dictlist2 = []
# for key, value in cheeses.items():
#     temp = [key, value]
#     dictlist.append(temp)
# print(dictlist)
#
# for i in dictlist:
#     x = str(i)
#     x.strip(" ")
#     dictlist2.append(x)
# print(dictlist2)

# for i in cheeses.values():
#     i = str(i)
#     i.split()
#     i.replace("('", "")
#
#     dictlist2.append(i)
#print(dictlist2)

# for i in range(len(dictlist)):
#     for j in range(len(dictlist[i])):
#
#         print(str(dictlist[i][j]).strip(", "))
#         print(dictlist[i][j])
#         if dictlist[i][j] == "B15-1":
#              print(i)