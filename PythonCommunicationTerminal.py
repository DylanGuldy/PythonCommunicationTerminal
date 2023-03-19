import tkinter
import tkinter as TK
from .SendReceiveEventHandler import SendAndReceiveMessageEvent
import tkinter.ttk as ttk


class ChatWindow(tkinter.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.SendMessageEvent = SendAndReceiveMessageEvent()
        self.ReceiveMessageEvent = SendAndReceiveMessageEvent()

    def run(self):
        self.master.mainloop()

def main():
    root = TK.Tk()
    root.resizable(True, True)
    chat = ChatWindow(root)
    chatWindow = ChatWindow(root)



if __name__ == "__main__":
    main()


#def send_input_area_text(self):
#   message = self.input_area.get('1.0', "end")
#   self.TriggerMessageSentEvent(message, NULL, NULL)
#   self.input_area.delete('1.0', "end")
#
#