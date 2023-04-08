#  решить с помощью list comprehension и распечатать его
ldict = [{'bin': str(bin(i)), 'dec': i, 'hex': str(hex(i)), 'oct': str(oct(i))} for i in range(16)]
from pprint import pprint

pprint(ldict)
