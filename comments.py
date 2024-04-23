from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR
import csv

# Create YoutubeCommentDownloader instance
downloader = YoutubeCommentDownloader()

# List of YouTube video URLs
video_urls = [
    'https://www.youtube.com/watch?v=lEFYYpE_hds',
    'https://www.youtube.com/watch?v=h6potmDg0ek',  # Add more URLs as needed
]

# Initialize an empty list to store all comments
all_comments = []

# Iterate over each video URL
for video_url in video_urls:
    # Get comments from the current video
    comments_generator = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_POPULAR)
    # Extend the list of all comments with comments from this video
    all_comments.extend(list(comments_generator))

# Sort all comments by the number of likes in descending order
all_comments.sort(key=lambda x: x.get('votes', 0), reverse=True)

# Check if comments exist
if all_comments:
    # Specify the CSV file path
    csv_file_path = 'combined_comments.csv'

    # Writing the comments to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        # Use csv.writer to handle writing multiple columns
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(['Video URL', 'Comment Text', 'Likes'])
        # Write comments data
        for comment in all_comments:
            
            comment_text = comment['text'].replace('\n', ' ')
            csv_writer.writerow([comment.get('video_url', ''), comment_text, comment.get('votes', 0)])

    print("Comments written to", csv_file_path)
else:
    print("No comments found.")
