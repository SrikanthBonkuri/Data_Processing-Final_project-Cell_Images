
import p3
import pandas as pd

df = pd.DataFrame(p3.cells, columns=['Area', '% White'])

df.to_csv('data/example.csv')
