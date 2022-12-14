# Load packages (comments for more special stuff)

import pandas as pd
import pickle # un-pickling stuff from training notebook
from xgboost import XGBRegressor # we use a trained XGBoost model...and therefore need to load it
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import shap # add prediction explainability

import numpy as np
import itertools # we need that to flatten ohe.categories_ into one list for columns
import streamlit as st
from streamlit_shap import st_shap # wrapper to display nice shap viz in the app
import plotly.express as px
import time

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

##Streamlit interface:
st.set_page_config(page_title='Bank Marketing Project',
                    page_icon="🐙",
                    layout='wide')

