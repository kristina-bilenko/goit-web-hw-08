import json
from models import Authors, Quotes

Authors.drop_collection()
Quotes.drop_collection()

with open("authors.json", "r", encoding="utf-8") as file:
    authors = json.load(file)

for author in authors:
    Authors(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        description=author["description"]
    ).save()

with open("quоtes.json", "r", encoding="utf-8") as file:
    quotes = json.load(file)

for quot in quotes:
    author = Authors.objects(fullname=quot["author"]).first()
    Quotes(
        tags=quot["tags"],
        author=author,
        quote=quot["quote"]
    ).save()