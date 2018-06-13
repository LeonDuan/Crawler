import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# constant
PROJECT_NAME = 'theverge'
HOMEPAGE = 'https://www.theverge.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

# Create worker threads (will die when main exists)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.setDaemon(True)
        t.start()


def work():
    while True:
        url = queue.get()  # get a url from queue
        Spider.crawl_page(threading.current_thread().name, url)  # crawl that url
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue. If so, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(f"{len(queued_links)} links in the queue")
        create_jobs()


queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
create_workers()
crawl()
