# import os
# import asyncio
# import aiohttp
# import logging
# import argparse
# from instaloader import Instaloader, Profile
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from tqdm.asyncio import tqdm_asyncio
# from tqdm import tqdm
# from dotenv import load_dotenv

# load_dotenv()
# # Configure logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Constants
# FLIC_TOKEN = os.getenv('FLICK_TOKEN')  # Replace with your Flic-Token
# UPLOAD_URL_ENDPOINT = "https://api.socialverseapp.com/posts/generate-upload-url"
# CREATE_POST_ENDPOINT = "https://api.socialverseapp.com/posts"
# VIDEOS_DIR = "videos"


# # API Helpers
# async def get_upload_url(session, title):
#     """Fetch the pre-signed upload URL from the API."""
#     headers = {
#         "Flic-Token": FLIC_TOKEN,
#         "Content-Type": "application/json",
#     }
#     async with session.get(UPLOAD_URL_ENDPOINT, headers=headers) as response:
#         if response.status != 200:
#             raise Exception(f"Failed to get upload URL: {await response.text()}")
#         data = await response.json()
#         return data["upload_url"], data["hash"]


# async def upload_video(session, upload_url, file_path):
#     """Upload the video using the pre-signed URL."""
#     with open(file_path, "rb") as file:
#         with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Uploading {os.path.basename(file_path)}") as pbar:
#             async with session.put(upload_url, data=file) as response:
#                 if response.status not in (200, 201):
#                     raise Exception(f"Failed to upload video: {await response.text()}")
#                 pbar.update(os.path.getsize(file_path))
#                 logging.info(f"Uploaded video: {file_path}")


# async def create_post(session, title, hash_value, category_id=1):
#     """Create a post after uploading the video."""
#     headers = {
#         "Flic-Token": FLIC_TOKEN,
#         "Content-Type": "application/json",
#     }
#     payload = {
#         "title": title,
#         "hash": hash_value,
#         "is_available_in_public_feed": False,
#         "category_id": category_id,
#     }
#     async with session.post(CREATE_POST_ENDPOINT, headers=headers, json=payload) as response:
#         if response.status != 200:
#             raise Exception(f"Failed to create post: {await response.text()}")
#         logging.info("Post created successfully.")


# # File Monitoring
# class VideoHandler(FileSystemEventHandler):
#     def __init__(self, event_loop):
#         self.loop = event_loop

#     def on_created(self, event):
#         if event.src_path.endswith(".mp4"):
#             self.loop.create_task(process_video(event.src_path))


# # Video Processing
# async def process_video(file_path):
#     print(f"Processing the video")
#     """Process the video: upload and post creation."""
#     async with aiohttp.ClientSession() as session:
#         try:
#             # Fetch upload URL
#             logging.info(f"Fetching upload URL for {file_path}...")
#             upload_url, hash_value = await get_upload_url(session, title=os.path.basename(file_path))

#             # Upload video
#             logging.info(f"Uploading video: {file_path}")
#             await upload_video(session, upload_url, file_path)

#             # Create post
#             logging.info(f"Creating post for video: {file_path}")
#             await create_post(session, title=os.path.basename(file_path), hash_value=hash_value)

#             # Delete local file
#             os.remove(file_path)
#             logging.info(f"Deleted local file: {file_path}")
#         except Exception as e:
#             logging.error(f"Error processing {file_path}: {e}")


# # Instagram Video Downloading
# def download_instagram_videos(profile_name, download_dir):
#     """Download videos from an Instagram profile."""
#     loader = Instaloader()

#     try:
#         # Load profile
#         profile = Profile.from_username(loader.context, profile_name)

#         # Download only videos with a progress bar
#         posts = list(profile.get_posts())
#         with tqdm(total=1, desc="Downloading videos", unit="video") as pbar:
#             for post in posts[:1]:
#                 if post.is_video:
#                     loader.download_post(post, target=download_dir)
#                     pbar.update(1)
#     except Exception as e:
#         logging.error(f"Failed to download videos from {profile_name}: {e}")


# # Main Function
# async def main(username: str):
#     if not os.path.exists(VIDEOS_DIR):
#         os.makedirs(VIDEOS_DIR)
#     logging.info("Starting directory monitoring...")
#     loop = asyncio.get_event_loop()
#     event_handler = VideoHandler(loop)
#     observer = Observer()
#     observer.schedule(event_handler, path=VIDEOS_DIR, recursive=False)
#     observer.start()
    
#     instagram_profile = username 
#     if username!="NULLUSER":
#         logging.info(f"Downloading videos from Instagram profile: {instagram_profile}")
#         download_instagram_videos(instagram_profile, VIDEOS_DIR)

#     else:
#         logging.info(f"Please pass in username.")
    
#      # Start file monitoring
    

#     try:
#         while True:
#             await asyncio.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()


