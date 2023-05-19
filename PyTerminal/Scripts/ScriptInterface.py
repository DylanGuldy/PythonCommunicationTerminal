from abc import ABC, abstractmethod


class ScriptInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @name.getter
    @abstractmethod
    def name(self):
        pass

    ######
    # A list of sessions needed by the script
    ######
    @property
    @abstractmethod
    def sessions(self):
        pass

    @sessions.setter
    @abstractmethod
    def sessions(self, value):
        pass

    @sessions.getter
    @abstractmethod
    def sessions(self):
        pass

    @abstractmethod
    def run(self):
        pass


