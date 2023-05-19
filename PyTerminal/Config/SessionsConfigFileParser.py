import json
from PyTerminal.Sessions.SerialSession import SerialSession
from serial import SerialException
from importlib.machinery import SourceFileLoader
from os.path import isfile


class SessionConfigFileParser(object):
    def __init__(self, config_file):
        self.config_file = open(config_file, 'r')
        self.data = json.load(self.config_file)

    def create_sessions(self, tk_parent):
        return_sessions = []
        for session in self.data["Sessions"]:
            if "Serial" in session:
                try:
                    return_sessions.append(SerialSession(session["Serial"]["Name"], tk_parent, session["Serial"]))
                except SerialException:
                    # TODO Error reporting
                    print("Failed to create Serial Session")
            if "Eth" in session:
                pass
                # TODO
                # return_sessions.append(EthernetSession(session["Eth"]["Name"], tk_parent, session["Eth"]))
        return return_sessions

    def gather_scripts(self):
        return_scripts = []
        for script in self.data["Scripts"]:
            module = self._get_module_for_script(script)
            script_class = self._get_script_class_from_module(module, script)
            return_scripts.append(script_class)
        return return_scripts

    @staticmethod
    def _get_script_class_from_module(module, script):
        if not hasattr(module, script["ClassName"]):
            # TODO Error Handling
            print("No class fitting the given name: {} was found in {}".format(script["ClassName"],
                                                                               script["Location"]))
            raise AttributeError("No class fitting the given name: {} was found in {}".format(script["ClassName"],
                                                                                              script["Location"]))
        script_class = getattr(module, script["ClassName"])
        return script_class

    @staticmethod
    def _get_module_for_script(script):
        if not isfile(script["Location"]):
            # TODO Error Handling
            print("{} was not found as a valid file".format(script["Location"]))
            raise FileNotFoundError("{} was not found as a valid file".format(script["Location"]))
        module = SourceFileLoader(script["Location"]).load_module()
        return module

    def __del__(self):
        self.config_file.close()
