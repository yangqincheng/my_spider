from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        # init函数前后都要加两个_
        self.urls = url_manager.UrlManager()
        # urls:管理爬过的url和没有爬过的url
        self.downloader = html_downloader.HtmlDownloader()
        # downloader:根据url把页面保存成一个字符串
        self.parser = html_parser.HtmlParser()
        # parser:解析器，后面可以加上BeautifulSoup+正则来找要用的东西
        self.outputer = html_outputer.HtmlOutputer()
        # 输出内容

    def craw(self, root_url):
        count = 1
        # 计数
        self.urls.add_new_url(root_url)
        # 把未爬的url放进待爬取队列之中
        while self.urls.has_new_url():
            # 判断待爬取队列是否为空
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                html_cont = self.downloader.download(new_url)
                # 把当前url的内容以字符串的形式保留下来
                new_urls, new_data = self.parser.paser(new_url, html_cont)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1


            except:
                print('craw failed')
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
