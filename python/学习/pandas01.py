import pandas as pd
import numpy as np

# df = pd.DataFrame({'col one':[100,200],'col two':[300,400]})
# print(df)

# dd = pd.DataFrame(np.random.rand(4,8))
dd = pd.DataFrame(np.random.rand(4,8),columns=list('abcdefgh'))

print(dd)