

class SessionConfigFileParser(object):
    def __init__(self, config_file):
        self.config_file = open(config_file, 'r')

    def create_sessions(self):
        pass

    def gather_scripts(self):
        pass
    
    def __del__(self):
        self.config_file.close()