import urllib

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()

#urllib2是一个标准库，安装python之后就自带了，并且只在于python2中

#在python3中，已经把urllib，urllib2等的合并为一个包urllib了。