# install_twisted_rector must be called before importing  and using the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()


from twisted.internet import reactor
from twisted.internet import protocol


class EchoProtocol(protocol.Protocol):
    def dataReceived(self, data):
        response = self.factory.app.handle_message(data)
        if response:
            self.transport.write(response)


class EchoFactory(protocol.Factory):
    protocol = EchoProtocol

    def __init__(self, app):
        self.app = app


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
storels=list()
storeds=dict()

class TwistedServerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        blue = (0, 0, 1.5, 2.5)
        red = (2.5, 0, 0, 1.5)
        self.label = Label(text="server started\n")
        reactor.listenTCP(8000, EchoFactory(self))
        btn =  Button(text='pasta done', background_color=blue, font_size=50)
        btn2 =  Button(text='burger done', background_color=red, font_size=50)
        btn3 =  Button(text='pizza done', background_color=blue, font_size=50)
        btn4 =  Button(text='veg-roll done', background_color=red, font_size=50)        
        btn.bind(on_press=self.callback1)
        
        btn2.bind(on_press=self.callback2)
        
        btn3.bind(on_press=self.callback3)
        
        btn4.bind(on_press=self.callback4)
        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(self.label)
        return layout

    def handle_message(self, msg):
        self.label.text = "received order:  %s" % msg
        storels.append(msg)
        storeds[msg]=storeds.get(msg,0)+1

        return msg
    def callback1(self, event):
        storeds["pasta     table no:1"]=storeds.get("pasta     table no:1",0)-1
        self.label.text = "delivered : pasta" 
        self.label.text = "pasta left to be delivered: %d"% storeds["pasta     table no:1"]
        
    def callback2(self, event):
        storeds["burger     table no:1"]=storeds.get("burger     table no:1",0)-1
        self.label.text = "delivered :burger"
        self.label.text = "burger left to be delivered: %d"% storeds["burger     table no:1"]
    def callback3(self, event):
        storeds["pizza     table no:1"]=storeds.get("pizza     table no:1",0)-1
        self.label.text = "delivered :pizza"
        self.label.text = "pizza left to be delivered: %d"% storeds["pizza     table no:1"]
    def callback4(self, event):
        storeds["Veg-roll     table no:1"]=storeds.get("Veg-roll     table no:1",0)-1
        self.label.text += "delivered :veg-rolls"
        self.label.text = "veg-rolls left to be delivered: %d"% storeds["Veg-roll     table no:1"]
   
        


if __name__ == '__main__':
    TwistedServerApp().run()