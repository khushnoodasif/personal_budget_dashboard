import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime

filepath = 'data/sample_data.csv'
df = pd.read_csv(filepath)
df.sample(10)