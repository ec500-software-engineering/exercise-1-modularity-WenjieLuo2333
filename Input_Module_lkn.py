# copyright @Kainan Liu @Wenjie Luo
def read_data(path):
    try:
        with open(path,'r') as f:
            time = []
            value = []
            data = f.readline().split()
            while data:
                if data:
                    value.append([float(data[0]),float(data[1]),float(data[2])])
                else:
                    print("Empty data file!\n")
                    return 2
                data = f.readline().split()
        print("Read data successfully\n")
        return value
    except:
        print("Error:No input data\n")

        
