from tkinter import Tk
from tkinter import scrolledtext
from tkinter import Frame
from PyTerminal.Events.SendReceiveEventHandler import SendReceiveMessageEvent


class Session(object):

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.getter
    def name(self):
        return self.__name

    def __init__(self, name, parent_tk: Tk, **kwargs):
        # Will hold the window for this class
        self.frame = Frame()

        # This is where we'd make a serial session IF I HAD ONE
        # self.connection = serial.Serial(connection_info)

        self.__name = name

        # For anything that wants to sub to when we get an event
        self.ReceiveMessageEvent = SendReceiveMessageEvent()

        self.session_text = scrolledtext.ScrolledText(self.frame)
        self.session_text.pack()
        self.session_text.config(state="disabled")

    def create_window(self, parent_window):
        self.frame = Frame(parent_window)

    def add_script(self, new_script):
        # TODO: I think scripts might need reflection or something
        #  Want to be able to pull in any ol' py script to operate on sessions
        self.__scripts.append(new_script)

    def del_script(self, del_script):
        self.__scripts.remove(del_script)

    # Threaded out to just listen for messages
    def listen_for_messages(self):
        pass
        # listen for message
        ##message_bytes = self.connection.read_until(self.connection_info["termination_char"])
        ##self.on_message_receive_event(message_bytes.decode('utf-8'))

    ##########################
    # Message Receive events
    #   TODO: Maybe break this out into
    #       a class for reuse in eth session?
    ##########################
    def on_message_send_subscriber(self, message, *args, **kwargs):
        self._append_message_to_text_area(message)

    def on_message_receive_event(self, message):
        self.ReceiveMessageEvent.on_message_event(message, None, None)
        self._append_message_to_text_area(message)

    def add_message_receive_event_subscriber(self, method_to_call):
        self.ReceiveMessageEvent += method_to_call

    def unregister_message_receive_event_subscriber(self, method_to_remove):
        self.ReceiveMessageEvent -= method_to_remove

    ##########################
    # Private methods
    ##########################
    def _append_message_to_text_area(self, message):
        self.session_text.config(state='normal')
        self.session_text.insert('end', message)
        self.session_text.yview('end')
        self.session_text.config(state='disabled')
