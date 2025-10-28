# Step 1: Install required packages
!pip install google-api-python-client youtube-transcript-api pandas --quiet

# Step 2: Import libraries
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import pandas as pd
import time

# Step 3: Set API key and channel ID
api_key = "AIzaSyD2mTSj7if6dJpoUwaXfHh5O9dmw3IE3fo"
channel_id = "UC4rlAVgAK0SGk-yTfe48Qpw"

# Step 4: Initialize YouTube API
youtube = build('youtube', 'v3', developerKey=api_key)

# Step 5: Get uploads playlist ID
channel_response = youtube.channels().list(
    part='contentDetails',
    id=channel_id
).execute()

uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Step 6: Fetch video IDs from uploads playlist
def get_videos_from_playlist(playlist_id, max_videos=50):
    video_ids = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token or len(video_ids) >= max_videos:
            break

    return video_ids[:max_videos]

video_ids = get_videos_from_playlist(uploads_playlist_id, max_videos=50)
print(f"Total video IDs fetched: {len(video_ids)}")

# Step 7: Fetch video metadata
def get_video_metadata(video_ids):
    all_data = []
    for vid in video_ids:
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics,status",
            id=vid
        )
        response = request.execute()
        for item in response['items']:
            data = {
                "videoId": item['id'],
                "title": item['snippet'].get('title'),
                "description": item['snippet'].get('description'),
                "publishedAt": item['snippet'].get('publishedAt'),
                "tags": item['snippet'].get('tags'),
                "categoryId": item['snippet'].get('categoryId'),
                "defaultLanguage": item['snippet'].get('defaultLanguage'),
                "defaultAudioLanguage": item['snippet'].get('defaultAudioLanguage'),
                "thumbnails": item['snippet']['thumbnails'],
                "duration": item['contentDetails'].get('duration'),
                "viewCount": item['statistics'].get('viewCount'),
                "likeCount": item['statistics'].get('likeCount'),
                "commentCount": item['statistics'].get('commentCount'),
                "privacyStatus": item['status'].get('privacyStatus'),
            }
            all_data.append(data)
        time.sleep(0.1)
    return all_data

video_metadata = get_video_metadata(video_ids)
print("Metadata fetched.")

# Step 8: Fetch transcripts reliably
def get_transcript_alternate(video_id):
    try:
        # Try English transcript first
        transcript_obj = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        transcript_text = " ".join([t['text'] for t in transcript_obj])
        return transcript_text, True
    except:
        # If English not available, try any transcript
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript_obj = transcript_list.find_transcript(transcript_list._transcripts.keys())
            transcript_text = " ".join([t['text'] for t in transcript_obj.fetch()])
            return transcript_text, True
        except:
            return None, False

# Step 9: Add transcript and availability to metadata
for video in video_metadata:
    vid = video['videoId']
    transcript, is_available = get_transcript_alternate(vid)
    video['transcript'] = transcript
    video['is_transcript_available'] = is_available
    time.sleep(0.1)

print("Transcripts fetched.")

# Step 10: Save to CSV
df = pd.DataFrame(video_metadata)
df.to_csv("youtube_channel_videos.csv", index=False)
print("CSV saved successfully!")

# Step 11: Display CSV in Colab
pd.set_option('display.max_rows', 50)  # Show all 50 videos
pd.set_option('display.max_colwidth', None)  # Show full transcript text
df
