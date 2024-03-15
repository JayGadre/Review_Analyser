#Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import streamlit as st
import pathlib
import textwrap
import time

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

#Importing google API key

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.environ['GOOGLE_API_KEY'] = "#Enter your Gemini-api key here"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

#Fetching the dataset

ds = pd.read_csv("D:\Python Projects\Data_sets\Mod_Reviews_data.csv",encoding='latin1')
print(ds.head())
print(ds['Review_result'].value_counts())

#Prompt for Gemini api to classify the reviews

start = 0
while True:
  try : 
    for i in range(start,31000):
      Reviews = ds['REVIEW_CONTENT'][i]
      b = str( ' Classify ' + '"' + str(Reviews) + '"' + ' as Positive,  Negative or Neutral . Give output only in one word .' )
      response = model.generate_content(b).text
      ds.loc[i,'Review_result'] = response
      print(ds['Review_result'][i],i)
  except:
    print("Error") 
    start=i+1
    continue;
  else :
    break;

#Saving the file

ds = ds.to_csv('Data_sets\Mod_Reviews_data.csv',index=False)
a = ds[ds['Review_result']=='Negative'].index.values
print(ds['REVIEW_CONTENT'][a])


                              

