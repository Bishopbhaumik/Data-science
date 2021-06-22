import csv
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# with open("tcv.csv") as csv_file:
#     csv_reader=csv.DictReader(csv_file)
    # lang_counter=Counter()
    # # row=next(csv_reader)
    # # print(row['LanguagesWorkedWith'].split(";"))
    # for row in csv_reader:
    #     lang_counter.update(row['LanguagesWorkedWith'].split(";"))



data=pd.read_csv("tcv.csv")
ids=data["Responder_id"]
lan=data["LanguagesWorkedWith"]


lang_counter=Counter()
for response in lan:
    lang_counter.update(response.split(";"))

lang=[]
popular=[]


# print(lang_counter.most_common(10))
for item in lang_counter.most_common(15):
    lang.append(item[0])
    popular.append(item[1])

print(lang)
print("popularity------>")
print(popular)

lang.reverse()
popular.reverse()

plt.barh(lang,popular,color= '#419698')
plt.title("most popular  languages")
plt.ylabel("languages")
plt.xlabel("popularity")
plt.tight_layout()
plt.show()