#copyright @Wenjie Luo wjluo@bu.edu
import queue
import Input_Thread
import Process_Thread
import UI_Thread
import time
"""
Input Thread
"""
def main():
	input_queue = queue.Queue()
	data_queue = queue.Queue()
	display_Alert_queue = queue.Queue()
	display_AI_queue = queue.Queue()
	In_Thread = Input_Thread.InputThread(input_queue,data_queue)

	Pro_Thread = Process_Thread.ProcessThread(data_queue,display_Alert_queue,display_AI_queue)
	UIThread=UI_Thread.UIThread(display_Alert_queue,display_AI_queue)
	In_Thread.start()
	Pro_Thread.start()
	UIThread.start()
	input_queue.put('input_data.txt')
	time.sleep(1)
	input_queue.put('exit')
	"""
	while True:
		cmd = input()
		if cmd == 'exit':
			input_queue.put(cmd)
			break
		else:
			input_queue.put(cmd)
	"""

if __name__ == '__main__':
	main()
