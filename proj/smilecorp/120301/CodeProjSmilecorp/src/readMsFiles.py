def getEvents(filename):
  es = set()
  with open(filename) as f:
    for line in f:
      e = line.strip()
      if not e in ['get','take','be','is','have','put','place','make',
          'go','go to','stand','walk','turn','turn on','add','remove']: 
        es.add(e)

  return es


def getParticipants(filename, form = 's'):
  psets = eval(open(filename).read())
  if form == 's':
    return psets
  plists = []
  for s in psets:
    plists.append(list(s))
  if form == 'l':
    return plists
  print('format flag is not a correct option')
  raise Exception

def getAnchorEvents(filename):
  aes = list() #of lists/sets
  with open(filename) as f:
    for line in f:
      if not line:
        continue
      try:
        ae = eval(line)
        if isinstance(ae,list):
          aes.append(ae)
      except Exception as e:
        print('Something wrong with line: ' + line)
        raise e

  return aes


def getEventDescriptions(scen):
  eDs = dict()
  fNames = {"vending_machine":'omics/buy_from_vending_machine.csv',
      "laundry":'omics/do_laundry.csv',
      "fast_food":'mturk/eat_in_fast_food_restaurant_filtered.csv',
      "dog":'omics/feed_a_pet_dog.csv',
      "microwave":'omics/heat_food_in_microwave.csv',
      "letter":'omics/mail_a_letter.csv',
      "coffee":'omics/make_coffee.csv',
      "credit_card":'mturk/pay_with_credit_card_filtered.csv',
      "food_back":'mturk/send_food_back_filtered.csv',
      "shower":'mturk/take_a_shower_filtered.csv'}
  fN = fNames[scen]
  omics = fN.startswith('omics')
  

  with open('../res/Lists/' + fN) as f:
    for line in f:
      if omics:
        leDs = line.split(';')
        for eD in leDs:
          eD = eD.strip(" .\n")
          if eD:
            if eD in eDs:
              eDs[eD] += 1
            else:
              eDs[eD] = 1

      else:
        leDs = line.split(',')
        for eD in leDs:
          eD = eD.strip()
          if eD != 'null' and eD != '':
            if eD in eDs:
              eDs[eD] += 1
            else:
              eDs[eD] = 1

  return set(eDs.keys())


def scenarioShorts():
  return ["vending_machine","laundry","fast_food","dog","microwave","letter",
      "coffee","credit_card","food_back","shower"]
 
participant_suffix = "_sets"
event_suffix = "_events"
event_result_suffix = "_eventlist"
mix_result_suffix ="_mixedlist"



'''
shower_events: Vs, 1 or 2 words, not yet cleaned of put etc
_anchor_events: list of full script items that describe an anchor event, one per line, eval() should work
_sets: list of sets of participants

_list: looks like a SubjNP ObjNP prepNP mixlist
_eventlist: mixlist of events, M
_mix..234 several mixlists
slightly different name_gold_sets: human readable version of _sets, seems to have more entries, cutoff when less than n occurrences of participant instance?
_tweets.csv Tweets found with TwitterSearch script by M
'''


