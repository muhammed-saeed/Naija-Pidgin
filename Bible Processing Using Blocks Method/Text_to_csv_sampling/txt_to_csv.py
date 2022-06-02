import pandas as pd

# read_file = pd.read_csv (r'C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\en_parrellel.txt')
# import pandas as pd
df = pd.read_fwf(r'C:\Users\lst\Desktop\Naija-Pidgin\BLOCKS_SPANS\BLOCKS_SPANS\en_bible\en_parrellel.txt')
df.to_csv(r'C:\Users\lst\Desktop\log.csv')

