import pika
import time

def send_email(body, destination):
    print(f"Sending email to {destination} with body: {body}")
    time.sleep(5)  

def callback(ch, method, properties, body):
    task = body.decode()  
    print(f"Received: {task}")
    
    try:
 
        if ", Destination: " in task:
            body, destination = task.split(", Destination: ")
            body = body.replace("Body: ", "")
            send_email(body, destination)  
        else:
            print(f"Invalid message format received: {task}")
    except Exception as e:
        print(f"Error processing task: {e}")
    ch.basic_ack(delivery_tag=method.delivery_tag)  

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)

channel.basic_qos(prefetch_count=1)

print(' [*] Waiting for messages... To exit press CTRL+C')
channel.basic_consume(queue='email_queue', on_message_callback=callback)
channel.start_consuming()