# -*- coding: utf-8 -*-
# +
# 특징별 통계내기

import pandas as pd

df = pd.read_csv('04_hashed.csv')

# -

print(len(df['src_ip'].unique()))

import numpy as np
df['src_ip'][df['src_ip'].isnull()]

print(len(df['dst_ip'].unique()))

print(df['Proto'].unique())

print(df['src_port'].unique())
print(len(df['src_port'].unique()))

print(df['dst_port'].unique())
print(len(df['dst_port'].unique()))

print(df['Action'].unique())

print(df['src_country'].unique())
print(len(df['src_country'].unique()))

print(len(df['dst_country'].unique()))
print(df['dst_country'].unique())
