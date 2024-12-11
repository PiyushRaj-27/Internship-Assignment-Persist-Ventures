# Video Uploader and Instagram Downloader

This project is an asynchronous Python script for downloading videos from an Instagram profile and uploading them to a remote server. The script also creates posts for the uploaded videos via API.

## Features
- **Instagram Video Downloader**: Download videos from a specified Instagram profile using Instaloader.
- **Asynchronous Upload**: Efficiently upload videos to a server using a pre-signed URL.
- **Post Creation**: Create posts on the server after successful video uploads.
- **Progress Tracking**: Includes progress bars for both downloading and uploading.

## Prerequisites
1. Python 3.8+
2. An environment variable `FLICK_TOKEN` containing your API token.
3. Required Python libraries (see [Installation](#installation) below).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/video-uploader-instagram.git
   cd video-uploader-instagram
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API token:
   ```env
   FLICK_TOKEN=your_api_token_here
   ```

## Usage
### Command-Line Arguments
- `--username`: The Instagram username from which to download videos. Default is `NULLUSER` (no downloads).

### Run the Script
```bash
python main.py --username <instagram_username>
```
- Replace `<instagram_username>` with the target Instagram profile's username.
- Videos are stored in the `videos/` directory.

### Workflow
1. Downloads videos from the specified Instagram profile (if username is provided).
2. Processes each `.mp4` file in the `videos/` directory by:
   - Fetching a pre-signed upload URL.
   - Uploading the video.
   - Creating a post.
   - Deleting the local video file after successful upload.

## Project Structure
```plaintext
├── main.py              # Main script
├── videos/              # Directory for storing videos
├── .env                 # Environment variables file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## API Endpoints
1. **Get Upload URL**
   - Endpoint: `https://api.socialverseapp.com/posts/generate-upload-url`
   - Returns a pre-signed URL for uploading videos.

2. **Create Post**
   - Endpoint: `https://api.socialverseapp.com/posts`
   - Creates a post with the uploaded video details.

## Dependencies
- `aiohttp`: For asynchronous HTTP requests.
- `tqdm`: For progress bars.
- `instaloader`: For downloading videos from Instagram.
- `dotenv`: For managing environment variables.
- `os`, `asyncio`, `logging`, `argparse`: Standard Python libraries.

## Error Handling
- Logs errors with descriptive messages.
- Automatically skips files if processing fails.

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