# if __name__ == "__main__":
#     try:
#         parser = argparse.ArgumentParser(description='Process some integers.')
#         parser.add_argument('--username', type= str, help="Username of the profile to download video from.", default="NULLUSER")
#         print(FLIC_TOKEN)
#         args = parser.parse_args()
#         asyncio.run(main(args.username))
#     except Exception as e:
#         logging.error(f"Application error: {e}")



# import os
# import asyncio
# import aiohttp
# import logging
# import argparse
# from instaloader import Instaloader, Profile
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from tqdm.asyncio import tqdm_asyncio
# from tqdm import tqdm
# from dotenv import load_dotenv
# from threading import Thread

# load_dotenv()

# # Configure logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Constants
# FLIC_TOKEN = os.getenv('FLICK_TOKEN')  # Replace with your Flic-Token
# UPLOAD_URL_ENDPOINT = "https://api.socialverseapp.com/posts/generate-upload-url"
# CREATE_POST_ENDPOINT = "https://api.socialverseapp.com/posts"
# VIDEOS_DIR = "videos"


# # API Helpers
# async def get_upload_url(session, title):
#     """Fetch the pre-signed upload URL from the API."""
#     headers = {
#         "Flic-Token": FLIC_TOKEN,
#         "Content-Type": "application/json",
#     }
#     async with session.get(UPLOAD_URL_ENDPOINT, headers=headers) as response:
#         if response.status != 200:
#             raise Exception(f"Failed to get upload URL: {await response.text()}")
#         data = await response.json()
#         return data["upload_url"], data["hash"]


# async def upload_video(session, upload_url, file_path):
#     """Upload the video using the pre-signed URL."""
#     with open(file_path, "rb") as file:
#         with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Uploading {os.path.basename(file_path)}") as pbar:
#             async with session.put(upload_url, data=file) as response:
#                 if response.status not in (200, 201):
#                     raise Exception(f"Failed to upload video: {await response.text()}")
#                 pbar.update(os.path.getsize(file_path))
#                 logging.info(f"Uploaded video: {file_path}")


# async def create_post(session, title, hash_value, category_id=1):
#     """Create a post after uploading the video."""
#     headers = {
#         "Flic-Token": FLIC_TOKEN,
#         "Content-Type": "application/json",
#     }
#     payload = {
#         "title": title,
#         "hash": hash_value,
#         "is_available_in_public_feed": False,
#         "category_id": category_id,
#     }
#     async with session.post(CREATE_POST_ENDPOINT, headers=headers, json=payload) as response:
#         if response.status != 200:
#             raise Exception(f"Failed to create post: {await response.text()}")
#         logging.info("Post created successfully.")


# # File Monitoring
# class VideoHandler(FileSystemEventHandler):
#     def __init__(self, event_loop):
#         self.loop = event_loop

#     def on_created(self, event):
#         if event.src_path.endswith(".mp4"):
#             logging.info(f"New file detected: {event.src_path}")
#             self.loop.call_soon_threadsafe(self.loop.create_task, process_video(event.src_path))


# # Video Processing
# async def process_video(file_path):
#     """Process the video: upload and post creation."""
#     async with aiohttp.ClientSession() as session:
#         try:
#             # Fetch upload URL
#             logging.info(f"Fetching upload URL for {file_path}...")
#             upload_url, hash_value = await get_upload_url(session, title=os.path.basename(file_path))

#             # Upload video
#             logging.info(f"Uploading video: {file_path}")
#             await upload_video(session, upload_url, file_path)

#             # Create post
#             logging.info(f"Creating post for video: {file_path}")
#             await create_post(session, title=os.path.basename(file_path), hash_value=hash_value)

#             # Delete local file
#             os.remove(file_path)
#             logging.info(f"Deleted local file: {file_path}")
#         except Exception as e:
#             logging.error(f"Error processing {file_path}: {e}")


# # Instagram Video Downloading
# def download_instagram_videos(profile_name, download_dir):
#     """Download videos from an Instagram profile."""
#     loader = Instaloader()

#     try:
#         # Load profile
#         profile = Profile.from_username(loader.context, profile_name)

#         # Download only videos with a progress bar
#         posts = list(profile.get_posts())
#         with tqdm(total=1, desc="Downloading videos", unit="video") as pbar:
#             for post in posts[:1]:
#                 if post.is_video:
#                     loader.download_post(post, target=download_dir)
#                     pbar.update(1)
#     except Exception as e:
#         logging.error(f"Failed to download videos from {profile_name}: {e}")


# # Run Observer in Thread
# def start_observer(loop):
#     event_handler = VideoHandler(loop)
#     observer = Observer()
#     observer.schedule(event_handler, path=VIDEOS_DIR, recursive=False)
#     observer.start()
#     try:
#         observer.join()
#     except KeyboardInterrupt:
#         observer.stop()
#     except Exception as e:
#         logging.error(f"Observer error: {e}")


# # Main Function
# async def main(username: str):
#     if not os.path.exists(VIDEOS_DIR):
#         os.makedirs(VIDEOS_DIR)

