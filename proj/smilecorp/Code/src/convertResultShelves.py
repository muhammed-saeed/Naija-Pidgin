
from sys import argv
import shelve
from contextlib import closing

url_dir = argv[1]
results = [shelve.open(url_dir + '/results0')]
with closing(shelve.open(url_dir+'/results','r')) as old:
  for url_id in old:
    rs_no = int(int(url_id) / 10000)#20000
    if rs_no >= len(results):
      results.append(shelve.open(url_dir + '/results' + str(rs_no)))
    results[rs_no][url_id] = old[url_id]

