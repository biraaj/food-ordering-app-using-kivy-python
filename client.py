# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:23:16 2016

@author: biraaj
"""
#install_twisted_rector must be called before importing the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()


#A simple Client that send messages to the echo server
from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message(data)


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_message("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.app.print_message("connection failed")

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
textbox = TextInput(text="table no:",size_hint_y=0.8, multiline=False)
total=list()

class TestApp(App):
    connection = None
    #textbox = TextInput(text="table no:",size_hint_y=0.8, multiline=False)

    def build(self):
        self.connect_to_server()
        layout = BoxLayout(orientation='vertical')
        #textbox = TextInput(text="table no:",size_hint_y=0.8, multiline=False)

        
        
        # use a (r, g, b, a) tuple
        blue = (0, 2.5, 1.5, 2.5)
        red = (2.5, 1, 0, 1.5)
        green=(3,1,2,0)
        btn =   Button(text='Pasta        Rs.220', background_color=blue, font_size=100)
        btn2 =  Button(text='Burger      Rs.200', background_color=red, font_size=100)
        btn3 =  Button(text='Pizza        Rs.350', background_color=blue, font_size=100)
        btn4 =  Button(text='Veg-Rolls  Rs.150', background_color=red, font_size=100)
        btn5=Button(text='total',background_colour=green,font_size=100)        
        btn.bind(on_press=self.callback1)
        
        btn2.bind(on_press=self.callback2)
        
        btn3.bind(on_press=self.callback3)
        
        btn4.bind(on_press=self.callback4)
        btn5.bind(on_press=self.callback5)
        
        self.label = Label(text="", font_size='50sp')
        
        layout.add_widget(textbox)
        
        
        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        
        layout.add_widget(self.label)
        layout.add_widget(btn5)
        print textbox.text
        return layout
    def callback1(self, event):
        print("item added1")  # test
        self.label.text = "pasta selected"
        self.connection.write("pasta")
        self.connection.write(str("     "+textbox.text))
        total.append(220)
        
    def callback2(self, event):
        print("item added2")  # test
        self.label.text = "burger selected"
        self.connection.write("burger")
        self.connection.write(str("     "+textbox.text))
        total.append(200)
    def callback3(self, event):
        print("item added3")  # test
        self.label.text = "pizza selected"
        self.connection.write("pizza")
        self.connection.write(str("     "+textbox.text))
        total.append(350)
    def callback4(self, event):
        print("item added4")  # test
        self.label.text = "Veg-roll selected"
        self.connection.write("Veg-roll")
        self.connection.write(str("     "+textbox.text))
        total.append(150)
    def callback5(self,event):
        add=0
        for i in range(len(total)):
            add=add+total[i]
        wr=("total cost:=Rs")+str(add)
        self.label.text=wr
    def connect_to_server(self):
        reactor.connectTCP('localhost', 8000, EchoFactory(self))

    def on_connection(self, connection):
        #self.print_message(self.label.text)
        self.connection = connection

    '''def send_message(self, *args):
        msg = self.label.text
        if msg and self.connection:
            self.connection.write(str(self.label.text))'''
            
    def print_message(self, msg):
        self.label.text
if __name__ == '__main__':
	TestApp().run()