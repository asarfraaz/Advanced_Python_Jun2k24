from time import sleep
import random

class FakeRequest:
    def __init__(self, url):
        self.url = url
        random.seed(200 + int(url.split('/')[-1]))
        #print("called with", url)

    def json(self):
        with open("posts.csv") as FH:
            for line in FH:
                sleep(0.1 * random.random())
                if self.url in line:
                    return {'body': "-" * int(line.split(',')[1])}

