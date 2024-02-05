![image](https://github.com/G3VV/Twine/assets/46306494/e24dbd8f-ba34-494a-b723-26fe92c8bccd)

# Twine

Twine is a Python-based tool that reads Reddit comments, takes screenshots of comments, converts them to text-to-speech (TTS), and stores the comments as JSON.

## Features

- Reads Reddit questions and extracts comments
- Takes screenshots of comments
- Converts comments to text-to-speech (TTS)
- Stores comments as JSON

## Installation

1. Clone the repository: `git clone https://github.com/G3VV/twine.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Navigate to the project directory: `cd twine`
2. Run the script: `python main.py`

## Configuration

You can customize the behavior of Twine by modifying the `.env` file. Here are some available options:

- `SUBREDDIT`: The subreddit to fetch comments from.
- `CLIENT_ID`: This is the Reddit API client ID.
- `CLIENT_SECRET`: This is the Reddit API client secret.

> You can find your client details on the [Reddit app panel](https://reddit.com/prefs/apps)
