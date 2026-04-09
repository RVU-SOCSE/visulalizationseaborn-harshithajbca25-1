import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df2 = pd.read_csv(r"prog14b.csv")
sns.pairplot(df2)
plt.show()
