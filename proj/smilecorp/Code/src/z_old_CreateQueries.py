'''
creates search strings and write them in a file
partly uses code from Ms CreateTwitterStrings.py

old version, not used as one strategy is now determined and has additional verb near:x direct object feature
'''
import readMsFiles as M
shorts = M.scenarioShorts()


def createQueries(strat, scen):

  #todo check if file exists, then ask to proceed or break
  a = p = e = 0
  s = False

  for char in strat:
    if char.isalpha():
      if char == 's':
        s = True
      else:
        var = char
    elif char.isdigit():
      if var == 'a':
        a = int(char)
      elif var == 'p':
        p = int(char) 
      elif var == 'e':
        e = int(char)
 
 
    else:
      print(strat)
      print('wrong format:', strat)
      print('right format: [s][a<n>][p<n>][e<n>], <n> is between 0 and 9')

      raise Exception

  #print(a,p,e,s)
  print("Creating queries with " + str(a) + ' anchor events, ' + str(p) + 
        ' participants and ' + str(e) + ' events for ' + scen.replace('_',' ') + 
        ' scenario' + ('.' if not s else ', including the scenario name.'))
  anchEvents = []
  #participants = set()
  #events = set()

  if a:
    anchEvents = M.getAnchorEvents('../res/Lists/events/' + scen + '_anchor_events')
  if p:
    participants = M.getParticipants('../res/Lists/participants/' + scen + '_sets','l') 
  if e:
    events = list(M.getEvents('../res/Lists/events/' + scen + '_events'))

  #print('Events:\n', events)
  # M def makeMixTriples(event, e=2, p = 1, s=True):
  #events = list(getSetOfEvents(getEventSource(event)))
  #participants = [list(s) for s in getParticipantSets(getParticipantSource(event))]


  anchEvent_tuples = []
  if a == 1:
    for aeL in anchEvents:
      for ae in aeL:
        anchEvent_tuples.append([ae])
  elif a > 1:
    generateTuplesWithSize(anchEvents, a, anchEvent_tuples)


  participant_tuples = []
  if p == 1:
    for pL in participants:
      for p in pL:
        participant_tuples.append([p])
  elif p > 1:
    #print('type part:', type(participants))
    #print('part:', (participants))
    generateTuplesWithSize(participants, p, participant_tuples)
 

  if e == 0:
    event_tuples = []
  elif e == 1:
    event_tuples = [[event] for event in events]
  elif e == 2:
    le = len(events)
    event_tuples = [[events[a],events[b]] for a in range(le) for b in 
                     range(a+1,le) if events[a] != events[b] ]
  elif e == 3:
    event_tuples = [[a,b,c] for a in events for b in events for c in events 
                                            if a != b and a != c and b != c]

  #print('AnchorEventTuples:\n', anchEvent_tuples)
  #print('ParticipantTuples:\n', participant_tuples)
  #print('EventTuples:\n', event_tuples)
  #print('scenario name in query:',s)

  def mix(*args):
    ret = ''
    for arg in args: 
      for strng in arg:
        strng = strng.strip(' .')
        if ' ' in strng:
          ret += ' "' + strng + '" '
        else:
          ret += ' ' + strng + ' '
    if s:
      return ret[1:] + '"' + scen.replace('_',' ')
    else:
      return ret[1:-1] 

  #qElems = [mix(aq,pq,eq) for aq in anchEvent_tuples for pq in participant_tuples for eq in event_tuples]

  with open('../res/Queries/' + strat + '_' + scen + '_queries.txt', 'w') as out:
    for q in  [mix(aq,pq,eq) for aq in anchEvent_tuples 
                for pq in participant_tuples for eq in event_tuples]:
      out.write(q + '\n')
  with open('../res/Queries/createdQueries.txt', 'a') as log:
    log.write(scen + '\t' + strat + '\n')


###M
def generateTuplesWithSize(multiSet, tupleSize, resultList):
  for currentStartSetIndex in range(len(multiSet) - tupleSize + 1):
    for startElementIndex in range(len(multiSet[currentStartSetIndex])):
      addToTuple(currentStartSetIndex,startElementIndex,list(),tupleSize,
                  multiSet,resultList)

def addToTuple(currentSetIndex, currentElementIndex, currentTuple, tupleSize, 
              multiSet, resultList):
  currentTuple.append(multiSet[currentSetIndex][currentElementIndex])
  if len(currentTuple) == tupleSize:
    resultList.append(currentTuple)
  else:
    tupleElementsLeft = tupleSize - len(currentTuple)
    for nextSet in range(currentSetIndex+1,len(multiSet)-tupleElementsLeft+1):
      for elementIndex in range(len(multiSet[nextSet])):
        addToTuple(nextSet,elementIndex,list(currentTuple),tupleSize,multiSet,
                    resultList)
###M


#naming convention: [s][a<n>][p<n>][e<n>], <n> is between 0 and 9
# for now, a not supported, e max 3 in size
# ToDo write function for variable e size

def strategies():
  yield('a1p2e1')
  return
  for a in range(0,3):
    print('a = ', a)
    for e in range(0,4):
      print('e =',e)
      for p in range(0,4):
        yield 'a'+str(a)+'e'+str(e)+'p'+str(p)
        yield 'sa'+str(a)+'e'+str(e)+'p'+str(p)
