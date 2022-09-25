import pandas as pd

df=pd.read_csv('./s.csv')
attack={}
for i, df_i in df.iterrows():
    #print(df_i)
    df_list=df_i.str.split('\t')
    for f in df_list:
        
        if len(f)>18:
            t=[x[:-1] for x in f[-18:]]
            x=[0.5 if len(tt)==3 else tt for tt in t]
            #print(t)
            attack[f[-19]]=x[-18:]
        else:
            col=f

df=pd.DataFrame(attack, index=col).T
df=df.astype('float')
df=df.T
print(df)
col_name=[]
df_combine=pd.DataFrame()
for i in range(df.shape[0]):
 
    for j in range(df.shape[0]):
        if i<j:
            df_att=df.iloc[i]*df.iloc[j]
            df_combine=pd.concat([df_combine, df_att], axis=1)
            col_name.append((df.index[i], df.index[j]))

df=df_combine.T
df.index=pd.Index(col_name)
df=df.T

weakness=(df>1).astype('int').sum()
resistance=(df<1).astype('int').sum()
df=df.T
df.loc[:, 'weakness']=weakness

df.loc[:, 'resistance']=resistance
print(df.sort_values('weakness').head(10))
print(df.sort_values('weakness').tail(10))
print(df.sort_values('resistance').head(10))
print(df.sort_values('resistance').tail(10))
df.to_csv('attribute.csv')

