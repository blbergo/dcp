sampleList =  [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 

startingPort = 'A'

startingPorts = []

itenerary = []

i = 0

#origin tracing
def recurssiveSearch(currentPair):

    #remove current pair from list to prevent infinite loop
    sampleList[currentPair[1]] = [[],None]

    j = 0

    #end of recurssion variable
    end = True

    #cycle through the list
    for pair in sampleList:
        if pair[0] == currentPair[0][1]:
            itenerary.append(pair[0][0])
            currentPair = [pair,j]
            end = False
            recurssiveSearch(currentPair)

        j += 1

    #prevent duplicates 
    if end and itenerary[-1] != currentPair[0][1]:
        itenerary.append(currentPair[0][1])
        

#find starting points
for pair in sampleList:
    if pair[0] == startingPort:
        startingPorts.append([pair, i])
    i += 1
       

if startingPorts == []:
    itenerary = None
else:
    itenerary.append(startingPort)
    for pair in startingPorts:
        recurssiveSearch(pair)


print(itenerary)