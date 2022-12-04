
import p3
import pandas as pd

df = pd.DataFrame(p3.cells, columns=['Area', 'White Pixel Count', 'Height', 'Width', 'Center_x', 'Center_y', 'Circle Area', 'Black Pixel Count'])

df.to_csv('data/example.csv')
