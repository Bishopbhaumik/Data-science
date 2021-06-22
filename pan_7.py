import pandas as pd

ci = pd.read_csv("at.csv", index_col=0)

ci.to_html("edu.html")