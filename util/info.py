from unidecode import unidecode
import praw
import json
import os
import random
import logging
import dotenv

dotenv.load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="TwineBot",
)

subreddits = [os.getenv('SUBREDDIT')]
post_dir = './data/post/'
comment_dir = './data/comment/'
tts_dir = './data/tts/'
screenshot_dir = './data/screenshot/'

def clearPreviousData():
    if os.path.exists(post_dir):
        for file in os.listdir(post_dir):
            os.remove(post_dir + file)
    else:
        os.makedirs(post_dir)

    if os.path.exists(comment_dir):
        for file in os.listdir(comment_dir):
            os.remove(comment_dir + file)
    else:
        os.makedirs(comment_dir)

    if os.path.exists(tts_dir):
        for file in os.listdir(tts_dir):
            os.remove(tts_dir + file)
    else:
        os.makedirs(tts_dir)

    if os.path.exists(screenshot_dir):
        for file in os.listdir(screenshot_dir):
            os.remove(screenshot_dir + file)
    else:
        os.makedirs(screenshot_dir)

def getPost():
    posts = []
    for subreddit in subreddits:
        for submission in reddit.subreddit(subreddit).hot(limit=100):
            if submission.stickied:
                continue
            if submission.over_18:
                continue
            posts.append(submission)

    if posts:
        random_post = random.choice(posts)
        title = unidecode(random_post.title)
        selftext = unidecode(random_post.selftext)
        post_json = {
            'id': random_post.id,
            'title': title,
            'selftext': selftext,
            'url': random_post.url,
            'score': random_post.score
        }
        with open(post_dir + "post" + '.json', 'w') as f:
            json.dump(post_json, f)
        logging.info("Gathered Post Successfully")
    else:
        logging.warning("No posts found")


        
def getComment():
    with open(post_dir + "post" + '.json', 'r') as f:
        post = json.load(f)

    submission = reddit.submission(id=post['id'])
    for comment in submission.comments.list()[:15]:
        body = unidecode(comment.body)
        if body == '[deleted]' or body == '[removed]':
            continue
        comment_json = {
            'id': comment.id,
            'body': body,
            'score': comment.score
        }
        with open(comment_dir + comment.id + '.json', 'w') as f:
            json.dump(comment_json, f)
        logging.info(f"Gathered Comment Successfully [{comment.id}]")
            
            
