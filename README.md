### CleanTheBurgh - Detecting fake news in English and Italian

## Inspiration

Inspired by JP Morgan's challenge and Botometer which detects twitter bots, we created a similar tool that detects fake news, in both English and Italian.

## What it does

When user enter a link to online news, the programme will output the probability that it believes the real.

## How I built it

1. We first collected and parsed a large amount of data, including title, content and urls of fake news and real news. 
2. Then the data is fed to our Machine Learning model to train. In the end we have chosen and tuned a RandomForest Model for prediction. 
3. Also we logged down websites that usually post fake news in both English and Italian. This is used for cross-check.
4. For users, we created a web scraper which returns the news content when a link is provided. 
5. Lastly, we have a GUI for the tool.

## Challenges I ran into
1. Insufficient data for Deep Learning - used Random Forest instead, a supervised machine learning model
2. Some bugs with GUI not displaying image - fixed

## Accomplishments that I'm proud of

1. The tool works for both English and Italian.
2. The tool is working correctly - the accuracy on test data can go up to 80%

## What I learned

We have gone through data collection, ML, web scraper and GUI.

## What's next for CleanTheBurgh
1. Detection ability on fake pictures or pictures with wrong titles/captions
2. Ideally the news database and fake news domains need to be updated regularly in order to keep accuracy.
