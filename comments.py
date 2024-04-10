from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR
import csv

# Create YoutubeCommentDownloader instance
downloader = YoutubeCommentDownloader()
# Get comments from a YouTube video URL
video_url = 'https://www.youtube.com/watch?v=PjPe9uEeWjc'
comments_generator = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_POPULAR)

# Convert the generator to a list
comments_list = list(comments_generator)
print(comments_list)
text_values = [comment['text'] for comment in comments_list]

# Print the result
print(text_values)
# Check if comments_list is not empty
if text_values:
    # Specify the CSV file path
    csv_file_path = 'comment.csv'

    # Writing the comments to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        # Use csv.writer to handle writing multiple columns
        csv_writer = csv.writer(csv_file)      
        # Write data
        csv_writer.writerows([comment['text'].replace(',', ' ').replace(' ', ' ').strip()] for comment in comments_list)

else:
    print("No comments found.")
