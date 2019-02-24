#copyright @Wenjie Luo, @Xiang Li
import threading
import time
class UIThread (threading.Thread):
	"""Thread to display information recieved from process thread"""
	def __init__(self,Alert_input_queue,AI_input_queue):
		threading.Thread.__init__(self)
		self.Alert_input_queue = Alert_input_queue
		self.AI_input_queue = AI_input_queue
	def run(self):
		print('UI Thread Start')
		while True:
			try:
				Input = self.Alert_input_queue.get()
				if Input == 'exit':
					break
				else:
					a1,a2,a3=Input[0],Input[1],Input[2]
					if a1 != 0:
						print("BO Alarm")
					if a2 != 0:
						print("BP Alarm")
					if a3 != 0:
						print("Pulse Alarm")
			except IOError:
				pass

			try:				
				if Input == 'exit':
					break
				else:
					Input = self.AI_input_queue.get()
					predBloodOxygen,predBloodPressure,prePulse=Input[0],Input[1],Input[2]
					print('predicted blood oxygen is: ' + str(predBloodOxygen))
					print('predicted blood pressure is: ' + str(predBloodPressure))
					print('predicted pulse is: ' + str(prePulse))
					print("")
			except IOError:
				time.sleep(1)
		print('UI Thread Stop')
