import pandas as pd

df = pd.DataFrame({"A":[1,2,3,4], "B":[5,6,7,8]})

# orient={'dict', 'list', 'series', 'split', 'records', 'index'}
df.to_dict()