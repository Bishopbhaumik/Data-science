import pandas as pd
xyz_web={'day':[1,2,3,4,5,6],'visitors':[1000,700,6000,590,2300,4000],'Bounce_rate':[20,10,3,15,10,34]}
df=pd.DataFrame(xyz_web)
print(df.head(2))
print(df.tail(2))