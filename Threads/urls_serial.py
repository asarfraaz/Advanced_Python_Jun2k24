import requests
import time
from common import FakeRequest

requests.get = FakeRequest

def get_post_len(url):
    print("Fetching", url)
    post = requests.get(url).json()
    return len(post['body'])

def crawler():
    base = "https://jsonplaceholder.typicode.com/posts"
    urls = [ f'{base}/{num}' for num in range(1, 15) ]

    total = list()
    for url in urls:
        print("Fetching", url)
        plen = get_post_len(url)
        total.append(plen)

    #total = map(get_post_len, urls)
    print(sum(total))

def main():
    start = time.time()
    crawler()
    print("=" * 30)
    print("Time taken :", time.time() - start)

if __name__ == "__main__":
    main()
