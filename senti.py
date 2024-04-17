from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import csv
import emoji
limit = 10
count = 0
# perform vader sentiment ananlysis
def sentiment_sc(sentence):
    # store object
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is: ", sentiment_dict)
    print("Sentence is rated as ",sentiment_dict['pos']*100, "% positive")
    print("Sentence is rated as ",sentiment_dict['neg']*100, "% negative")
    print("Sentence is rated as ",sentiment_dict['neu']*100, "% neutral")
    

    # overall rating of the sentence
    print("Sentence is rated as:", end=" ")
    if sentiment_dict['compound'] >= 0.05:
        print("positive")
    elif sentiment_dict['compound'] <= -0.05:
        print("negative")
    else:
        print("neutral")
# perform TextBlob analysis for subjectivity score
def texblob(statement):
    senti = TextBlob(statement)
    senti = senti.sentiment
    print(senti)


# driver code
if __name__ == "__main__" :
    # Open the input file for reading
    file_path = 'combined_comments.csv'
    with open(file_path, "r", encoding='utf-8',newline='') as csvfile:
        # Read the entire content
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            count +=1
            print(row)
            sentiment_sc(row)
            result = ', '.join(row)
            print(result)
            texblob(result)

            if count >= limit:
                break




