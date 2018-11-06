# Scrapy settings for properties project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'properties'

SPIDER_MODULES = ['properties.spiders']
NEWSPIDER_MODULE = 'properties.spiders'

# Crawl responsibly by identifying yourself (and your website) on
# the user-agent
#USER_AGENT = 'properties (+http://www.yourdomain.com)'

# Disable S3
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

# headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
           "Accept-Encoding": "gzip,deflate",
           "Accept-Language": "en-us,en;q=0.5",
           "Connection": "keep-alive",
           "Content-Length": "181",
           "Content-Type": "application/x-www-form-urlencoded",
           "Host": "login.sina.com.cn",
           "Keep-Alive": "115",
           "Referer": "http://login.sina.com.cn/hd/signin.php?entry=vblog&r=http%3A%2F%2Fvupload.you.video.sina.com.cn%2Fu.php%3Fm%3D1%26cate%3D0",
           "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16"}


#
# headers = {"Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#            "Accept-Charset", "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
#            "Accept-Encoding", "gzip,deflate",
#            "Accept-Language", "en-us,en;q=0.5",
#            "Connection", "keep-alive",
#            "Content-Length", "181",
#            "Content-Type", "application/x-www-form-urlencoded",
#            "Host", "login.sina.com.cn",
#            "Keep-Alive", "115",
#            "Referer", "http://login.sina.com.cn/hd/signin.php?entry=vblog&r=http%3A%2F%2Fvupload.you.video.sina.com.cn%2Fu.php%3Fm%3D1%26cate%3D0",
#            "User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16"}

