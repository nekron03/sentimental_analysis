from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import csv
import emoji
import matplotlib.pyplot as plt

limit = 10
count = 0
polarity_comments = []  # List to store tuples of polarity score and comment text
positive_comments = []
negative_comments = []
neutral_comments = []

# Function to perform Vader sentiment analysis
def sentiment_sc(sentence):
    # Create SentimentIntensityAnalyzer object
    sid_obj = SentimentIntensityAnalyzer()
    # Perform sentiment analysis
    sentiment_dict = sid_obj.polarity_scores(sentence)
    # Append tuple of compound polarity score and comment text to polarity_comments list
    polarity_comments.append((sentiment_dict['compound'], sentence))
    print("Overall sentiment dictionary is: ", sentiment_dict)
    print("Sentence is rated as ",sentiment_dict['pos']*100, "% positive")
    print("Sentence is rated as ",sentiment_dict['neg']*100, "% negative")
    print("Sentence is rated as ",sentiment_dict['neu']*100, "% neutral")
        # overall rating of the sentence
    print("Sentence is rated as:", end=" ")
    if sentiment_dict['compound'] >= 0.05:
        print("positive")
        positive_comments.append(sentence)
    elif sentiment_dict['compound'] <= -0.05:
        print("negative")
        negative_comments.append(sentence)
    else:
        print("neutral")
        neutral_comments.append(sentence)

    

# Function to perform TextBlob analysis for subjectivity score
def texblob(statement):
    senti = TextBlob(statement)
    senti = senti.sentiment
    print(senti)

# Driver code
if __name__ == "__main__":
    # Open the input file for reading
    file_path = 'combined_comments.csv'
    with open(file_path, "r", encoding='utf-8', newline='') as csvfile:
        # Read the entire content
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            count += 1
            print(row)
            result = ', '.join(row)
            print(result)
            pol = sentiment_sc(result)
            
            texblob(result)
            if count >= limit:
                break

    # Calculate average polarity score
    if polarity_comments:
        average_polarity = sum(p[0] for p in polarity_comments) / len(polarity_comments)
        print("Average polarity score:", average_polarity)
        if average_polarity > 0.05:
            print("The Video has got a Positive response")
        elif average_polarity < -0.05:
            print("The Video has got a Negative response")
        else:
            print("The Video has got a Neutral response")

        # Find comment with most positive sentiment
        most_positive_comment = max(polarity_comments, key=lambda x: x[0])
        print("Most positive comment (Polarity Score: {}):".format(most_positive_comment[0]))
        print(most_positive_comment[1])

        # Find comment with most negative sentiment
        most_negative_comment = min(polarity_comments, key=lambda x: x[0])
        print("Most negative comment (Polarity Score: {}):".format(most_negative_comment[0]))
        print(most_negative_comment[1])

    else:
        print("No comments found.")

# print(positive_comments)
# print(f"length of pos comments: {len(positive_comments)}")

# print(negative_comments)
# print(f"length of neg comments: {len(negative_comments)}")

# print(neutral_comments)
# print(f"length of neu comments: {len(neutral_comments)}")

positive_count = len(positive_comments)
negative_count = len(negative_comments)
neutral_count = len(neutral_comments)

# labels and data for Bar chart
labels = ['Positive', 'Negative', 'Neutral']
comment_counts = [positive_count, negative_count, neutral_count]

# Creating bar chart
plt.bar(labels, comment_counts, color=['blue', 'red', 'grey'])

# Adding labels and title to the plot
plt.xlabel('Sentiment')
plt.ylabel('Comment Count')
plt.title('Sentiment Analysis of Comments')

# Displaying the chart
plt.show()

# labels and data for Bar chart
labels = ['Positive', 'Negative', 'Neutral']
comment_counts = [positive_count, negative_count, neutral_count]

plt.figure(figsize=(10, 6)) # setting size

# plotting pie chart
plt.pie(comment_counts, labels=labels)

# Displaying Pie Chart
plt.show()


