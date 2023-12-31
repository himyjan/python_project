# -*- coding: utf-8 -*-
"""Python課程數據分析報告SharedBikes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jorZ0rS-AFnViWr5XLYqjodZ0yTO0H71
"""

# 簡報 https://gamma.app/public/-Python-a0xs2he4jzt4veg
# !pip install

import numpy as np
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")

csv_data = pd.read_csv('https://storage.googleapis.com/kagglesdsdata/datasets/3925292/6826295/bike.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231101%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231101T225841Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=c644fcd8d1f0698fa1f59bfdb70f48db17fe1c83608b694fe0a4a106c224cd84078de5db684596b7107d74f8aa4ddc2163721dfca1220b4fb4d9f87b62a06ce020680fe8eee32378ea44c10e53a941a15d729330a298a8c7cf0f2ac45b95c797a9d0abe4499d3622025cc5803fba2d47599dcf40cd2a7ff7ccee08388dec1a48b21d3c9862571cd815b13eda826b5f069d128417fd78972872d9f48d4937e524df5e635206ea1050c4d42392f172527a7ff2b8cfd2b99360a9fa09d31c3cc920d4e8779ac178cac2191433b1d726453b944814b45e6256b80f9c5d38af28dbe0ae7500f6d66b07cd93736d25d37c57901b345971556dc7f0f77ba8418048d5e8')
json_data = pd.read_json('https://storage.googleapis.com/kagglesdsdata/datasets/3925292/6826295/Bike_Network.json?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231101%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231101T225752Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5f77b58543e7b3e59fe30f7caafd94deac43d5c271cb92c080519321310ad1e9f10ec7f1bb1133bdd0698201aaaa8797388c351e6d6ab7b34c62abdecc11246174326a32b229b9a8a9c3bf59cd8cbcd7b5357ebc5b940a99b8f0620b900b2c4f6f68787449cef2777d89e2818991238164efe14bfa3f0592e7a45063146589e7a88b2bbdb59a506fc2dc6f2704aae42ee50f95a5ae6921257ac1cf28d81e3a61bd111e89773d095ef3a6ba8f533302122b5bdf57e1595ed668399408a5a485b3542ea2b5e52046991ce5501e0576ff704d4e1f685fb532c2813d654cd26d8cd6d87fdee1a11a02e57aa4e4751d5cb89b76e30f28632acc7b03b284f117872a95')

csv_data.info()
csv_data.nunique()

json_data.info()

csv_data

csv_data.groupby('location/country').describe()

# df = csv_data.groupby('location/country').size().reset_index(name='count')
# ax = sns.barplot(x='location/country', y='count', data=df)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
# plt.subplots_adjust(wspace=0.5)
# plt.tight_layout()
# plt.show()

df = csv_data['location/country'].value_counts().to_frame().reset_index()
sns.set(rc={'figure.figsize':(15,5)})
ax = sns.barplot(x='index', y='location/country', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="right")
plt.tight_layout()
plt.show()

from plotly.express import scatter_geo
scatter_geo(data_frame=csv_data, lat='location/latitude', lon='location/longitude', hover_name='name', color='location/country', height=1000)

import seaborn as sns
import matplotlib.pyplot as plt

df = csv_data[['location/country', 'ebikes']].dropna()
df = df['location/country'].value_counts().to_frame().reset_index()
ax = sns.barplot(x='index', y='location/country', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="right")
plt.tight_layout()
plt.show()

sns.lineplot(data=csv_data, palette="tab10", linewidth=2.5)