#copyright @Wenjie Luo wjluo@bu.edu
import Input_Module_lkn
import storage
import Alert_module
import AiModule
import UserInterface_module
"""
Input Module
"""
Input_bp=Input_Module_lkn.read_data('./BP_data.txt')
Input_bo=Input_Module_lkn.read_data('./bo_data.txt')
Input_pulse=Input_Module_lkn.read_data('./pulse_data.txt')
"""
Storage Module
"""
storage_data=zip(Input_bo,Input_bp,Input_pulse)
data_save=list(storage_data)
stored_data = []
for i in data_save:
	tmp = storage.storage(i)
	stored_data.append(tmp)
"""
Alert Module   0-bo 1-bp 2-pul
"""
key_words=['bo','bp','pul']
alert_sys = Alert_module.Alert()
for i in range(3):
	for key in ['bo','bp','pul']:
		for j in stored_data:	
			data_in = [j.read(key),i]
			alert_sys.Alert_for_three_categories_input(data_in)
alert_sound = alert_sys.Alert_Output()
UserInterface_module.alert_out(alert_sound)

"""
AI Module
"""
ai_sys = AiModule.AiModule()

for j in stored_data:	
	ai_sys.input_check(Input_bo,Input_bp,Input_pulse)

predict_bo,predict_bp,predict_pul=ai_sys.predict()

"""
UI
"""
UserInterface_module.ai_output(predict_bo,predict_bp,predict_pul)