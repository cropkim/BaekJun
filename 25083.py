import pandas as pd
URL = "https://raw.githubusercontent.com/cropkim/BaekJun/master/25083.txt"
data = pd.read_csv(URL)
# f = open("25083.txt","r")
# lines = f.readlines()
print(data)