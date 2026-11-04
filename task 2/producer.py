import pika
import json
import connect
from faker import Faker
from models import Contact

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email', durable=True)

    fake = Faker()

    for _ in range(5):
        contact = Contact(fullname=fake.name(), email=fake.email(), text=fake.text())
        contact.save()
        message = {"id": str(contact.id), "fullname": contact.fullname, "email": contact.email, "text": contact.text}
        message_json = json.dumps(message)
        channel.basic_publish(exchange='', routing_key='email', body=message_json.encode('utf-8'))
        print(f" [x] Sent '{contact.text}' for {contact.fullname} on {contact.email}")

    connection.close()

if __name__ == '__main__':
    main()
