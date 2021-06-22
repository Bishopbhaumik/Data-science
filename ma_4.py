import csv
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')



data=pd.read_csv("tcv.csv")
ids=data["Responder_id"]
lan=data["LanguagesWorkedWith"]

lang_counter=Counter()
for response in lan:
    lang_counter.update(response.split(";"))


lang=[]
popular=[]

for item in lang_counter.most_common(15):
    lang.append(item[0])
    popular.append(item[1])





plt.pie(popular,labels=lang)
plt.tight_layout()
plt.show()