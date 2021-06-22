import pandas as pd
df=pd.DataFrame({"Day":[1,2,3,4],"Visitors":[200,100,230,300],"Bounce_rate":[20,45,60,10]})
df=df.rename(columns={"Visitors":"users"})
print(df)