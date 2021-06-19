import pandas as pd

def downsampledet(data,col):
    m = data.iloc[:, 4:].resample("T").mean()
    n = data.iloc[:, 0:4]
    res = pd.merge(n, m, how="inner", on=col)
    return res

def downsample(data,col):
    m = data.iloc[:, 2:].resample("T").mean()
    n = data.iloc[:, 0:2]
    res = pd.merge(n, m, how="inner", on=col)
    return res

def writecsv(data,name):
    data.to_csv(name)

def readdata(name,col):
    d = pd.read_csv(name,parse_dates = [col],index_col=0)
    d.drop(d.columns[0],axis = 1,inplace=True)
    return (d.set_index([col]))

if __name__ == '__main__':
    detail = readdata('C:/Users/Monika Bisht/Desktop/Nunam_Internship/Task_1/detail.csv', 'Absolute Time')
    data = downsampledet(detail, 'Absolute Time')
    writecsv(data,'detailDownsampled.csv')
    detailVol = readdata('C:/Users/Monika Bisht/Desktop/Nunam_Internship/Task_1/detailVol.csv', 'Realtime')
    data = downsample(detailVol, 'Realtime')
    writecsv(data,'detailVolDownsampled.csv')
    detailTemp = readdata('C:/Users/Monika Bisht/Desktop/Nunam_Internship/Task_1/detailTemp.csv', 'Realtime')
    data = downsample(detailTemp, 'Realtime')
    writecsv(data, 'detailTempDownsampled.csv')