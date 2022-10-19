__author__ = 'Michaela'

shorts = ["vending_machine","laundry","fast_food","dog","microwave","letter","coffee","credit_card","food_back","shower"]
prefix = "/Users/lynchen/Uni/CoLi/BachelorUdS/BachelorArbeit/SearchQueries/TwitterAPI/Python/files/participants/"
event_prefix = "/Users/lynchen/Uni/CoLi/BachelorUdS/BachelorArbeit/SearchQueries/TwitterAPI/Python/files/events/"
participant_suffix = "_sets"
event_suffix = "_events"
event_result_suffix = "_eventlist"
mix_result_suffix ="_mixedlist"



def getParticipantSets(file):
    return eval(open(file).read())

def stringAsList(st):
    return [word for word in st.split()]


def getSetOfEvents(file):
    ret = set()
    with open(file) as f:
        for line in f:
            ret.add(line.strip())
    return ret

#removeUnderscore = lambda x : x.replace("_"," ")
removeUnderscore = lambda x : x.split("_")[-1]
getParticipantSource = lambda x: prefix + x + participant_suffix
getEventSource = lambda x: event_prefix + x + event_suffix
eventResultFile = lambda x: event_prefix + x + event_result_suffix
mixResultFile = lambda x : prefix +x + mix_result_suffix

def makeEventTriples(event):
    events = list(getSetOfEvents(getEventSource(event)))
    ret = []
    for i in range(len(events) -2):
        first = events[i]
        for j in range(i+1, len(events) -1):
            second = events[j]
            for k in range(j+1, len(events)):
                third = events[k]
                ret.append(first + " " + second + " " + third + " " + removeUnderscore(event))
    return ret

def makeMixTriples(event, no_events=2, no_participants = 1, addScenario=True):
    events = list(getSetOfEvents(getEventSource(event)))


    participants = [list(s) for s in getParticipantSets(getParticipantSource(event))]

    if no_events == 1:
        event_tuples = [[a] for event in events]
    if no_events == 2:
        event_tuples = [[a,b] for a in events for b in events if a != b ]
    if no_events == 3:
        event_tuples = [[a,b,c] for a in events for b in events for c in events if a != b and a != c and b != c]

    participant_tuples = []
    if no_participants == 1:
        for s in participants:
            for p in s:
                participant_tuples.append([pS])
    else:
        generateTuplesWithSize(participants, no_participants, participant_tuples)
      #  for i in range(len(participants) - (no_participants -1)):
      #      for j in range(len(participants[i])):
      #        recAddToTuple([],i,j,no_participants,participant_tuples,participants)
    print(participant_tuples)
    print(event_tuples)
    if addScenario:
        mix = lambda a,b: " ".join(a+b) + " " + removeUnderscore(event)
    else:
        mix = lambda a,b: " ".join(a+b)

    return [ mix(a,b) for a in event_tuples for b in participant_tuples]


def generateTuplesWithSize(multiSet, tupleSize, resultList):
    for currentStartSetIndex in range(len(multiset) - tupleSize + 1):
        for startElementIndex in range(len(multiset[currentStartSetIndex])):
            addToTuple(currentStartSetIndex,startElementIndex,list(),tupleSize,multiSet,resultList)

def addToTuple(currentSetIndex, currentElementIndex, currentTuple, tupleSize, multiSet, resultList):
    currentTuple.append(multiSet[currentSetIndex][currentElementIndex])
    if len(currentTuple) == tupleSize:
        resultList.append(currentTuple)
    else:
        tupleElementsLeft = tupleSize - len(currentTuple)
        for nextSet in range(currentSetIndex+1,len(multiSet)-tupleElementsLeft+1):
            for elementIndex in range(len(multiSet[nextSet])):
                addToTuple(nextSet,elementIndex,list(currentTuple),tupleSize,multiSet,resultList)


def recAddToTuple(tuple, setNumber,setPosition,tuplesize,result,multiset):
        tuple.append(multiset[setNumber][setPosition])
        if len(tuple) == tuplesize:
            result.append(tuple)
            return
        for i in range(len(multiset[setNumber+1])):
            recAddToTuple(tuple[:],  setNumber +1,i,tuplesize,result,multiset)


for scenario in shorts:
    #with open(eventResultFile(scenario),'w') as f:
    #    eventtriples = makeEventTriples(scenario)
    #    print(str(eventtriples))
    #    f.write(str(eventtriples))
    with open(mixResultFile(scenario),'w') as f2:
        mixtriples = makeMixTriples(scenario)
        print(str(mixtriples))
        f2.write(str(mixtriples))
    with open(prefix + scenario + "_mix2",'w') as f3:
        mixtriples = makeMixTriples(scenario,addScenario=False)
        print(mixtriples)
        f3.write(str(mixtriples))
    with open(prefix + scenario + "_mix4",'w') as f4:
        mixtriples = makeMixTriples(scenario,2,2,addScenario=True)
        print(mixtriples)
        f4.write(str(mixtriples))
