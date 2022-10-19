
import createQueries as cQ
import readMsFiles as M
import bingFunctions as bF
import subprocess
import time


def GBcountEventDescriptions(scen):
  eDs = M.getEventDescriptions(scen)
  with open('../res/Lists/EventDescriptions/' + scen + 
      '_eventDescriptions.txt', 'w') as out:
    for eD in eDs:
      out.write('"' + eD + '"\n')


queries = ['"sign the receipt" "credit card" checkout','"sign the receipt" "credit card" wallet']
for url, n in sorted(bF.firstNResultsDict(queries,250).items(), key = lambda x: x[1]):
  print(n,url)




#print('nichts')


'''
strategy, queries, counts for queries

strats = ['a1p2e1']
scens = ['vending_machine']

for strat in strats:#cQ.strategies():
  for scen in scens:#M.scenarioShorts():
    #cQ.createQueries(strat, scen)
    
    p = subprocess.check_output(['perl', 'GoogleCountPerlScript/google_carolyn.pl', 
        '../res/Queries/' + strat + '_' + scen + '_queries.txt', 
        '../res/Queries/' + strat + '_' + scen + '_queries_G.txt'])
    print('p',p)
    try:
      bF.bingCount('../res/Queries/' + strat + '_' + scen + '_queries_G.txt', 
          '../res/Queries/' + strat + '_' + scen + '_queries.txt_BG')
    except Exception as e:
      print('bingCount', strat, scen, e)
'''

'''
get G and B counts for event descriptions

scen = 'food_back'#'letter'#'fast_food'#microwave'#'dog'#'credit_card'#'coffee'#'shower'#'laundry'#'vending_machine'
print(scen, 'google', time.ctime())
p = subprocess.check_output(['perl', 'GoogleCountPerlScript/google_carolyn.pl', 
      '../res/Lists/EventDescriptions/' + scen + '_eventDescriptions.txt', 
      '../res/Lists/EventDescriptions/' + scen + '_eventDescriptions_G.txt']) 
print(scen, 'bing', time.ctime())
bF.bingCount('../res/Lists/EventDescriptions/' + scen + 
  '_eventDescriptions_G.txt',  '../res/Lists/EventDescriptions/' + scen + 
  '_eventDescriptions_BG.txt')
print(scen, 'done', time.ctime())
'''
'''done once, wrong google, no verbatim, bing zu oft pro zeit
for scen in M.scenarioShorts():
  #done GBcountEventDescriptions(scen)
  print(scen,'google', time.ctime())
  p = subprocess.check_output(['perl', 'GoogleCountPerlScript/google_carolyn.pl', 
        '../res/Lists/EventDescriptions/' + scen + '_eventDescriptions.txt', 
        '../res/Lists/EventDescriptions/' + scen + '_eventDescriptions_G.txt'])
  print(scen,'bing', time.ctime())
  bF.bingCount('../res/Lists/EventDescriptions/' + scen + '_eventDescriptions_G.txt',  '../res/Lists/EventDescriptions/' + scen + '_eventDescriptions_BG.txt')
'''
'''
a1p2urls = firstNResultsStrategy('a1p2')
for a,v in sorted(a1p2urls.items(), key = lambda x : -x[1]):
  print(a,v)
'''
