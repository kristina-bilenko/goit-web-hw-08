from models import Authors, Quotes
import sys

sys.stdout.reconfigure(encoding="utf-8")

while True:
    command = input("Введіть команду: ").strip()

    if command == "exit":
        print("Програму завершено!")
        break

    elif command.startswith("name:"):
        name = command.split(":", 1)[1].strip()

        author = Authors.objects(fullname=name).first()

        if author:
            quotes = Quotes.objects(author=author)

            for quote in quotes:
                print(quote.quote)
        else:
            print("Автора не знайдено")

    elif command.startswith("tag:"):
        tag = command.split(":", 1)[1].strip()

        quotes = Quotes.objects(tags=tag)

        for quote in quotes:
            print(quote.quote)

    elif command.startswith("tags:"):
        tags = command.split(":", 1)[1].strip().split(",")
        tags = [tag.strip() for tag in tags]

        quotes = Quotes.objects(tags__in=tags)

        for quote in quotes:
            print(quote.quote)

    else:
        print("Невідома команда. Спробуйте ще раз.")