#     # Start the observer in a separate thread
#     loop = asyncio.get_event_loop()
#     observer_thread = Thread(target=start_observer, args=(loop,), daemon=True)
#     observer_thread.start()

#     # Download Instagram videos if username is provided
#     if username != "NULLUSER":
#         logging.info(f"Downloading videos from Instagram profile: {username}")
#         download_instagram_videos(username, VIDEOS_DIR)
#     else:
#         logging.info("No Instagram username provided.")

#     # Keep the main loop running
#     try:
#         while True:
#             await asyncio.sleep(1)
#     except KeyboardInterrupt:
#         logging.info("Shutting down...")


# if __name__ == "__main__":
#     try:
#         parser = argparse.ArgumentParser(description="Monitor a directory and process Instagram videos.")
#         parser.add_argument('--username', type=str, help="Instagram username to download videos from.", default="NULLUSER")
#         args = parser.parse_args()

#         asyncio.run(main(args.username))
#     except Exception as e:
#         logging.error(f"Application error: {e}")




import os
import asyncio
import aiohttp
import logging
import argparse
from instaloader import Instaloader, Profile
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
FLIC_TOKEN = os.getenv('FLICK_TOKEN')  # Replace with your Flic-Token
UPLOAD_URL_ENDPOINT = "https://api.socialverseapp.com/posts/generate-upload-url"
CREATE_POST_ENDPOINT = "https://api.socialverseapp.com/posts"
VIDEOS_DIR = "videos"

# API Helpers
async def get_upload_url(session, title):
    """Fetch the pre-signed upload URL from the API."""
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json",
    }
    async with session.get(UPLOAD_URL_ENDPOINT, headers=headers) as response:
        if response.status != 200:
            raise Exception(f"Failed to get upload URL: {await response.text()}")
        data = await response.json()
        return data["url"], data["hash"]

async def upload_video(session, upload_url, file_path):
    """Upload the video using the pre-signed URL."""
    with open(file_path, "rb") as file:
        with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Uploading {os.path.basename(file_path)}") as pbar:
            async with session.put(upload_url, data=file) as response:
                if response.status not in (200, 201):
                    raise Exception(f"Failed to upload video: {await response.text()}")
                pbar.update(os.path.getsize(file_path))
                logging.info(f"Uploaded video: {file_path}")

async def create_post(session, title, hash_value, category_id=1):
    """Create a post after uploading the video."""
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json",
    }
    payload = {
        "title": title,
        "hash": hash_value,
        "is_available_in_public_feed": False,
        "category_id": category_id,
    }
    async with session.post(CREATE_POST_ENDPOINT, headers=headers, json=payload) as response:
        if response.status != 200:
            raise Exception(f"Failed to create post: {await response.text()}")
        logging.info("Post created successfully.")

# Video Processing
async def process_video(file_path):
    """Process the video: upload and post creation."""
    async with aiohttp.ClientSession() as session:
        try:
            # Fetch upload URL
            logging.info(f"Fetching upload URL for {file_path}...")
            upload_url, hash_value = await get_upload_url(session, title=os.path.basename(file_path))
            print(f"Upload URL: {upload_url}")
            # Upload video
            logging.info(f"Uploading video: {file_path}")
            await upload_video(session, upload_url, file_path)

            # Create post
            logging.info(f"Creating post for video: {file_path}")
            await create_post(session, title=os.path.basename(file_path), hash_value=hash_value)

            # Delete local file
            os.remove(file_path)
            logging.info(f"Deleted local file: {file_path}")
        except Exception as e:
            logging.error(f"Error processing {file_path}: {e}")

# Instagram Video Downloading
def download_instagram_videos(profile_name, download_dir):
    """Download videos from an Instagram profile."""
    loader = Instaloader()

    try:
        # Load profile
        profile = Profile.from_username(loader.context, profile_name)

        # Download only videos with a progress bar
        posts = list(profile.get_posts())
        with tqdm(total=1, desc="Downloading videos", unit="video") as pbar:
            for post in posts[:1]:
                if post.is_video:
                    loader.download_post(post, target=download_dir)
                    pbar.update(1)
    except Exception as e:
        logging.error(f"Failed to download videos from {profile_name}: {e}")

# Main Function
async def main(username: str):
    if not os.path.exists(VIDEOS_DIR):
        os.makedirs(VIDEOS_DIR)

    # Download Instagram videos if username is provided
    if username != "NULLUSER":
        logging.info(f"Downloading videos from Instagram profile: {username}")
        download_instagram_videos(username, VIDEOS_DIR)

    # Process all videos in the directory
    video_files = [f for f in os.listdir(VIDEOS_DIR) if f.endswith(".mp4")]
    for video in video_files:
        await process_video(os.path.join(VIDEOS_DIR, video))

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Process Instagram videos and upload them.")
        parser.add_argument('--username', type=str, help="Instagram username to download videos from.", default="NULLUSER")
        args = parser.parse_args()

        asyncio.run(main(args.username))
    except Exception as e:
        logging.error(f"Application error: {e}")

