from nltk.sentiment import SentimentIntensityAnalyzer
import ttkbootstrap as tb
sia = SentimentIntensityAnalyzer()
def analyze_sentiment():
    text=my_text.get()
    if not text:
        result.config(text="Please enter some text to analyze.", bootstyle='warning')
        return
    sentiment = sia.polarity_scores(text)
    #AI logic to determine the mood based on the compound score
    if sentiment['compound'] >= 0.05:
        res="You seem to be in a positive mood! keep going!"
        style='success'
    elif sentiment["compound"] <= -0.05:
        res="You seem to be in a negative mood. Under the weather mate?, hope you feel better soon!"
        style='danger'
    else:
        res="You seem to be in a neutral mood. Hope you have a good day!"
        style='info'
    result.config(text=res, bootstyle=style)

#GUI Building
root = tb.Window(title="Sentiment Analyzer",themename='vapor', size=(500,350))
label = tb.Label(root, text="Enter the text to analyze:",font=("Helvetica Standard", 20))
label.pack(pady=10)
#Input field
my_text = tb.Entry(root, width=50)
my_text.pack(pady=10)
#Button
btn = tb.Button(root, text="Mood check", bootstyle="primary", command=analyze_sentiment)
btn.pack(pady=20)
result = tb.Label(root, text="", font=("Helvetica", 12), wraplength=400)
result.pack(pady=20)
root.mainloop()