from googleapiclient.discovery import build

# -----------------------------
# Step 1: Your API key & Channel ID
# -----------------------------
api_key = 'AIzaSyD2mTSj7if6dJpoUwaXfHh5O9dmw3IE3fo'  # Replace with your YouTube Data API key
channel_id = 'UC4rlAVgAK0SGk-yTfe48Qpw'  # Replace with the channel ID you want

# -----------------------------
# Step 2: Build YouTube service
# -----------------------------
youtube = build('youtube', 'v3', developerKey=api_key)

# -----------------------------
# Step 3: Fetch latest 5 videos from the channel
# -----------------------------
search_request = youtube.search().list(
    part='snippet',
    channelId=channel_id,
    maxResults=5,
    order='date'
)
search_response = search_request.execute()

# -----------------------------
# Step 4: Extract video IDs
# -----------------------------
video_ids = []
for item in search_response['items']:
    # Make sure it's a video (not playlist or channel)
    if item['id']['kind'] == 'youtube#video':
        video_ids.append(item['id']['videoId'])

# -----------------------------
# Step 5: Fetch video details (duration, views, etc.)
# -----------------------------
video_request = youtube.videos().list(
    part='snippet,contentDetails,statistics',
    id=','.join(video_ids)
)
video_response = video_request.execute()

# -----------------------------
# Step 6: Print video details
# -----------------------------
for video in video_response['items']:
    print(f"Video ID: {video['id']}")
    print(f"Title: {video['snippet']['title']}")
    print(f"Description: {video['snippet']['description']}")
    print(f"Published At: {video['snippet']['publishedAt']}")
    print(f"Duration: {video['contentDetails']['duration']}")
    print(f"Views: {video['statistics'].get('viewCount', 'N/A')}")
    print("-" * 50)
