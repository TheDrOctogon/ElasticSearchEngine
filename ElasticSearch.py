import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import os
import newspaper
from newspaper import Source, Article, fulltext

es = Elasticsearch()
i=1

data = {}
data['articles'] = []
menu = {}
menu['1']="Update Database"
menu['2']="Search Test"
menu['3']="Database stats"
menu['4']="Exit"
while True:
    for entry in menu:
        print (entry, menu[entry])

    selection=input("Please Select:")
    if selection == '1':
        cnn_paper = newspaper.build('http://cnn.com', language='en', fetch_images=False, number_threads=20)
        for article in (cnn_paper.articles):
            if i < 100:
                try:
                    print(i)
                    print(article.url)
                    article.download()
                    print("article downloaded")
                    article.parse()
                    print("article parsed")
                    article.authors
                    article.text
                    article.title
                    data['articles'].append({
                        'title': article.title,
                        'author': article.authors,
                        'text': article.text
                    })
                    print("pushed into data")
                    res = es.index(index="articles", body=data['articles'][0])
                    print("indexed")
                    data['articles'].clear()
                    print("dict cleared")
                    i = i + 1
                except:
                    i = i + 1
                    pass

    elif selection == '2':
        res = es.search(index='articles', body={'query': {'match': {'text': 'virus'}}})
        print(res['hits']['hits'])

    elif selection == '3':
        es.indices.refresh('articles')
        res=es.cat.count('articles', params={"format": "json"})
        print(res)

    elif selection == '4':
        break

    else:
        print
        "Unknown Option Selected!"






