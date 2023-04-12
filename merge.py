import pandas as pd
while 1:
    df1=pd.read_csv("in.csv")
    df2=pd.read_csv("out.csv")
    #df3=df1.merge(df2,on=["Name",""])
    intime=df1.index(2,"in_time")
    outtime=df2.index(2,"out_time")
    print(outtime)
    print(intime)


    df3 = pd.merge(df1, df2, on='Name')
    df3.set_index('Name', inplace=True)
    df3.to_csv("output.csv")



