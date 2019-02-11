#copyright @Xiang Li
import random


class AiModule():
    def __init__(self):
        self.bo = []
        self.bp = []
        self.pulse = []

    def input_check(self, bloodOxygen, bloodPressure, pulse):
        """
        check the input type from the database in case there are some mistake data.
        """
        try:
            while True:
                for i, j, k in zip(bloodOxygen, bloodPressure, pulse):
                    self.bo.append(i)
                    self.bp.append(j)
                    self.pulse.append(k)

                print(self.bo)
                break

        except AttributeError:
            print('input type false')

    def predict(self):
        """
        predict blood oxygen, blood pressure, pulse for each type from database.
        format:
            (float value)
        """
        rand = random.randint(1, len(self.bo))
        predBloodOxygen = 0
        predBloodPressure = 0
        prePulse = 0
        for i in range(rand):
            predBloodOxygen += self.bo[i]/rand
            predBloodPressure += self.bp[i]/rand
            prePulse += self.pulse[i]/rand
        #print('predicted blood oxygen is: ' + str(predBloodOxygen))
        #print('predicted blood pressure is: ' + str(predBloodPressure))
        #print('predicted pulse is: ' + str(prePulse))
        return predBloodOxygen, predBloodPressure, prePulse