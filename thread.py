import time
import thread

def show_message(message):
	while True:
		print message
		time.sleep(1)

def start():
	msg1 = 'Hilo 1'
	msg2 = 'Hilo 2'

	thread.start_new_thread(show_message, (msg2,))
	thread.start_new_thread(show_message, (msg1,))
	x = raw_input('a')

start()