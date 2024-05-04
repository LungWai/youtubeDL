from pytube import YouTube
import os

def download_mp4(link):
    try:
        # Define the download destination within a subfolder named "download"
        download_destination = os.path.join(os.getcwd(), "MP4")
        # Create the directory if it does not exist
        if not os.path.exists(download_destination):
            os.makedirs(download_destination)
        
        youtube_object = YouTube(link)
        highest_resolution_stream = youtube_object.streams.get_highest_resolution()
        # Specify the download destination in the download method
        highest_resolution_stream.download(output_path=download_destination)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

def download_mp3(link):
    try:
        # Define the download destination within a subfolder named "MP3"
        download_destination = os.path.join(os.getcwd(), "MP3")
        # Create the directory if it does not exist
        if not os.path.exists(download_destination):
            os.makedirs(download_destination)
        
        youtube_object = YouTube(link)
        audio_stream = youtube_object.streams.filter(only_audio=True).first()
        # Specify the download destination in the download method
        audio_stream.download(output_path=download_destination)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the audio: {e}")

if __name__ == "__main__":
    video_link = input("Enter the YouTube video URL: ")
    format_choice = input("Enter the format you want to download (mp4 : 1 / mp3 : 2): ").lower()
    if format_choice == "1":
        download_mp4(video_link)
    elif format_choice == "2":
        download_mp3(video_link)
    else:
        print("Invalid format selected. Please choose either mp4 or mp3.")
