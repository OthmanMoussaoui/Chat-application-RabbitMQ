<h1 align="left">Chat Messaging using RabbitMQ</h1>

###

<div align="center">
  <img height="" src="https://www.rabbitmq.com/img/logo-rabbitmq.svg"  />
</div>

###

<p align="left">This repository contains the code for a simple chat messaging application that uses RabbitMQ as the message broker. The application allows users to send and receive messages in real-time using the publish-subscribe pattern.</p>

###

<h2 align="left">Getting Started</h2>

###

<p align="left">These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

###

<h2 align="left">Prerequisites</h2>

###

<p align="left">You will need to have <br>-Python3 : https://www.python.org/downloads/<br>-Tkinter : run in the command prompt  "pip install tk"<br>-RabbitMQ server if you want to run it on local host  follow instruction on https://www.rabbitmq.com/download.html<br>or you can use Cloudamqp to get your application deployed on Cloud and you can use the the application on different Machines <br>https://www.cloudamqp.com/</p>

###

<h2 align="left">Installing</h2>

###

<p align="left">Clone the repository to your local machine<br>Change directory into the cloned repository<br>Install the Prerequisites</p>

###

<h3 align="left">1-On local host</h3>

###

<p align="left">Start RabbitMQ server<br>sudo systemctl start rabbitmq-server<br>go to http://localhost:15672/ to find the management page.<br>change Url in otana.py/mehdi.py<br>to  url='localhost'</p>

###

<h3 align="left">2-On Cloudamqp</h3>

###

<div align="center">
  <img height="" src="https://www.pulumi.com/logos/pkg/cloudamqp.svg"  />
</div>

###

<p align="left">Create an account in https://www.cloudamqp.com/<br><br>Create your instance<br><br>Get your amqpUrl on CloudAMQP console page<br><br>put this Url on otana.py/mehdi.py <br>url='amqpurl'</p>

###

<h2 align="left">Run Application</h2>

###

<p align="left">Run Otana.py and Mehdi.py and start sending Messages <br>On localhost : do this in one machine <br>On CloudAMQP : you can use 2 machines</p>

###

<div align="center">
  <img height="300" src="https://raw.githubusercontent.com/OthmanMoussaoui/Chat-application-RabbitMQ/main/Connection.jpeg"  />
</div>

###

<div align="center">
  <img height="300" src="https://raw.githubusercontent.com/OthmanMoussaoui/Chat-application-RabbitMQ/main/TEST.jpeg"  />
</div>

###

<p align="left">For more details about Project check : https://github.com/OthmanMoussaoui/Chat-application-RabbitMQ/blob/main/RabbitMQ.pdf<br>For more details about RabbitMQ :<br>https://github.com/OthmanMoussaoui/Chat-application-RabbitMQ/blob/main/Getting_Started_with_RabbitMQ_and_CloudAMQP.pdf</p>

###
