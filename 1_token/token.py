from urllib.request import urlretrieve
import os
import re

def download_data_file(url, file_name=None):
    """Download a file from the given URL."""
    if not os.path.exists("data"):
        os.makedirs("data")
    
    if file_name:
        filename = file_name
    else:
        filename = os.path.basename(url)

    file_path = f"data/{filename}"
    urlretrieve(url, file_path)
    return file_path


def parse_file(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        parse_text(text)
        
def parse_text(text):
    char_count = len(text)
    print(f"Number of characters in the file: {char_count}")
    words = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    preprocessed = [item.strip() for item in words if item.strip()]
    print(f"Number of words: {len(preprocessed)}")



# ----------------------------------------------------------------
url_1 = ("https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt")

url_2 = ('https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt')

parse_file(download_data_file(url_1))
# parse_file(download_data_file(url_2, 'tinyshakespeare.txt'))
# parse_text('Hello, world. Is this-- a test?')
