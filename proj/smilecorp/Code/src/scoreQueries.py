from utilities import *

from os import listdir as ls
from math import log

def _per_scen_vo_counts(scen_long, idf_shelve):#scenario dependency file name (without ending)
  #vos
  if '_total docs' in idf_shelve:
    tmp_count = idf_shelve['_total docs'] + 1
    idf_shelve['_total docs'] = tmp_count
  else:
    idf_shelve['_total docs'] = 1

  vo_pairs = shelve.open('../res/Queries/Scoring/vo_tfs_' + scen_long)
  rel_p = re.compile('((?:\w|-|\\\\\\/)+)\(((?:\w|[-' + "'" + '`.]|\\\\\\/)+)-(\d+), ((?:\w|[-' + "'" + '`.]|\\\\\\/)+)-(\d+)\)') #dependency relation pattern
  verb = obj = None
  deps = set()
  with open('../res/ParseData/dep/' + scen_long + '.dep') as dep:
    for line in dep:
      if not line.strip():
        dobjs = [(x,y) for (x,y,z) in deps if z == 'dobj']
        if dobjs:
          #if len(dobjs) > 1:
          for v,o in dobjs:
            for top,bottom,r in deps:
              if bottom == v:
                break
            else:
              verb, obj = v, o
              #i assume there is only one headverb
              break
          #else:
          #  verb, obj = dobjs[0]
          if verb is not None and obj is not None:
            obj_l = [y for (x,y,z) in deps 
                      if (z == 'nn' or z == 'amod') and x == obj]
            obj_l.append(obj)
            #if obj_l:
              #print('v,o,oa:',verb,obj,obj_l)

            obj_str = ' '.join(word for (word,pos) in sorted(obj_l, 
                                key = lambda x: int(x[1])))
            #if ' ' in obj_str:
              #print(verb[0], obj_str, obj_l)
          
            #vo_pairs.add((verb[0],obj_str))
            if verb[0] + '\t' + obj_str in vo_pairs:
              tmp_count = vo_pairs[verb[0] + '\t' + obj_str] + 1
              vo_pairs[verb[0] + '\t' + obj_str] = tmp_count
            else:
              vo_pairs[verb[0] + '\t' + obj_str] = 1
              if verb[0] + '\t' + obj_str in idf_shelve:
                tmp_count = idf_shelve[verb[0] + '\t' + obj_str] + 1
                idf_shelve[verb[0] + '\t' + obj_str] = tmp_count
              else:
                idf_shelve[verb[0] + '\t' + obj_str] = 1
            if '_total vos' in vo_pairs:
              tmp_count = vo_pairs['_total vos'] + 1
              vo_pairs['_total vos'] = tmp_count
            else:
              vo_pairs['_total vos'] = 1

        obj_str = obj_l = verb = obj = None
        deps = set()
        
        
        #interesting relations: dobj, 
        # also:TODO nn for #2 of dobj
      else:
        rel = rel_p.match(line)
        if not rel:
          print('Line cannot be parsed as a dependency relation:')
          print(line)
          continue
        deps.add(((rel.group(2), rel.group(3)), (rel.group(4), rel.group(5)), 
                  rel.group(1)))
  vo_pairs.close()


def _per_scen_ngram_counts(scen_long, idf_shelve):
  #vos
  if '_total docs' in idf_shelve:
    tmp_count = idf_shelve['_total docs'] + 1
    idf_shelve['_total docs'] = tmp_count
  else:
    idf_shelve['_total docs'] = 1

  tf_shelve = shelve.open('../res/Queries/Scoring/ngram_tfs_' + scen_long)
  
  ngram_p = re.compile('') #n-gram pattern

  with open('../res/ParseData/txt/' + scen_long + '.txt') as txt:
    for line in txt:
      #print('line',line)
      for n in range(1,5):
        ngram_p = re.compile('(\w+)' + ('' if n <= 1 else 
                            ('(?=' + ((n-1) *'\W+?(\w+)' + ')')))) #n-gram pattern
        for mo in ngram_p.finditer(line):
          ngram = ' '.join(mo.groups())
          #print(n,ngram)
              
          if ngram in tf_shelve:
            tmp_count = tf_shelve[ngram] + 1
            tf_shelve[ngram] = tmp_count
          else:
            tf_shelve[ngram] = 1
            if ngram in idf_shelve:
              tmp_count = idf_shelve[ngram] + 1
              idf_shelve[ngram] = tmp_count
            else:
              idf_shelve[ngram] = 1
          if '_total ' + str(n) in tf_shelve:
            tmp_count = tf_shelve['_total ' + str(n)] + 1
            tf_shelve['_total ' + str(n)] = tmp_count
          else:
            tf_shelve['_total ' + str(n)] = 1


  #for n in range(1,9):
  #  print(tf_shelve['_total ' + str(n)],str(n),'grams')

  tf_shelve.close()






