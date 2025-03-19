
from functools import reduce


def get_prices(Nstore,products,sales):
    return tuple((k,v - (tuple(filter(lambda x: x[0] == Nstore,sales)))[0][1] * v)for k, v in products)

def get_prices_dict(Nstore,prod_dict,sale_dict):
    return {k:v*(1-sale_dict[Nstore]) for (k,v) in prod_dict.items()}

def get_prices_by_type(Nstore,prod_dict,sales,types):
    return {a: (b - sales.get(Nstore).get(tuple(filter(lambda x: True if a in types[x] else False, types))[0])*b) for a,b in prod_dict.items()}

# {a: (b - sales.get(Nstore).get(tuple(filter(lambda x: True if a in types[x] else False, types))[0])*b) for a,b in prod_dict.items()}
def accumulate_prices(Nstore,prod_dict,sales,types,add):
    return reduce(lambda a,b: a+b,{a: (b - sales.get(Nstore).get(tuple(filter(lambda x: True if a in types[x] else False, types))[0])*b) for a,b in prod_dict.items()}.values())

products = (('p1',1000),('p2',2000),('p3',5000),('p4',100))
sales = (('s1',0.2),('s2',0.3),('s3',0.1))

prod_dict = dict(products)
sale_dict = dict(sales)
print("A:")
print(get_prices('s1',products,sales))
print("B:")
print(get_prices_dict('s1',prod_dict,sale_dict))

sales = {'s1':{'t1':0.2, 't2':0.1}, 's2':{'t1':0.1, 't2':0.2},'s3':{'t1':0.3, 't2':0.5}}
types = {'t1':('p2', 'p4'), 't2':('p1', 'p3')}
print("C:")
print(get_prices_by_type('s1', prod_dict, sales, types))

print("D:")
add = None
print(accumulate_prices('s1',prod_dict,sales,types,add))