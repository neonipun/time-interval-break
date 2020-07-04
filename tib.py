from plyer import notification
import argparse
import os 
import sys
import time

# https://www.iconsdb.com/green-icons/time-icon.html
app_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), "time-32.ico")

def time_in_seconds(t):
    try:
        if 'm' in t:
            t = float(t[:-1]) * 60
        elif 's' in t:
            t = float(t[:-1])
        else:
            sys.exit('Wrong Time Format')
    except Exception as e:
        sys.exit('Exception: Wrong Time Format, '+str(e))
    return t

parser = argparse.ArgumentParser(description='Time interval breaks. Time Format: tm/ts. ex: 30s, 5m, 0.5m, 120s')
parser.add_argument('time_interval', metavar='t', help='Time interval in minutes or seconds.')
parser.add_argument('break_time', metavar='b', help='Break time in minutes or seconds.')
parser.add_argument('--intervals', type=int, default=999, help='Number of time interval breaks')
parser.add_argument('--message', default="Take a BREAK!!!", help='Custom break message.')
args = parser.parse_args()

time_interval = time_in_seconds(args.time_interval)
break_time = time_in_seconds(args.break_time)
title = f"Time Interval Break for {args.break_time}"
while args.intervals:
    time.sleep(time_interval)
    notification.notify(title=title, message=args.message, app_icon=app_icon, timeout=min(60, break_time+10))
    time.sleep(break_time)
    args.intervals -= 1
    print(f"{args.message}: {args.intervals} more intervals to go!. Time: {time.strftime('%I:%M:%S %p', time.localtime())}")