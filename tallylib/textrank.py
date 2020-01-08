import spacy
import pytextrank
import datetime

def getYelpReviews(business_id, 
                   starting_date, 
                   ending_date):
    pass

def yelpTrendyPhrases(business_id='Iq7NqQD-sESu3vr9iEGuTA', 
                      periods=12,
                      bagging_periods=3, 
                      days_per_period=30,
                      topk=10
                      ):    
    '''
    1. Get Yelp review texts
    2. Bag review texts within certain period, e.g. 6 peridos (180 days)
    3. Use Textrank to get scores
    4. Return JSON format for the frontend visualization
    '''
    # In Google Colab, run 6 period bagging:
    # CPU times: user 24.5 s, sys: 520 ms, total: 25 s
    # Wall time: 25 s
    # https://colab.research.google.com/drive/1r4uvFA6RNV35lO3JcYoO5Psz_EVhmNu0
    
    df_reviews = pd.DataFrame(columns=['date', 'text'])
    current_date = datetime.strptime('2018-11-30', '%Y-%m-%d')
    past_date = current_date - timedelta(days=days_per_period * periods -1)
    getYelpReviews(business_id, 
                   starting_date=current_date,
                   ending_date=past_date)

    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm/en_core_web_sm-2.2.5")
    # cutomize lemmatizer 
    # https://spacy.io/api/lemmatizer
    # ...
    textrank = pytextrank.TextRank()
    nlp.add_pipe(textrank.PipelineComponent, name="textrank", last=True)

    keywords = []
    for period in range(periods):
        # [starting_date, ending_date] = 180 days
        # or ending_date - staring_date = 179 days
        ending_date = current_date - timedelta(days=days_per_period * period)
        starting_date = ending_date - timedelta(days=days_per_period * bagging_periods -1)
        
        condition = ((df_reviews['date']>=starting_date) &
                    (df_reviews['date']<=ending_date))
        df_texts = df_reviews[condition][['text', 'date']]
        text = " ".join(df_texts['text'].to_list())
        doc = nlp(text)
        for i,p in enumerate(doc._.phrases):
            keywords.append([ending_date, p.rank, p.count, p.text])
            if i >= topk-1: break  
    del [df_reviews]
    df_keywords = pd.DataFrame(keywords,
        columns=['date', 'rank', 'count', 'keywords'])
    df_keywords = df_keywords['keywords'].value_counts().index[:topk]

