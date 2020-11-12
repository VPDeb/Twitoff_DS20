"""Prediction of Users based on tweet embedding"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .twitter import vectorize_tweet

def predict_user(user0_name, user1_name, hypo_tweet_text):
    """
    Determine return which user is more likely to say a hypothetical tweet.

    Example run: predict_user('elonmusk', 'nasa', 'tesla cars are rad')
    return either 0 (user0_name) or 1 (user1_name)
    """
    user0 = User.query.filter(User.name == user0_name).one() #nasa
    user1 = User.query.filter(User.name == user1_name).one() #elonmusk
    user0_vects = np.array([tweet.vect for tweet in user0.tweets]) #vectorizing nasa tweets
    user1_vects = np.array([tweet.vect for tweet in user1.tweets]) #vectorizing elonmusk tweets
    vects = np.vstack([user0_vects, user1_vects]) #stacks vectorized tables
    lables = np.concatenate([np.zeros(len(user0.tweets)), 
        np.ones(len(user1.tweets))]) #correspondign user label to vectorized tweets
    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text) #vectorizing sample tweet

    log_reg = LogisticRegression().fit(vects, labels)
    
    return log_reg.predit(hypo_tweet_vect.reshape(1, -1))