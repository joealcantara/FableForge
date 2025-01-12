class Logger:
    def __init__(self):
        self.log = open("log.txt", "w+")
        self.log.write("Log open\n")

    def close_logger(self):
        self.log.write("Log closed")
        self.log.close()

    def write_to_log(self, message):
        self.log.write(message + "\n")
