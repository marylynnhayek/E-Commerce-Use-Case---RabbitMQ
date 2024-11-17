import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)

for i in range(3):
    customer_name = f"Customer{i+1}"
    destination = f"customer{i+1}@gmail.com"
    promotion_code = f"USJ-PROMO2024-{i+1}"
    product_recommendation = f"Top Pick Product #{i+1}"
    product_line = "Winter Collection"

    promo_body = (
        f"Dear {customer_name},\n\n"
        f"Thank you for shopping at USJ-Store!\n\n"
        f"We have a special offer just for you!\n"
        f"Enjoy a 20% discount on your next purchase using the code: {promotion_code}.\n"
        f"Don't miss out on this limited-time offer!\n\n"
        f"Happy Shopping!\n"
        f"USJ-Store Team"
    )

    marketing_body = (
        f"Hi {customer_name},\n\n"
        f"Discover the latest addition to our {product_line}!\n\n"
        f"Our featured product: {product_recommendation} is now available at a special price.\n"
        f"Upgrade your wardrobe with this stylish and versatile piece perfect for any season.\n"
        f"Visit our store now to check it out!\n\n"
        f"Best regards,\n"
        f"USJ-Store Fashion Team"
    )

    feedback_body = (
        f"Hello {customer_name},\n\n"
        f"We hope you enjoyed your recent purchase from USJ-Store.\n\n"
        f"We would love to hear your thoughts and feedback on your shopping experience.\n"
        f"Your feedback helps us improve and serve you better.\n\n"
        f"Click here to leave your review: [Feedback Link]\n\n"
        f"Thank you for your time!\n"
        f"USJ-Store Customer Service"
    )
    
    if i == 0:
        body = promo_body
        message_type = "Promotional Discount Message"
    elif i == 1:
        body = marketing_body
        message_type = "Product Marketing Message"
    else:
        body = feedback_body
        message_type = "Feedback Request Message"

    delimiter = "###"
    message = f"{delimiter}\nBody: {body}\nDestination: {destination}\n{delimiter}\n"

    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )
    print(f"Sent ({message_type}): {message}")
    time.sleep(1)

connection.close()