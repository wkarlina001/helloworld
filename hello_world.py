#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:29:43 2020

@author: wkarlina
"""

import streamlit as st

# subheader for sidebar
st.sidebar.subheader('Make Your Selections')

# option for user to capitalise input text
uppercase = st.sidebar.checkbox('Upper Case')

# option to determine the number of repeat of input text
repeat = st.sidebar.slider('How many repetition?', 1, 3, 1)

# option to reverse the order of input order
reverse = st.sidebar.checkbox('Reverse Order')


# define function for text processing of input text 
def process_text(input_split):
    # reverse the order of list if reverse option is chosen
    if reverse:
        input_split = list(reversed(input_split))

    # generate output based on number of repeat chosen    
    for i in range(len(input_split)):
        input_split[i] = input_split[i] * repeat

    # join list of lines to become string type
    join_text = '\n'.join(input_split)

    # capitalise input text if uppercase is chosen
    if uppercase:
        join_text = str.upper(join_text)

    # return join_text as string output
    return join_text


# input and output title
st.title('Input and Output Text')

# user can input multiline text
input_text = st.text_area('Input Text', 'Hello world.\nToday is a good day.')

# split the multiline text and return as list of lines
input_text_split = input_text.splitlines()

# option to generate output text based on selection 
if st.button('Generate Output'):
    # process text based on defined function and selections made by user
    output_text = process_text(input_text_split)

    # print output_text as multiline text
    st.text_area('Output Text', output_text)
