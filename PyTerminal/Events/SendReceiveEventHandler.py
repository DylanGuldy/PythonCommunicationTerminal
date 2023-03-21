
class SendReceiveEventHandler(object):
    def __init__(self):
        self.__RegisteredEventsToCall = []

    def __iadd__(self, event):
        self.__RegisteredEventsToCall.append(event)

    def __isub__(self, event):
        self.__RegisteredEventsToCall.remove(event)

    def __call__(self, message, *args, **kwargs):
        for event in self.__RegisteredEventsToCall:
            event(message, *args, **kwargs)


class SendReceiveMessageEvent(object):
    def __init__(self):
        self.OnMessageSendReceive = SendReceiveEventHandler()

    # Triggers the event
    def on_message_event(self, message, *args, **kwargs):
        self.OnMessageSendReceive(message, *args, **kwargs)

    def register_on_message_event(self, method_to_run):
        self.OnMessageSendReceive += method_to_run

    def unregister_on_message_event(self, method_to_remove):
        self.OnMessageSendReceive -= method_to_remove

