import math
def es_get_items():
   es_items = int(input('Ether the number of items: '))
   return es_items
def es_get_boxsize():
    es_boxsize = int(input('Enter the number of items per box: '))
    return es_boxsize
def calcboxamt(esi,esbs):
    boxamt = math.ceil(esi / esbs)
    return boxamt

esi = es_get_items()
esbs = es_get_boxsize()
esba = calcboxamt(esi,esbs)
print(f'For {esi} items, packing {esbs} items in each box, you will need {esba} boxes.')

