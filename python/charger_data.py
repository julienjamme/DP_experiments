import pandas as pd
import os
import parametres as param

os.chdir(param.PATH)

capital_bike_share = pd.read_csv('data/capital_bike_share.csv')
capital_bike_share.head()
