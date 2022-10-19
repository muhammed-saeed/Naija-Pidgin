class DD(dict):
    '''
    Das Default-Dictionary wird mit einer "Default Factory" initialisiert,
    die ein "callable" sein muss (z.B. eine Funktion) und Default-Werte
    bei Bedarf erzeugt.
    '''
    def __init__(self, makedefault, *optional_args):
        if optional_args:
            super().__init__(optional_args)
        else:
            super().__init__()
        self.makedefault = makedefault

    def __call__(self):
        '''
        Die __call__ Methode erzeugt ein frisches DD-Objekt -- damit kann man
        Default-Dictionaries erzeugen, die ihrerseits ein Default-Dictionary 
        als Default-Wert haben:
        '''
        return DD(self.makedefault)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return dict.setdefault(self, key, self.makedefault())

if __name__=='__main__':
  def makedefault():
      return 'irgendwas'

  d = DD(makedefault, ('blupp','blupp'), ('x','y'))
  print("d = DD(makedefault, ('blupp'='blupp), ('x','y'))")
  print("  d['bla'] : ",d['bla'])
  print("  d['blupp'] : ",d['blupp'])
  print("  d['x'] : ",d['x'],'\n')

  d = DD(int) 
  print('d = DD(int)') 
  print("  d['bla']' : ",d['bla'],'\n')

  d = DD(DD(int))
  print('d = DD(DD(int))')
  print("  d['bla']['blub'] : ",d['bla']['blub'])


