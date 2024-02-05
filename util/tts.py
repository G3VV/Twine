from handlers.tiktoktts import tts
import os
import random
import json
import logging

comment_dir = './data/comment/'
post_dir = './data/post/'
voices = [
    'en_us_001',
    'en_us_002',
    'en_us_006',
    'en_us_007',
    'en_us_009',
    'en_us_010',
    'en_uk_001',
    'en_uk_003', 
    'en_au_001',
    'en_au_002',    
]

def generateVoice():
    comment_files = os.listdir(comment_dir)
    random_voice = random.choice(voices)

    with open(post_dir + 'post.json', 'r') as f:
        data = json.load(f)
    tts(data['title'], random_voice, f"./data/tts/post.mp3")

    
    for comment_file in comment_files:
        random_voice = random.choice(voices)
        with open(comment_dir + comment_file, 'r') as f:
            data = json.load(f)
        
        tts(data['body'], random_voice, f"./data/tts/{data['id']}.mp3")
        logging.info(f"Generated TTS for {data['id']}")