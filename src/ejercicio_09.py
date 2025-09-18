import pandas as pd
import numpy as np

def ejercicio_09():
    data = np.array([
        [1000, 1200, 1100],
        [900, 950, 1050],
        [1500, 1400, 1600]
    ])
    df = pd.DataFrame(data, columns=['Q1', 'Q2', 'Q3'])
    print(df)
    print(df.dtypes)

if __name__ == "__main__":
    ejercicio_09()
