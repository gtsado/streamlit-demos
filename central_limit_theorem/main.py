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

st.title('Central Limit Theorem Demonstration')
st.subheader('An App by Godwin Tsado')
st.write('The Central Limit Theorem (CLT) states that if we randomly sample with replacement enough from any distribution'
         'then the distribution of the mean of our samples will approximate to a normal distribution')

probability_of_heads = st.number_input(label='Probability of Landing Heads', min_value=0.0, max_value=1.0, value=.5)
iterations = st.number_input(label='Number of Iterations', min_value=1, max_value=1000000000, value=1000)
flips = st.number_input(label='Number of Flips', min_value=1, max_value=20, value=10)
plot_title = st.text_input('Enter a title for your plot', value='My plot title')

# 1000 iterations of flipping a coin 1 time
binomial = np.random.binomial(flips,probability_of_heads,iterations)

means = [np.random.choice(binomial, 100, replace=True).mean() for i in range(1000)]

fig1, ax1 = plt.subplots()

ax1 = plt.hist(means)
plt.title(plot_title)
st.pyplot(fig1)