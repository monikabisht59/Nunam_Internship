import pandas as pd

def readdata(name):
    return (pd.read_excel(name,sheet_name=None))

def writecsv(data,pattern,name):
    list_df = []
    for i in data.keys():
        if i.startswith(pattern):
            list_df.append(data[i])
    pd.concat(list_df).to_csv(name,index=False)


if __name__ == '__main__' :
    details = readdata('C:/Users/Monika Bisht/Desktop/data_source/data.xlsx')
    writecsv(details,'Detail_67_','detail.csv')
    writecsv(details,'DetailVol_67_','detailVol.csv')
    d2 = readdata('C:/Users/Monika Bisht/Desktop/data_source/data_1.xlsx')
    data = {**details,**d2}
    writecsv(data,'DetailTemp_67_','detailTemp.csv')
