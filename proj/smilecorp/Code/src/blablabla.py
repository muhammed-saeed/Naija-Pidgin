def build_corpus(corpus_name, scen_id, scen, scen_short, scen_par = None, 
                                    new_urls = True, new_qs = False):
    scen = scen.replace(' ', '_')
    scen_short = scen.replace(' ', '_')
    scen_par = scen_par.replace(' ', '_')




  with open(corpus_f,'w') as c:
    c.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n\t',
        '<corpus eventid="', '1234', #TODO how get eventid, as function param
        '" scenario="'+scen.replace('_',' ')+'" short="'+scen_short.replace('_',' ')+'" time="', timestamp(), 
        '" potential_queries="', query_f, '">\n')))
  #TODO get scenario names from function parameters




def get_all_corpora_gen(new_urls = True, new_qs = False):
  shorts = ["fast_food","food_back","laundry","coffee","dog", "microwave",
                            "credit_card","vending_machine","letter","shower"]      
    ids = [2, 3 ,56, 111, 66 , 92, 11, 31, 101, 14]
  not_so_shorts = ["fast food restaurant", "send food back", "do laundry", 
                                     "make coffee", "feed a dog", #"phone", "iron",
                                    "heat sth in microwave", "pay w credit card", 
                                    "buy f vending machine", "mail a letter", "take a shower"]

    scenarios = ['eat_in_fast_food_restaurant_filtered', 'send_food_back_filtered', 
                            'do_laundry', 'make_coffee', 'feed_a_pet_dog', 'heat_food_in_microwave', 
                            'pay_with_credit_card_filtered', 'buy_from_vending_machine', 
                            'mail_a_letter', 'take_a_shower_filtered'] 
    participants = ['fast_food_restaurant', 'food_back', 
                            'laundry', 'coffee', 'dog', 'microwave', 
                            'credit_card', 'vending_machine', 
                            'letter', 'shower'] 


    for i in range(10):
        yield 'will create' + scenarios[i]
        build_corpus(scenarios[i], ids[i], scenarios[i], shorts[i], participants[i], new_urls, new_qs)
        yield 'created' + scenarios[i]

    yield 'created all 10 corpora'
    return




-------------------------------
####  createQueries.py

for now long and short name
def createQueries(scen, outf,p_from_scen = None, log_f = stdout):

  print("Creating queries for " + scen.replace('_',' ') + ' scenario')

  participants = M.getParticipants('../res/Lists/participants/' + scen + 
                                    '_sets','l') 
#TODO these are nt so short names, change to gold sets?

  #vos


 #vos
  vo_pairs = set()
  rel_p = re.compile('(\w+)\((\w+)-(\d+), (\w+)-(\d+)\)') #dependency relation pattern
  verb = obj = None
  deps = set()
  with open('../res/ParseData/dep/' + 'feed_a_pet_dog.dep') as dep:
    for line in dep:
      if not line.strip():

change above and eveything that has scen (to short name), scen must mean  long name



if __name__ == '__main__':
  createQueries('feed_a_pet_dog','dog','cq.dog_queries_text.txt')







  
def _make_docs_mini(amount,urls,results,snippets,corpus_name, corpus_f,log_f):
  # make function _make_docs(urls,results,snippets,corpus_name, corpus_f,log_f)
  doc_no = 0
  url_no = 0
  n_succ = n_tot = n_ish = n_perf = 0
  for url in urls:
    '''
    n_supp = str(len(results[urls[url]]))
    url_no += 1
    try:
      title, body, errors = wF.get_doc(url,log_f)
    except Exception as e:
      #raise e
      with open(log_f,'a') as log:
        log.write(''.join(('Document at URL: ',url,
            ' could not be retrieved due to ',type(e).__name__,' : ', str(e),
            '\nIt was found by these queries: \n  ', str(urls[url]),'\n\n')))
      continue
    body =  insertXMLEnt(body.strip())
    title =  insertXMLEnt(title)
    if body:
      n_ish += 1
      if len(body) > 20:
        #print(timestamp(),'len',len(body))
        n_succ += 1
      if errors == '':
        n_perf += 1
    n_tot += 1
    if not body:
      continue
  
    doc_no += 1
      
    doc_id = str(doc_no).zfill(6)
    doc_file = corpus_name + '_docs/' + doc_id + '.xml'
    with open(corpus_f,'a') as c:
      c.write(''.join(('\n\t\t<document id="', doc_id,'" url="', insertXMLEnt(url),'" time="',
                  timestamp(),'" support="',n_supp,'" title="', title, '" file="',
                    insertXMLEnt(doc_file),'">\n')))

      c.write('\t\t</document>\n')
    
    with open('../res/Corpora/' +  insertXMLEnt(doc_file),'w') as d:
      d.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                  '\n<document id="doc', doc_id,'" url="', insertXMLEnt(url),'" time="', 
                  timestamp(),'" support="',n_supp,'" title="',title,'">\n')))

      d_snippet = ''
      for q_id, b_rank in results[urls[url]]:
        sn_no = int(int(urls[url])/10000)
        #print(sn_no)
        snippet = snippets[sn_no][urls[url]+' '+q_id]
        if (not d_snippet) and snippet.strip():
          d_snippet = snippet
        #TODO take best ranked query snippet
        d.write(''.join(('\t\t\t<query id="', q_id,'" bing-rank="',str(b_rank),'"/>\n')))
      d.write(''.join(('\t<description>', d_snippet, '</description>\n',
                  '\t<body>\n\t\t',body,'\n\t</body>\n</document>\n')))
    '''
    counters = doc_no, url_no, n_perf, n_succ,n_ish, n_tot
    nc = _make_doc(counters, url, urls,results,snippets,corpus_name, corpus_f,log_f)
    doc_no, url_no, n_perf, n_succ,n_ish, n_tot = nc

    if (doc_no) == amount:
      break

  print('\n',timestamp())
  print('no probs:',n_perf,'/',n_tot,float(n_perf)/n_tot)
  print('>20chars:',n_succ,'/',n_tot,float(n_succ)/n_tot)
  print('non-empty:',n_ish,'/',n_tot,float(n_ish)/n_tot)
  print(url_no)
  print('')
