import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time
import pickle
import sklearn

st.title('Penguin Classifier')
st.write(
    'This app uses **six** inputs to predict the species of penguin using a model built on Palmer\'s Penguin\'s data')

penguins = pd.read_csv('penguins.csv')
penguins['sex'] = penguins.sex.str.title()
# print(penguins.head())

random_forest_pickle = open('random_forest_penguin.pickle', 'rb')
mapping_pickle = open('penguin_targets.pickle', 'rb')

random_forest = pickle.load(random_forest_pickle)
mapping = pickle.load(mapping_pickle)
random_forest_pickle.close()
mapping_pickle.close()

penguin_island = st.selectbox('Penguin Island', options=penguins.island.unique())
gender = st.selectbox('Gender', options=penguins.sex.unique())
bill_length = st.number_input('Bill Length (mm)', min_value=0)
bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
body_mass = st.number_input('Body Mass (g)', min_value=0)

island_biscoe, island_dream, island_torgersen = 0, 0, 0
if penguin_island == 'Biscoe':
    island_biscoe = 1
elif penguin_island == 'Dream':
    island_dream = 1
elif penguin_island == 'Torgersen':
    island_torgersen = 1

male, female = 0, 0
if gender == 'Male':
    male = 1
else:
    female = 1

prediction = random_forest.predict([[bill_length, bill_depth, flipper_length, body_mass, island_biscoe
                                        , island_dream, island_torgersen, female, male]])

prediction_probability = random_forest.predict_proba([[bill_length, bill_depth, flipper_length, body_mass, island_biscoe
                                                          , island_dream, island_torgersen, female, male]])[0][0]

prediction_species = mapping[prediction][0]
st.subheader('Prediction of your species')
st.write(
    f'We predict your penguin is of a {prediction_species} penguin with a probability of {prediction_probability: .0%}')

st.image('feature_importance.png')

st.write('Below are histograms for each continuous variable separated by penguin species.'
         'The verticle line represents the inputted value')

numerical_features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
numerical_inputs = [bill_length, bill_depth, flipper_length]

for i, feature in enumerate(numerical_features):
    fig, ax = plt.subplots()
    ax =  sns.displot(x=penguins[feature], hue=penguins['species'])
    plt.axvline(numerical_inputs[i], color='r', linewidth = 2)
    plt.title(f'{feature} by Species')
    st.pyplot(ax)
