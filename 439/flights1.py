



sampleList = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]  #['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'

splitListOrigin = []

startingPort = 'YUL'

iternerary = [startingPort]

for pair in sampleList:

    #get all the origins for easy searching
    splitListOrigin.append(pair[0])

def findFirst(criteria):
    i = 0
    if criteria not in splitListOrigin:
        return None
    else:
        retArray = []
        for origin in splitListOrigin:
            if origin == criteria:

                #store the index value for easy editing
               return [sampleList[i],i]
            i += 1

currentPort = findFirst(startingPort)

#check to see port actually exists
if currentPort == None:
    iternerary = None
else:

    #loop until there isn't a origin-dest overlap
    while currentPort != None:
        iternerary.append(currentPort[0][1])

        #effectively removes the port, skips around out of bounds errors that can occur in findFirst due to array size
        sampleList[currentPort[1]] = ('',currentPort[0][1])

        currentPort = findFirst(currentPort[0][1])

print(iternerary)