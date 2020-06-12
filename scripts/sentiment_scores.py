# Import necessary modules

# !pip install vaderSentiment
# !pip install fastparquet
# !pip install tqdm


import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import dask.dataframe as dd
from fastparquet import ParquetFile
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import nltk
import json
from nltk.corpus import wordnet 
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from sqlalchemy import Table, Column, Integer, String, MetaData


pd.set_option('display.max_columns', None)


#########
# Load dask dataframe
def load_dask():
  reviews = dd.read_parquet('https://tally-ai-dspt3.s3.amazonaws.com/yelp-restaurants/reviews.parquet.gzip')
  return reviews

#####
df = load_dask()
df.head(3)


# Create the sentiment analysis function
def sentiment_score(comment):
    analyser = SentimentIntensityAnalyzer()
    
    x = 0
    score = analyser.polarity_scores(comment)
    x = x + score['pos']
    x = x + score['compound']
    x = x - score['neg'] 
    
    return x

df['review_score'] = df['text'].apply(sentiment_score)
df.head(3)

#set up sentiment_score max_columns
review_sentiment_cols = ['review_id', 'business_id', 'review_score']

#create sentiment table
reviewSentiment = df[review_sentiment_cols]
reviewSentiment.head(1)


#add tqdm (also add directly to database)
# making new dataframe for the scores
scores_col = ['text', 'business_id', 'review_id']
scores = df[scores_col]
scores = scores.compute()
scores = scores[scores['business_id'] == 'S9RoY_Smsh0a2JPo90bkdg']# just work with one popular cafe

#############################
#harsh attempt at scores table

def sentiment_score(sentence):
	# Create a SentimentIntensityAnalyzer object. 
	sid_obj = SentimentIntensityAnalyzer()
	# polarity_scores method of SentimentIntensityAnalyzer oject gives a sentiment dictionary. which contains pos, neg, neu, and compound scores. 
	sentiment_dict = sid_obj.polarity_scores(sentence)
	return sentiment_dict
def get_sentiment(review_list):
	all_sentiments = []
	compounds = []
	if len(review_list) > 0:
		for review in review_list:
			score = sentiment_score(review)
			all_sentiments.append(score)
	if len(all_sentiments) > 0:
		for sentiment_dict in all_sentiments:
			compound = sentiment_dict['compound']
			compounds.append(compound)
	if len(compounds) > 0:
		avg_sentiment = sum(compounds) / len(compounds)
	else:
		avg_sentiment = None
	return avg_sentiment
def get_subject_review_scores(review_list):
  if len(review_list) > 0:
    sub_sentiment_score = round((get_sentiment(review_list))*150)
  elif sub_sentiment_score < 0:
    sub_sentiment_score = 0
  else:
    sub_sentiment_score = 75
  return sub_sentiment_score

def sentimental_analysis(df):
  # Create a SentimentIntensityAnalyzer object. 
  sid_obj = SentimentIntensityAnalyzer()
  # extract_subject_related_words
  df['text'] = df['text'].apply(lambda x:" ".join(re.findall("[a-zA-Z]+", x)))
  df['cleaned'] = df['text'].apply(tokenizer)
  df['words_related_to_food'] = df['cleaned'].apply(related_to_food)
  df['food_review_list'] = df[df['words_related_to_food'].map(len) > 1]['text'].tolist()
  df['food_score'] = df['food_review_list'].apply(get_subject_review_scores)
  df['words_related_to_service'] = df['cleaned'].apply(related_to_service)
  df['service_review_list'] = df[df['words_related_to_service'].map(len) > 1]['text'].tolist()
  df['service_score'] = df['service_review_list'].apply(get_subject_review_scores)
  df['words_related_to_speed'] = df['cleaned'].apply(related_to_service)
  df['speed_review_list'] = df[df['words_related_to_speed'].map(len) > 1]['text'].tolist()
  df['speed_score'] = df['speed_review_list'].apply(get_subject_review_scores)
  df['words_related_to_price'] = df['cleaned'].apply(related_to_service)
  df['price_review_list'] = df[df['words_related_to_price'].map(len) > 1]['text'].tolist()
  df['price_score'] = df['price_review_list'].apply(get_subject_review_scores)
  df['words_related_to_ambience'] = df['cleaned'].apply(related_to_service)
  df['ambience_review_list'] = df[df['words_related_to_ambience'].map(len) > 1]['text'].tolist()
  df['ambience_score'] = df['ambience_review_list'].apply(get_subject_review_scores)
  df['words_related_to_experience'] = df['cleaned'].apply(related_to_service)
  df['experience_review_list'] = df[df['words_related_to_experience'].map(len) > 1]['text'].tolist()
  df['experience_score'] = df['experience_review_list'].apply(get_subject_review_scores)
  return df


# create sql table
meta = MetaData()

revSentimentScores = Table(
   'revSentimentScores', meta, 
   Column('buisness_id', String, primary_key = True), 
   Column('review_id', String), 
   Column('lastname', String),
   Column('')
)