# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 18:46:18 2017

@author: Oliver Crosbie Higgs
"""

import praw
import csv
import datetime

reddit = praw.Reddit(user_agent=')',
                     client_id='', client_secret="",
                     username='', password='')

results = []

for submission in reddit.subreddit('worldnews').submissions(1498867200, 1501545599):
    results.append([submission.author, 
                    submission.title, 
                    submission.url.split("/")[2],
                    datetime.datetime.fromtimestamp(submission.created),
                    submission.score])

with open("reddit.csv", "w", newline='',encoding='utf8') as output:
    writer = csv.writer(output)
    writer.writerows(results)