import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import os

es = Elasticsearch()
i=1
file=open("docs.json")
docs=json.loads(file.read())



while i <= len(docs['articles']) :
    res = es.index(index="articles", id=i, body=docs['articles'][i-1])
    i=i+1



"""
res=es.get(index="articles",id=1)
print(res)
res=es.get(index="articles",id=2)
print(res)
res=es.get(index="articles",id=3)
print(res)
"""


res= es.search(index='articles',body={'query':{'match':{'text':'shooting'}}})
print (res['hits']['hits'])
