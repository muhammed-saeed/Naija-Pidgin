'''
creates search strings and write them in a file
partly uses code from Ms CreateTwitterStrings.py
'''

from utilities import *
import readMsFiles as M
import re
shorts = M.scenarioShorts()
out_participants = ['it','s','bin']

def createQueries(scen, short, outf,p_from_scen = None, log = stdout):
  if p_from_scen is None:
    print('no participant for scenario name given')
    p_from_scen = short # participant is often the short name

  log.write("Creating queries for " + scen.replace('_',' ') + '\n')

  participants = M.getParticipants('../res/Lists/participants/' + short + 
                                    '_sets','l') 

  #vos
  vo_pairs = set()
  #rel_p = re.compile('(\w+)\((\w+)-(\d+), (\w+)-(\d+)\)') #dependency relation pattern
  rel_p = re.compile('((?:\w|-|\\\\\\/)+)\(((?:\w|[-' + "'" + '`.]|\\\\\\/)+)-(\d+), ((?:\w|[-' + "'" + '`.]|\\\\\\/)+)-(\d+)\)') #dependency relation pattern  
  verb = obj = None
  deps = set()
  with open('../res/ParseData/dep/' + scen + '.dep') as dep:
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
          continue
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
          if not (p in out_participants or p == p_from_scen or p == o):
            q_id += 1
            query = '\t'.join((str(q_id).zfill(6),'?', v, o, p, p_from_scen))
            out.write(query + '\n')
  print(q_id,'queries created.')

  with open('../res/Queries/createdQueries.txt', 'a') as q_log:
    q_log.write('\n'.join((timestamp(), scen, outf)) + '\n\n') # + timestamp outfile ...

if __name__ == '__main__':
  createQueries('change_bed_sheets', 'bed_sheets','cq.bed_sheet_queries.txt')