def make_vo_shelves():
  print('vo shelves already there, breaking')
  return
  score_dir = '../res/Queries/Scoring/'
  dep_dir = '../res/ParseData/dep/'
  dep_files = [name[:-4] for name in ls(dep_dir) if name[-4:] == '.dep']
  
  idf_shelve = shelve.open(score_dir + 'vo_idfs')
  for scen_long in dep_files:
    print(scen_long)
    _per_scen_vo_counts(scen_long, idf_shelve)
  print('done vos')
  #c1 = c2 = 0
  #for k in idf_shelve:
  #  if 1 == idf_shelve[k]:
  #    c1 += 1
  #  else:
  #    c2 += 1

  print(idf_shelve['_total docs'],'docs')
  #print('once',c1)
  #print('more',c2)
  idf_shelve.close()

def make_ngram_shelves():
  print('ngram shelves already there, breaking')
  return

  score_dir = '../res/Queries/Scoring/'
  txt_dir = '../res/ParseData/txt/'
  txt_files = [name[:-4] for name in ls(txt_dir) if name[-4:] == '.txt']
  
  idf_shelve = shelve.open(score_dir + 'ngram_idfs')
  for scen_long in txt_files:
    print(scen_long)
    _per_scen_ngram_counts(scen_long, idf_shelve)
  print('done ngrams')
  #c1 = c2 = 0
  #for k in idf_shelve:
  #  if 1 == idf_shelve[k]:
  #    c1 += 1
  #  else:
  #    c2 += 1

  print(idf_shelve['_total docs'])
  #print('once',c1)
  #print('more',c2)
  idf_shelve.close()


def make_tfidf_shelves():
  make_vo_shelves()
  make_ngram_shelves()

def get_vo_tfidf(scen_long, verb, obj, tf_shelve = None, idf_shelve = None):
  vo = verb + '\t' + obj
  ct = cid = False
  if tf_shelve is None:
    ct = True
    tf_shelve = shelve.open('../res/Queries/Scoring/vo_tfs_' + scen_long,'r')
  if idf_shelve is None:
    cid = True
    idf_shelve = shelve.open('../res/Queries/Scoring/vo_idfs', 'r')
  
  tf = float(tf_shelve[vo])/tf_shelve['_total vos']
  idf = log(float(idf_shelve['_total docs']) / idf_shelve[vo])

  if ct: tf_shelve.close()
  if cid: idf_shelve.close()

  return tf*idf
  

def get_part_tfidf(scen_long, part, tf_shelve = None, idf_shelve = None):
  ct = cid = False
  gram_n = len(part.split())
  if tf_shelve is None:
    ct = True
    tf_shelve = shelve.open('../res/Queries/Scoring/ngram_tfs_' + scen_long,'r')
  if idf_shelve is None:
    cid = True
    idf_shelve = shelve.open('../res/Queries/Scoring/ngram_idfs', 'r')

  if part in tf_shelve:
    tf = float(tf_shelve[part])/tf_shelve['_total ' + str(gram_n)]
  else:
    tf = 0.0
    print(part,'=participant not in tf_shelve')
    #raise Exception
  if part in idf_shelve:
    idf = log(float(idf_shelve['_total docs']) / idf_shelve[part])
  else:
    print(part,'=participant not in idf_shelve')
    idf = 0.0

  if ct: tf_shelve.close()
  if cid: idf_shelve.close()

  return tf*idf
  



def score_queries(query_f, scen_long):
  try:
    vo_tf_shelve = shelve.open('../res/Queries/Scoring/vo_tfs_' + scen_long, 'r')
    vo_idf_shelve = shelve.open('../res/Queries/Scoring/vo_idfs', 'r')
    ngram_tf_shelve = shelve.open('../res/Queries/Scoring/ngram_tfs_' + scen_long, 'r')
    ngram_idf_shelve = shelve.open('../res/Queries/Scoring/ngram_idfs', 'r')
  except Exception as e:
    print('encountered exception during score_queries():')
    print(e)
    if ask_yes_no('do you want to build tf-idf-shelves to go on? '):
      make_tfidf_shelves()
      vo_tf_shelve = shelve.open('../res/Queries/Scoring/vo_tfs_' + scen_long, 'r')
      vo_idf_shelve = shelve.open('../res/Queries/Scoring/vo_idfs', 'r')
      ngram_tf_shelve = shelve.open('../res/Queries/Scoring/ngram_tfs_' + scen_long, 'r')
      ngram_idf_shelve = shelve.open('../res/Queries/Scoring/ngram_idfs', 'r')
    else:
      raise e
  
  with open(query_f) as qs:
    scored_query_f = query_f[:-4] + '_scored' + query_f[-4:]
    with open(scored_query_f ,'w') as sqs:#assumes .txt
      sqs.write(qs.readline())
      for line in qs:
        ID, score, verb, obj, part, ptitle = line.split('\t')
        score = get_vo_tfidf(scen_long, verb, obj, vo_tf_shelve, vo_idf_shelve)
        score *= get_part_tfidf(scen_long, part, ngram_tf_shelve, ngram_idf_shelve)
        sqs.write('\t'.join((ID,str(score), verb, obj, part, ptitle)))

        
        
  
  vo_tf_shelve.close()
  vo_idf_shelve.close()
  ngram_tf_shelve.close()
  ngram_idf_shelve.close()
  print('scored',query_f)
  return scored_query_f 


if __name__ == '__main__':
  make_tfidf_shelves()
  score_queries('../res/Queries/dog_queries.txt','feed_a_pet_dog')
        
