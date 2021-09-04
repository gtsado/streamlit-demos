# This app graphs a line chart starting at a random number sampled from a normal distribution with mean 0 and variance 1
# The for loop keeps sampling new random numbers and then adds them to the sum
import streamlit as st
import time
import numpy as np

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1,1)
chart = st.line_chart(last_rows)

st.write(last_rows)

for i in range(1,101):
    new_rows = last_rows[-1,:] + np.random.randn(50,1).cumsum(axis=0)
    status_text.text(f'{i}% Complete')
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

st.write(new_rows)
progress_bar.empty()