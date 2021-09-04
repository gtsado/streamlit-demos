# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('San Fransisco Trees')
st.write('This app analyzes trees in San Francisco using data provided by [SF\'s Department of Public Works]'
         '(https://data.sfgov.org/City-Infrastructure/Street-Tree-List/tkzw-k3nq)')

trees = pd.read_csv('Street_Tree_List.csv')
trees.columns = map(str.lower, trees.columns)

trees_dbh_grouped = trees.groupby(['dbh']).agg(tree_count=('treeid', 'nunique'))
trees_dbh_grouped.sort_index(inplace=True)
trees_dbh_grouped = trees_dbh_grouped.iloc[0:101,:]
st.line_chart(trees_dbh_grouped)
st.bar_chart(trees_dbh_grouped)
st.area_chart(trees_dbh_grouped)

fig = px.histogram(data_frame=trees.sample(1000), x='dbh')

st.plotly_chart(fig)
