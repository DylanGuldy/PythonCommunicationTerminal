from tkinter import Frame

from PyTerminal.Sessions.SerialSession import Session


class SessionsWindow(object):
    def __init__(self, parent_window, initial_session_row_count=1, initial_session_col_count=1):
        self.window = Frame(parent_window)
        # 2D array that will be the Session Panes, these may be empty
        self.session_windows = [[1 for y in range(initial_session_col_count)] for x in range(initial_session_row_count)]

    def build_window(self, sessions: list[Session], session_row_count, session_col_count):
        for x in range(0, session_row_count):
            for y in range(0, session_col_count):
                self.session_windows[x][y] = sessions[x+y]
                self.session_windows[x][y].frame.grid(row=x, column=y, sticky="NSEW", ipadx=2, ipady=2)



