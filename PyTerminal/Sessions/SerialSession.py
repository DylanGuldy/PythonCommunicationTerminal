from tkinter import Tk
from tkinter import Frame
import serial
from PyTerminal.Sessions.Session import Session


class SerialSession(Session):

    def __init__(self, parent: Tk, connection_info: dict, scripts: list, **kwargs):
        super().__init__(parent, scripts)
        self.connection = serial()

    def listen_for_messages(self):
        # Threaded out to just listen for messages
        # listen for message
        message_bytes = self.connection.read_until(self.connection_info["termination_char"])
        super().on_message_receive_event(message_bytes.decode('utf-8'))


