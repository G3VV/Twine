import logging
from util.info import getComment, getPost, clearPreviousData
from util.tts import generateVoice
from util.screenshot import takePostScreenshot, takeCommentScreenshot

logger = logging.getLogger()
logging.basicConfig(format='Twine » %(message)s', level=logging.INFO)

if __name__ == '__main__':
    clearPreviousData()
    getPost()
    getComment()
    generateVoice()
    takePostScreenshot()
    takeCommentScreenshot()