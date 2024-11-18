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

![image](https://github.com/user-attachments/assets/99dc8560-0643-453a-8fe9-2a81eb49eb46)

**Prerequisites**:
------------------
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
   
![image](https://github.com/user-attachments/assets/5449b29d-b021-4bbb-bb6a-e1089fb65e24)

4- pip install pika

![image](https://github.com/user-attachments/assets/c08c2bf7-0dce-4487-9e9e-ad1626e79769)

5- Write the scripts.
6- Start the RabbitMQ Server.

![image](https://github.com/user-attachments/assets/a12a5c6a-722c-4128-b388-e37025e3c62e)

7- Run the Producer script in the termninal to observe the output.
8- Run the Consumer script in the terminal to observe the output.

![image](https://github.com/user-attachments/assets/15a4e855-e53f-4c8e-8889-7ffcd7d2a604)

