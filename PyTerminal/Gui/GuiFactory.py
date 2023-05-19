from PyTerminal.Sessions import SerialSession
from PyTerminal.Gui.SessionWindow import SessionsWindow


class PyTerminalFactory(object):
    def __init__(self, config=None):
        self.session_window = None
        self.sessions = []
        pass

    def create_session_window(self, main_window, config):
        self.session_window = SessionsWindow(main_window)

    def create_sessions(self, session_window, config_file=None):
        # TODO: add config parser and create script interface
        if config_file:
            configs = config_file
        for config in configs:
            self.sessions.append(SerialSession(session_window, config.info, config.scripts))