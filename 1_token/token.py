from urllib.request import urlretrieve

url = ("https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt")
file_path = "data/the-verdict.txt"
urlretrieve(url, file_path)
