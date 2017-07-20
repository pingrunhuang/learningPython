import time
import urllib.request
from threading import Thread

def get_responses_single_thread():
    urls = ['http://www.baidu.com', 'http://www.jd.com', 'http://www.alibaba.com', 'http://www.reddit.com']
    start = time.time()
    for url in urls:
        print(url)
        resp = urllib.request.urlopen(url)
        print(resp.getcode())
    print("Elapsed time: %s" % (time.time()-start))

class GetUrlThread(Thread):
    def __init__(self, url):
        super(GetUrlThread, self).__init__()
        self.url = url
    def run(self):
        response = urllib.request.urlopen(self.url)
        print(self.url, response.getcode())
def get_responses_multi_thread():
    urls = ['http://www.baidu.com', 'http://www.jd.com', 'http://www.alibaba.com', 'http://www.reddit.com']
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Elapsed time: %s" % (time.time()-start))


get_responses_single_thread()
get_responses_multi_thread()