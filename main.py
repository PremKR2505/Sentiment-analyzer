from nltk.sentiment import SentimentIntensityAnalyzer
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)
text= str(input("Enter the text to analyze: "))
sentiment = analyze_sentiment(text)
print("Sentiment Analysis Result:")
print(sentiment)
if sentiment['compound'] >= 0.05:
    print("You seem to be in a positive mood! keep going!")
elif sentiment["compound"] <= -0.05:
    print("You seem to be in a negative mood. Under the weather mate, hope you feel better soon!")
else:
    print("You seem to be in a neutral mood. Hope you have a good day!")