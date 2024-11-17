![image](https://github.com/user-attachments/assets/2d5643e9-9abc-4699-8e94-2e620a65cbdd)# E-Commerce-Use-Case: Email Messaging System with RabbitMQ:

This assignment implements an Email Messaging System using RabbitMQ as the message broker. The system has a Producer-Consumer architecture where:

- The Producer sends different types of email messages (Promotional, Marketing, Feedback) to a RabbitMQ queue.
- The Consumer listens to the queue, processes the messages, and simulates sending the email to the specified destination.

**Features**:
-------------
1- Utilize RabbitMQ for message queuing.
2- Support three types of email messages:
      - Promotional Emails
      - Product Marketing Emails
      - Feedback Request Emails
3- Demonstrate a Producer-Consumer model with message acknowledgment.

**Prerequisites**:
------------------
- Python 3.10+ installed.
- Docker Desktop installed.
- RabbitMQ Docker image with the management plugin.

**Steps Undertaken:**
1- Install and run Docker desktop.
2- Pull the RabbitMQ image and start a container:
**docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management**

![image](https://github.com/user-attachments/assets/ddfa04de-5f4c-41c5-866e-09b5ec6bb644)

3- Access the RabbitMQ Management Portal:
   **- URL:** http://localhost:15672/
   **- Username:** guest
   **- Password:** guest
4- pip install pika
5- Write the scripts.
6- Start the RabbitMQ Server
7- Run the Producer script.
8- Run the Consumer script.
