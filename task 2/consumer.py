import pika
import sys
import json
import connect
from models import Contact


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email', durable=True)

    def sending_email(contact):
        contact_db = Contact.objects(id=contact["id"]).first()
        if contact_db:
            contact_db.done = True
            contact_db.save()
            print(f"Email sent to {contact_db.email}")

    def callback(ch, method, properties, body):
        message = body.decode('utf-8')
        contact = json.loads(message)
        sending_email(contact)
        print(f" [x] Received {contact}")

    channel.basic_consume(queue='email', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
