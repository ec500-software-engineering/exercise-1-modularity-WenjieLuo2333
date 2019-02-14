#copyright @Wenjie Luo
import Input_Module_lkn
import queue
import threading
import time

class InputThread (threading.Thread):
	def __init__(self,input_queue,output_queue):
		threading.Thread.__init__(self)
		self.input_queue = input_queue
		self.output_queue = output_queue
		self.data = []
	def run(self):
		print("Input Thread Start")
		while True:
			try:
				Input = self.input_queue.get()
				if Input == 'exit':
					self.output_queue.put('exit')
					break
				else:
					self.data = Input_Module_lkn.read_data(Input)
					if self.data == None:
						print("Wrong Path!")
						continue
					self.output_queue.put(self.data)
			except:
				time.sleep(3)
		print('Input Thread Stop')
