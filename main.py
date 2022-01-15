import os
import sys
import urllib.request

def download(url:str, path:str):
    urllib.request.urlretrieve(url, path)

def init_database():
    print(os.path.abspath(os.path.dirname(__file__)))
    if not os.path.exists('database'):
        os.mkdir("database")

def download_word(word:str):
    word = word.lower()
    url_us = r'http://dict.youdao.com/dictvoice?type=0&audio=' + word
    url_en = r'http://dict.youdao.com/dictvoice?type=1&audio=' + word
    file_path_us = os.path.join("database", word + "_us.mp3")
    file_path_en = os.path.join("database", word + "_en.mp3")
    download(url_us, file_path_us)
    download(url_en, file_path_en)

if __name__ == "__main__":
    print(sys.argv)
    if (len(sys.argv) == 2):
        init_database()
        download_word(sys.argv[1])
    else:
        print("pls use like this: python main.py word")