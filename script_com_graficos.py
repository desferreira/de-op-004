
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from sklearn.metrics import roc_curve, auc
from scipy.stats import loguniform

# Leitura da base
df_adv = pd.read_csv("db/advertising_full.csv", parse_dates=["Timestamp"])

# Cópia da base
df_adv_copy = df_adv.copy()

# Padronização das colunas para minúscula e sem espaços
df_adv_copy.columns = df_adv_copy.columns.str.lower().str.replace (' ','_')

# Visualização das 5 primeiras linhas
df_adv_copy.head()
print(df_adv_copy.head())

numeric_var = df_adv_copy[['daily_time_spent_on_site', 'age', 'area_income', 'daily_internet_usage']]

numeric_var.hist(bins=30, color = 'teal')

plt.suptitle("Distribuição das Variáveis Numéricas")

plt.show()
