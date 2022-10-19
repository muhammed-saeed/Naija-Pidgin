from utilities import *
from os.path import isfile


def _get_doc_score(doc_id, corpus, q_scores):
  score = 0.0
  q_p = re.compile('<query id="(.*?)" bing-rank="(.*?)"')
  with open(corpus + '_docs/' + doc_id + '.xml') as doc:
    doc.readline() #header
    doc.readline() #document tag
    for line in doc:
      mo = q_p.search(line)
      if mo:
        q_score = float(q_scores[mo.group(1)])
        rank_score = (0.5 + ((250 - int(mo.group(2))) / 500))
        score += q_score * rank_score
        #print(score)
      else:
        break
  return score

def make_doc_scores(corpus):
  q_scores = {}#'00998':0.0,'01082':0.0,'01092':0.0,'01086':0.0,'01083':0.0}
  id_p = re.compile('<document id="(.*?)"')
  with open(corpus + '_doc_scores.csv','w') as scs:
    with open(corpus + '_corpus.xml') as c:
      c.readline() #header
      c_elem = c.readline() #corpus tag
      q_f = re.search('potential_queries="(.*?).txt"',c_elem).group(1)
      with open(q_f + '_scored.txt') as qs:
        qs.readline()
        for line in qs:
          q = line.split('\t')
          q_scores[q[0]] = q[1]

      for line in c:
        mo = id_p.search(line)
        if mo:
          doc_id = mo.group(1)
          scs.write(''.join((doc_id, '\t', 
                    str(_get_doc_score(doc_id, corpus, q_scores)),'\n')))

#TODO do this for url shelve rather than finished corpus
#  then score on/off for buildCorpus

def _get_url_score(url_id, results, q_scores):
  score = 0.0
  found_by = results[url_id]
  for (q_id, b_rank) in found_by:
    q_score = q_scores[q_id]
    rank_score = (0.5 + ((250 - int(b_rank)) / 500))
    score += q_score * rank_score
    #print(score)
  return score

def make_url_scores(url_dir, scored_query_f):
  with open(url_dir + '/url_scores.csv','w') as scs_table:
    with closing(shelve.open(url_dir + '/url_scores')) as scs:
      results = [shelve.open(url_dir + '/results0', 'r')]
      rs_no = 0
      while True:
        rs_no += 1
        if isfile(url_dir + '/results' + str(rs_no) + '.db'):
          results.append(shelve.open(url_dir + '/results' + str(rs_no), 'r'))
        else:
          break
      if isinstance(scored_query_f, str): #is a file
        try:
          with closing(shelve.open(url_dir + '/query_scores', 'r')) as q_scores:
            if len(q_scores) == 0:
              raise Exception
        except:
          #if not isfile(url_dir + '/query_scores.db'):
          with open(scored_query_f) as scored_queries:
            scored_queries.readline()
            with closing(shelve.open(url_dir + '/query_scores')) as q_scores:
              for line in scored_queries:
                q = line.split('\t')
                q_scores[q[0]] = float(q[1])

        with closing(shelve.open(url_dir + '/query_scores', 'r')) as q_scores:
          for rs in results:
            for url_id in rs:
              url_score = _get_url_score(url_id, rs, q_scores)
              scs_table.write(''.join((url_id, '\t', 
                      str(url_score),'\n')))
              scs[url_id] = url_score



      else: # assumes that it is the q_scores shelve
        q_scores = scored_query_f 
        for rs in results:
          for url_id in rs:
            print('here', url_id)
            url_score = _get_url_score(url_id, rs, q_scores)
            scs_table.write(''.join((url_id, '\t', 
                    str(url_score),'\n')))
            scs[url_id] = url_score



      for rs in results:
        rs.close()

if __name__ == '__main__':
  make_doc_scores('../res/Corpora/dog_developing_corp_22')
