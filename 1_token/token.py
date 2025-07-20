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
        return text_to_tokens_with_stats(text)

def text_to_tokens(text):
    words = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    tokens = [item.strip() for item in words if item.strip()]
    return tokens

def text_to_tokens_with_stats(text):
    char_count = len(text)
    print(f"Number of characters in the file: {char_count}")
    tokens = text_to_tokens(text)
    print(f"Number of words: {len(tokens)}")
    return tokens

def build_token_ids(tokens):
    vocab_set = sorted(set(tokens))
    m_id_to_token = {token: i+1 for i, token in enumerate(vocab_set)}
    return m_id_to_token
    

# ----------------------------------------------------------------
url_1 = ("https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt")

url_2 = ('https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt')

arr = parse_file(download_data_file(url_1))
print(len(arr), ' total tokens')

tokens = text_to_tokens("The quick brown fox jumps over the lazy dog")
m_token_id_token = build_token_ids(tokens)

tokens = tokens[:100]
print('tokens: ', tokens)
print('by token ids: ', [m_token_id_token[x] for x in tokens])
