import pandas as pd
import matplotlib .pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")
dfe=pd.DataFrame({"Day":[1,2,3,4],"Visitors":[200,100,230,300],"Bounce_rate":[20,45,60,10]})

dfe.set_index("Day",inplace=True)

# print(df)
dfe.plot()
plt.show()