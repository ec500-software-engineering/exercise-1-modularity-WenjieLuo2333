#copyright @Wenjie Luo
# It's the I/O documentation for Alert System

# Alert Sys
import numpy
class Alert():
    def __init__(self):
        self.bo = []
        self.bp = []
        self.pul = []
        self.average_list = [[] for i in range(3)]
        self.alert_flag1 = 0
        self.alert_flag2 = 0
        self.alert_flag3 = 0

    def exceed_threshold(self, data, tp):

        if tp == 0:
            if not 0.1 <= data <= 0.3:
                return 1
            else:
                return 0
        elif tp == 1:
            if not 80 <= data <= 120:
                return 2
            else:
                return 0
        else:
            if not 60 <= data <= 90:
                return 3
            else:
                return 0

    def Alert_Output(self):
        """
        Compare data with certain threthold
        send flags to user interface module.
        """
        return self.alert_flag1,self.alert_flag2,self.alert_flag3

    def Alert_for_three_categories_input(self, data_in):
        """
        get data for each type from database.
        format:
            (double value,int type)
        """
        if len(self.average_list[data_in[1]]) < 20:
            self.average_list[data_in[1]].append(float(data_in[0]))
        else:
            del (self.average_list[data_in[1]][0])
            self.average_list[data_in[1]].append(float(data_in[0]))

        if len(self.average_list[0]) >= 15 and self.exceed_threshold(numpy.mean(self.average_list[0]),0) != 0:
            self.alert_flag1 = self.exceed_threshold(numpy.mean(self.average_list[0]),0)
        if len(self.average_list[1]) >= 15 and self.exceed_threshold(numpy.mean(self.average_list[1]),1) != 0:
            self.alert_flag2 = self.exceed_threshold(numpy.mean(self.average_list[1]),1)
        if len(self.average_list[2]) >= 15 and self.exceed_threshold(numpy.mean(self.average_list[2]),2) != 0:
            self.alert_flag3 = self.exceed_threshold(numpy.mean(self.average_list[2]),2)


