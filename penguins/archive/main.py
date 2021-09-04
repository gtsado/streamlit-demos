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
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time

st.title('Palmer\'s Penguins')
st.write('Use this app to explore bi-variate relationships in the Penguins data set')

file = st.file_uploader('Select your penguins CSV (default provided if none indicated)')

@st.cache
def load_data(data=None) -> object:
    """This function returns a dataframe"""
    time.sleep(5)
    if data:
        penguins = pd.read_csv(data)
    else:
        penguins = pd.read_csv('../penguins.csv')
        # st.stop()
    return penguins


penguins = load_data()

selections_1 = penguins.select_dtypes(float).columns
selections_2 = penguins.species.unique()
selections_3 = penguins.sex.unique()[:-1]

x = st.selectbox(label='X-axis variable', options=selections_1, index=0)
y = st.selectbox(label='Y-axis variable', options=selections_1, index=1)
gender = st.selectbox(label='Select a gender', options=selections_3)

# species = st.selectbox('What Species would you like to visualize', options=selections_2)

fig, ax = plt.subplots()

# ax.scatter(x = penguins['flipper_length_mm'], y = penguins['body_mass_g'], marker = penguins['species'])
# sns.scatterplot(data=penguins[penguins['species'] == species], x=x, y=y)
sns.scatterplot(data=penguins[penguins['sex'] == gender], x=x, y=y, style='species', hue='species')

ax.set_title(f'''Scatterplot of Palmer's Penguins''')
st.pyplot(fig)
