import time
import webbrowser

total_breaks = 3
break_count = 0
print("This program started on " + time.ctime())
while break_count < total_breaks:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=wBs4x9kjQP8&t=2096s")
    break_count = break_count + 1
