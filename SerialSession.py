import tkinter
from tkinter import Tk
from tkinter import scrolledtext
import serial
import socket
from SendReceiveEventHandler import SendAndReceiveMessageEvent


class SerialSession:
    def __init__(self, parent: Tk, connection_info: dict, scripts: list, **kwargs):
        self.frame = Tk.frame(parent)
        self.connection_info = connection_info
        # This is where we'd make a serial session IF I HAD ONE
        #self.connection = serial.Serial(connection_info)
        self.scripts = scripts

        # For anything that wants to sub to when we get an event
        self.ReceiveMessageEvent = SendAndReceiveMessageEvent()

        self.session_text = scrolledtext.ScrolledText(self.frame).pack()
        self.session_text.config(state="disabled")

    # Threaded out to just listen for messages
    def listen_for_messages(self):
        pass
        # listen for message
        ##message_bytes = self.connection.read_until(self.connection_info["termination_char"])
        ##self.on_message_receive_event(message_bytes.decode('utf-8'))

    def on_message_send_subscriber(self, message, *args, **kwargs):
        self._append_message_to_text_area(message)

    def on_message_receive_event(self, message):
        self.ReceiveMessageEvent.on_message_event(message, None, None)
        self._append_message_to_text_area(message)

    def add_message_receive_event_subscriber(self, method_to_call):
        self.ReceiveMessageEvent += method_to_call

    def unregister_message_receive_event_subscriber(self, method_to_remove):
        self.ReceiveMessageEvent -= method_to_remove

    def _append_message_to_text_area(self, message):
        self.session_text.config(state='normal')
        self.session_text.insert('end', message)
        self.session_text.yview('end')
        self.session_text.config(state='disabled')

