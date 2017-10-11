import ggplot
from ggplot import *
import pandas as pd

df = pd.read_csv("/Users/apple/Krow/data/MSFT.csv")
#df['date'] = df['date'].map(lambda s: s.replace("-", "")).astype("datetime64")
df['date'] = df['date'].astype("datetime64")
print(df.head())
print(ggplot(aes(x='date', y='high'), data=df) + geom_line())

