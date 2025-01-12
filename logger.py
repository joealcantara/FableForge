import time

class Logger:
    def __init__(self):
        self.log = open("log.txt", "w+")

    def timestamp(self):
        # seconds passed since epoch
        seconds = time.time()

        # convert the time in seconds since the epoch to a readable format
        lt = time.localtime(seconds)

        return ("[" + str(lt.tm_mday) + "-" + str(lt.tm_mon) + "-" + str(lt.tm_year) + " " +
            str(lt.tm_hour) + ":" + str(lt.tm_min) +"." + str(lt.tm_sec) + "] - ")

    def close_logger(self):
        self.log.write("Log closed")
        self.log.close()

    def write_to_log(self, message):
        self.log.write(self.timestamp() + message + "\n")
