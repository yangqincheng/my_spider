class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        # 两个set（）集合，一个放爬过的url，一个放没爬过的url

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        # 如果url既不在旧集合也不在新集合，用add（）放进new集合

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0
        # 判断new集合是否为空

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        # 获取即将要爬取的url，并且把它放进old集合
        # pop（）函数是set（）集合的随机删除函数，随机选一个元素返回
