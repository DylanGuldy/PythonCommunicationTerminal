from abc import ABC, abstractmethod


class ScriptInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    def name(self, value):
        pass

    @name.getter
    def name(self):
        pass

    def run(self):
        pass


