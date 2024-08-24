#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:59:14 2022

@author: ineisk
"""
# Ines KOUYATE's project - Python webapp

# Importation of functions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)


# Importation of the data file
total_data = pd.read_csv(
    "/Users/ineisk/Desktop/M2/Samia - Python web application/Project/Womens Clothing E-Commerce Reviews.csv")
print(total_data)  # to see the data

# Removal of useless variables
total_reviews = total_data.drop(
    ["Division Name", "Title", "Positive Feedback Count"], axis=1)
print(total_reviews)

# Creation of the webapp

st.title("SHEIN reviews analysis")
st.caption("Ines Kouyate's WebApp")
st.image("/Users/ineisk/Desktop/M2/Samia - Python web application/Project/SHEIN_Logo.jpg")

app_mode = st.sidebar.selectbox(
    'Tabs', ['Home', 'Explanatory analysis', 'Business recommandations'])

if app_mode == 'Home':
    st.subheader("Context")
    st.markdown("We want to analyse our marketing strategy and to do so we collected data of our website, about our products' reviews.")
    st.markdown("This dataset includes 23486 rows and 6 feature variables. Each row corresponds to a customer review, and includes the variables:")
    st.markdown(
        "Clothing ID: Integer Categorical variable that refers to the specific piece being reviewed")
    st.markdown("Age: Positive Integer variable of the reviewers age.")
    st.markdown("Review Text: String variable for the review body.")
    st.markdown(
        "Rating: Positive Ordinal Integer variable for the product score granted by the customer from 1 Worst, to 5 Best.")
    st.markdown(
        "Recommended IND: Binary variable stating where the customer recommends the product where 1 is recommended, 0 is not recommended.")
    st.markdown(
        "Department Name: Categorical name of the product department name.")
    st.markdown("Class Name: Categorical name of the product class name.")

    if st.checkbox('Show the dataset'):
        st.write(total_reviews.head())
    explanatorystep = st.button("Go to explanatory analysis")
    if explanatorystep:
        app_mode = 'Explanatory analysis'

if app_mode == 'Explanatory analysis':
    st.markdown(
        'Here is a global view of the distribution of our data thanks to these histograms')
    df = pd.DataFrame(
        total_reviews,
        columns=[
            'Age',
            'Recommended IND',
            'Rating',
            'Department Name'])
    df.hist()
    plt.show()
    st.pyplot()
    st.markdown(
        'Our customers gloabally seem satisfied with our products. Approximately 19 000 customers recommended them. Our main clientele is between 35-45 years old.')
    st.info('You can filter by clothes category')
    Category_selection = st.selectbox(
        'Clothes categories',
        total_reviews['Department Name'].unique())

    if Category_selection == 'Intimate':
        intimate_df = df[df["Department Name"] == "Intimate"]
        st.caption("Average rating")
        st.write(np.average(intimate_df["Rating"]))
        intimate_df.hist()
        plt.show()
        st.pyplot()

    if Category_selection == 'Dresses':
        dresses_df = df[df["Department Name"] == "Dresses"]
        st.caption("Average rating")
        st.write(np.average(dresses_df["Rating"]))
        dresses_df.hist()
        plt.show()
        st.pyplot()

    if Category_selection == 'Bottoms':
        bottoms_df = df[df["Department Name"] == "Bottoms"]
        st.caption("Average rating")
        st.write(np.average(bottoms_df["Rating"]))
        bottoms_df.hist()
        plt.show()
        st.pyplot()

    if Category_selection == 'Tops':
        tops_df = df[df["Department Name"] == "Tops"]
        st.caption("Average rating")
        st.write(np.average(tops_df["Rating"]))
        tops_df.hist()
        plt.show()
        st.pyplot()

    if Category_selection == 'Jackets':
        jackets_df = df[df["Department Name"] == "Jackets"]
        st.caption("Average rating")
        st.write(np.average(jackets_df["Rating"]))
        jackets_df.hist()
        plt.show()
        st.pyplot()

    if Category_selection == 'Trend':
        trend_df = df[df["Department Name"] == "Trend"]
        st.caption("Moyenne")
        st.write(np.average(trend_df["Rating"]))
        trend_df.hist()
        plt.show()
        st.pyplot()

if app_mode == 'Business recommandations':
    st.markdown('The feedbacks or our clients are **POSITIVE** !')
    st.image(
        "/Users/ineisk/Desktop/M2/Samia - Python web application/Project/tenor.gif")
    st.markdown(
        'However, the rating of our Trend products are lower than the average (3.8/5), we need to focus on improving them.')
