'''
creates search strings and write them in a file
partly uses code from Ms CreateTwitterStrings.py
'''

from utilities import *
import readMsFiles as M
import re
shorts = M.scenarioShorts()
out_participants = ['it','s','bin']

def createQueries(scen, outf,p_from_scen = None, log_f = stdout):
  if p_from_scen is None:
    p_from_scen = scen # participant is often the short name

  print("Creating queries for " + scen.replace('_',' ') + ' scenario')

  participants = M.getParticipants('../res/Lists/participants/' + scen + 
                                    '_sets','l') 

  #vos
  vo_pairs = set()
  rel_p = re.compile('(\w+)\((\w+)-(\d+), (\w+)-(\d+)\)') #dependency relation pattern
  verb = obj = None
  deps = set()
  with open('../res/ParseData/dep/' + 'feed_a_pet_dog.dep') as dep:
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
          
            vo_pairs.add((verb[0],obj_str))
        obj_str = obj_l = verb = obj = None
        deps = set()
        
        
        #interesting relations: dobj, 
        # also:TODO nn for #2 of dobj
      else:
        rel = rel_p.match(line)
        if not rel:
          print('Line cannot be parsed as a dependency relation:')
          print(1,line, len(line))
        deps.add(((rel.group(2), rel.group(3)), (rel.group(4), rel.group(5)), 
                  rel.group(1)))

  #for v,o in vo_pairs:
    #print((v,o))

  q_id = 0
  #with open('../res/Queries/' + strat + '_' + scen + '_queries.txt', 'w') as out:
  with open(outf, 'w') as out:
    out.write('id\tscore\tv\td-obj\tp\tp-title\n')
    for (v,o) in vo_pairs:
      for pl in participants:
        for p in pl:
          if not p in out_participants:
            q_id += 1
            query = '\t'.join((str(q_id).zfill(5),'?', v, o, p, p_from_scen))
            out.write(query + '\n')

  with open('../res/Queries/createdQueries.txt', 'a') as q_log:
    q_log.write('\n'.join((timestamp(), scen, outf)) + '\n\n') # + timestamp outfile ...

if __name__ == '__main__':
  createQueries('dog','cq.dog_queries_text.txt')
