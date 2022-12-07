
import p3
import pandas as pd

df = pd.DataFrame(p3.cells, columns=['Area', 'White Percent Area', 'Height', 'Width', 'Center_x', 'Center_y', 'Circle Area', 'Black Percent Circle'])

df.to_csv('data/example.csv')
