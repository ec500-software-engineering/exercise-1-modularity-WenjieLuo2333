#copyright @Shilu Wu
#It's the I/O documentation for the User_Interface_system
#User Interface

def alert_out(alert_number):
	if alert_number == 0:
		print("OK")
	elif alert_number == 1:
		print("BO Alert!")
	elif alert_number == 2:
		print("BP Alert!")
	elif alert_number == 3:
		print("PUL Alert!")

def ai_output(predBloodOxygen,predBloodPressure,prePulse):
    print('predicted blood oxygen is: ' + str(predBloodOxygen))
    print('predicted blood pressure is: ' + str(predBloodPressure))
    print('predicted pulse is: ' + str(prePulse))