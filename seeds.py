import json
from connect import connect
from models import Authors, Quotes


with open("authors.json", "r", encoding="utf-8") as file:
    authors = json.load(file)

for author in authors:
    Authors(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        description=author["description"]
    ).save()

with open("quotes.json", "r", encoding="utf-8") as file:
    quotes = json.load(file)

for quot in quotes:
    author = Authors.objects(fullname=quot["author"]).first()
    Quotes(
        tags=quot["tags"],
        author=author,
        quote=quot["quote"]
    ).save()