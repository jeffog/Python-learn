import time
import webbrowser

c = 1

print ("This program started on " + time.ctime())

while c < 3: 
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=dyMXYE_50Ts")
    c = c + 1
