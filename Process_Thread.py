#copyright @Wenjie Luo
import queue
import threading
import time
import Alert_module
import AiModule

class ProcessThread (threading.Thread):
	def __init__(self,input_queue,Alert_output_queue,AI_output_queue):
		threading.Thread.__init__(self)
		self.input_queue = input_queue
		self.Alert_output_queue = Alert_output_queue
		self.AI_output_queue = AI_output_queue
	def run(self):
		print('Process Thread Start')
		while True:
			try:
				Input = self.input_queue.get()
				if Input == 'exit':
					self.Alert_output_queue.put('exit')
					break
				else:
					alert_sys = Alert_module.Alert()
					for i in range(3):
						for j in Input:
							alert_sys.Alert_for_three_categories_input([j[i],i])
					
					alert_sound1,alert_sound2,alert_sound3 = alert_sys.Alert_Output()
					self.Alert_output_queue.put([alert_sound1,alert_sound2,alert_sound3])

					ai_sys = AiModule.AiModule()
					ai_input = list(zip(*Input))
					ai_sys.input_check(list(ai_input[0]),list(ai_input[1]),list(ai_input[2]))
					predict_bo,predict_bp,predict_pul=ai_sys.predict()
					self.AI_output_queue.put([predict_bo,predict_bp,predict_pul])
			except:
				time.sleep(1)
		print('Process Thread Stop')
