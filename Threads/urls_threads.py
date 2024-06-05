import requests
import time
from threading import Thread
from common import FakeRequest
from multiprocessing.pool import ThreadPool

requests.get = FakeRequest

total = list()

def get_post_len(url):
    print("Fetching", url)
    post = requests.get(url).json()
    return len(post['body'])
    #total.append(len(post['body']))

def crawler():
    base = "https://jsonplaceholder.typicode.com/posts"
    urls = [ f'{base}/{num}' for num in range(1, 15) ]

    with ThreadPool() as pool:
        results = pool.map(get_post_len, urls)

    print(sum(results))

def main():
    start = time.time()
    crawler()
    print("=" * 30)
    print("Time taken :", time.time() - start)

if __name__ == "__main__":
    main()
