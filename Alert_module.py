#copyright @Wenjie Luo
# It's the I/O documentation for Alert System

# Alert Sys
import numpy
class Alert():
    def __init__(self):
        self.bo = []
        self.bp = []
        self.pul = []
        self.average_list = average_list = [[] for i in range(3)]
        self.alert_flag = -1

    def exceed_threshold(self, data, tp):
        if tp == 0:
            if not 0.1 <= data <= 0.3:
                return 0
            else:
                return -1
        elif tp == 1:
            if not 80 <= data <= 120:
                return 1
            else:
                return -1
        else:
            if not 60 <= data <= 90:
                return 2
            else:
                return -1

    def Alert_Output(self):
        """
        Compare data with certain threthold
        send flags to user interface module.
        """
        if self.alert_flag != -1:
            return self.alert_flag
        else:
            return -1

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

        if len(self.average_list[0]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[0]),'bo') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[data_in[1]]),'bo')
        if len(self.average_list[1]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[1]),'bp') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[data_in[1]]),'bp')
        if len(self.average_list[2]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[2]),'pul') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[data_in[1]]),'pul')


