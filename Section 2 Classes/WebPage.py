import urllib
from time import perf_counter
import urllib.request

class WebPage:
    def __init__(self, url):
        self._url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        self._url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None
    
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page
    
    @property
    def page_size(self):
        if self._page_size is None:
            self.download_page()
        return self._page_size
    
    @property
    def load_time_secs(self):
        if self._load_time_secs is None:
            self.download_page()
        return self._load_time_secs
    
    def download_page(self):
        print("Downloading the page..")
        ##watch course
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time

github = WebPage("https://www.google.com")

print(f"Page load time: {github.load_time_secs:.2f} seconds")
print(f"Page size: {github.page_size}")

print(f"Page load time: {github.load_time_secs:.2f} seconds")
print(f"Page size: {github.page_size}")

github.url = "https://github.com/"
print(f"Page load time: {github.load_time_secs:.2f} seconds")
print(f"Page size: {github.page_size}")

print(f"Page load time: {github.load_time_secs:.2f} seconds")
print(f"Page size: {github.page_size}")

urls = [
    "https://www.google.com",
    "https://github.com/",
    "https://www.instagram.com/"
]

for url in urls:
    page = WebPage(url)
    print(f"{url}:\t size: {page.page_size}\t load time: {page.load_time_secs:.2f} seconds;")