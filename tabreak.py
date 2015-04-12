''' Simple python program showing a video
in a webbrowser after a certain amount
of time.
'''
import webbrowser
import time

# our constant variables
number_of_breaks = 0
max_breaks = 3
intervall = 10
url = 'www.youtube.com/watch?v=pIgZ7gMze7A'

# loop until number in max_breaks is reached
while number_of_breaks < max_breaks:
    time.sleep(intervall)
    webbrowser.open(url)
    number_of_breaks += 1
