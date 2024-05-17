
# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dataset:
df=pd.DataFrame({'x_values': range(1,101), 'y_values': np.random.randn(100)*15+range(1,101) })

print (df)


# plot
plt.plot( 'x_values', 'y_values', data=df, linestyle='none', marker='o')
plt.show()



