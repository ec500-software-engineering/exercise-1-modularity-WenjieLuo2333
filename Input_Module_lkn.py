# copyright @Kainan Liu
def read_data(path):
    try:
        with open(path,'r') as f:
            time = []
            value = []
            data = f.readline().split()
            while data:
                if data:
                    time.append(data[0])
                    value.append(float(data[1]))
                    

                else:
                    print("Empty data file!\n")
                    return 2
                data = f.readline().split()
        print("Read data successfully\n")
        return value
    except:
        print("Error:No input data\n")

        
