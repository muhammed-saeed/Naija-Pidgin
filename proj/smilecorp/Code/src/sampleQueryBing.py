from bingapi.bingapi3ify import Bing
app_id = '7977945912BDC64D968333DD9B3053001E4395AB'
print('.')

def dictprint(d, indent = 0):
  #print(d)
  #return
  for k in d:
    print(indent * '  ', k, sep = '')
    v = d[k]
    if isinstance(v, dict):
      dictprint(v, indent + 1)
    elif isinstance(v, list):
      listprint(v, indent + 1)
    else:
      print((indent + 1) * '  ', v, sep = '')  
def listprint(l, indent = 0):
  #print(indent * '  ' + 'list, ', len(l))
  return
  
  print(indent * '  ' + '[ length' + str(len(l)))
  i = 0
  for e in l:
    i += 1
    print(indent * '  ' + str(i))
    if isinstance(e, dict):
      dictprint(e, indent + 1)
    elif isinstance(e, list):
      listprint(e, indent + 1)
    else:
      print((indent + 1) * '  ', v, sep = '')

  print(indent * '  ' + ']')
 
bing = Bing(app_id)
offset = 0
count = 2
while offset < 3: #1000
  result = bing.do_web_search("bing", extra_args={'web.count':count, 'web.offset':offset})
  offset += count
  dictprint(result)

print('.')
