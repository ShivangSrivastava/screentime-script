
from argparse import ArgumentParser
from datetime import datetime, timedelta
import time


TODAY_LOG_FILE = "/tmp/screen_time_today_log.txt"
ALL_LOG_FILE = "/tmp/screen_time_all_log.txt"

# Creating files if not exist
try:
    with open(TODAY_LOG_FILE) as f:
        pass
except FileNotFoundError:
    with open(TODAY_LOG_FILE,"w") as f:
        pass
try:
    with open(ALL_LOG_FILE) as f:
        pass
except FileNotFoundError:
    with open(ALL_LOG_FILE,"w") as f:
        pass

parser = ArgumentParser()
parser.add_argument("-a",action="store_true",help="Display all screen time")
parser.add_argument("-r",action="store_true",help="Display raw screen time")
parser.add_argument("--init",action="store_true",help="Initiate the screen time")

class ScreenTime:
    def __init__(self, displayAll=False,raw=False) -> None:
        self.displayAll = displayAll
        self.raw = raw

    def start(self):
        with open(TODAY_LOG_FILE) as file:
            timestamps = file.readlines()
            if timestamps and not self.isNewDay(int(timestamps[0].strip("\n"))):
                return

        self._store(int(time.time()))


    def display(self):
        self._store(int(time.time()))

        with open(TODAY_LOG_FILE) as file:
            timestamps = file.readlines()
            if len(timestamps)>=1:
                first_ts = int(timestamps[0].strip("\n"))
                last_ts = int(timestamps[-1].strip("\n"))

        if self.displayAll:
            with open(ALL_LOG_FILE) as file:
                print("Screen time")
                lines = file.readlines()
                for line in lines:
                    print(line)
                if lines:
                    return
                print("No previous record\n")

        diff = datetime.fromtimestamp(last_ts) - datetime.fromtimestamp(first_ts)
        if self.raw:
            print(timedelta(seconds=diff.seconds))
            return
        print(f"Screen time of today : {timedelta(seconds=diff.seconds)}")

    def _store(self, timestamp:int):
        isNewDay = False
        with open(TODAY_LOG_FILE, "a+") as file:
            timestamps = file.readlines()
            if len(timestamps)>=1:
                try:
                    first_ts = int(timestamps[0].strip("\n"))
                    last_ts = int(timestamps[-1].strip("\n"))
                except ValueError:
                    return False
                isNewDay = self.isNewDay(last_ts)

        if isNewDay:
            diff = datetime.fromtimestamp(last_ts) - datetime.fromtimestamp(first_ts)

            with open(ALL_LOG_FILE,"a") as allLog:
                allLog.write(f"{datetime.fromtimestamp(last_ts).date()}: {timedelta(seconds=diff.seconds)}\n")

            with open(TODAY_LOG_FILE,"w") as file:
                file.writeline(f"{timestamp}")
        else:
            with open(TODAY_LOG_FILE,"a") as file:
                file.write(f"{timestamp}\n")
        return True

    def isNewDay(self,latest_ts:int) -> bool:
        return datetime.now()-datetime.fromtimestamp(latest_ts)>timedelta(1)

if __name__ == "__main__":
    args = parser.parse_args()
    screen_time = ScreenTime(args.a,args.r)
    if args.init:
        screen_time.start()
    else:
        screen_time.display()
