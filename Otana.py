import pika
import time
from threading import Thread
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageDraw,ImageGrab,ImageTk

url = "amqps://kldqaapz:lqFOJ_g3ElJAq3vpYvR56ajj1Rkkog0t@albatross.rmq.cloudamqp.com/kldqaapz"
params = pika.URLParameters(url)
params.socket_timeout = 5


#fonction of receiver
def receiver():

    def callback(ch, method, propreties, body):
        msg_list.insert(END, "Mehdi -- "+ body.decode())
    
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='task_queue2')

    if (channel.basic_consume(queue='task_queue2', on_message_callback= callback, auto_ack=True)):
        msg_list.insert(END,"welcome again this is the box of messages... ")
        time.sleep(2)
        messagebox.showinfo("boom", " You'r online!")
        msg_list.delete(0,END)

    channel.start_consuming()
    connection.close()
    

#function of send
def send():
    connection = pika.BlockingConnection(params)
    #connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue1')

    live = entry_field.get()     
    msg_list.insert(END, "YOU -- " + live)
    
    channel.basic_publish(exchange='', routing_key='task_queue1', body= live)    
    connection.close()
    
#instancé  TK (jan)

jan = Tk()
jan.title("Otana")
jan.geometry("480x450")

#exit function
def exit():
    msg_list.delete(0,END)
    jan.destroy()

head = Frame(jan)
head.grid(row=0,column=0, pady = 5, padx = 5)
im = ImageTk.PhotoImage(Image.open("logo.png"))

labeln = Label(head, image=im)

labeln.grid(row=0,column=0, pady = 5, padx = 5,sticky='W')

lbl = Label(head, text="Hello this is an app to message using RabbitmQ", font=("Tekton Pro", 10))
lbl.grid(column=0, row=1,sticky='nsew')

#frame field text

messages_frame = Frame(jan)
scrollbar = Scrollbar(messages_frame) 
msg_list = Listbox(messages_frame, height=10, width=50, yscrollcommand=scrollbar.set)
scrollbar.grid(row=0,column=1, pady = 5, padx = 5)
msg_list.grid(row=0,column=0, pady = 5, padx = 5)
# msg_list.pack()
messages_frame.grid(row=1,column=0, pady = 5, padx = 5)

#FRAME FIELD button

botao_frame = Frame(jan)
lb = Label(botao_frame,text = "enter your message : ")
lb.grid(row=0,column=0, pady = 5, padx = 5)
entry_field = Entry(botao_frame, textvariable = '')
#entry_field.bind("<Return>", send)
entry_field.grid(row=0,column=1, pady = 5, padx = 5,sticky='nsew')

#exit button

send_button = Button(botao_frame, text= "Send", command= send)
send_button.grid(row=0,column=3, pady = 5, padx = 5)
bottonexit = Button(botao_frame, text = "exit", command= exit )
bottonexit.grid(row=0,column=4, pady = 5, padx = 5)
botao_frame.grid(row=2,column=0, pady = 5, padx = 5)
#FOTTER
footer = Frame(jan)
footer.grid(column=0, row=3)
lbl = Label(footer, text="Made by Othman Moussaoui", font=("Tekton Pro", 10))
lbl.grid(column=0, row=0,sticky='nsew')
lbl = Label(footer, text="Supervised by Pr:Lamia Karim", font=('Helvetica' , 10,'bold'))
lbl.grid(column=0, row=1,sticky='nsew')
lb = Label(footer,text="Thank you for testing ☺ hope you enjoy it ", font=("Tekton Pro", 10))
lb.grid(row=2,column=0, pady = 5, padx = 5)



receive_thread = Thread(target= receiver)
sender_thread = Thread(target= send)
receive_thread.start()
sender_thread.start()
jan.mainloop()