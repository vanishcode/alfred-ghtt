#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -  *  - coding:UTF-8 -  *  -
import urllib2
from bs4 import BeautifulSoup
import re

base_url = u'http://bbs.ghtt.net/'
result = [u'<?xml version="1.0"?><items>']
plate_list = {
'xsrx':
'http://bbs.ghtt.net/forum-86-1.html',
'xyzx':
'http://bbs.ghtt.net/forum-1-1.html',
'swzl':
'http://bbs.ghtt.net/forum-146-1.html',
'1+1':
'http://bbs.ghtt.net/forum-183-1.html',
'byqz':
'http://bbs.ghtt.net/forum-99-1.html',
'jjjz':
'http://bbs.ghtt.net/forum-160-1.html',
'xyqh':
'http://bbs.ghtt.net/forum-112-1.html',
'mgzs':
'http://bbs.ghtt.net/forum-208-1.html',
'gsdt':
'http://bbs.ghtt.net/forum-93-1.html',
'wmtt':
'http://bbs.ghtt.net/forum-92-1.html',
'lxtx':
'http://bbs.ghtt.net/forum-207-1.html',
'dmtt':
'http://bbs.ghtt.net/forum-32-1.html',
'sssh':
'http://bbs.ghtt.net/forum-122-1.html',
'tdqy':
'http://bbs.ghtt.net/forum-100-1.html',
'yxhy':
'http://bbs.ghtt.net/forum-186-1.html',
'zyxs':
'http://bbs.ghtt.net/forum-114-1.html',
'kyzq':
'http://bbs.ghtt.net/forum-136-1.html',
'xxzy':
'http://bbs.ghtt.net/forum-135-1.html',
'wylx':
'http://bbs.ghtt.net/forum-119-1.html',
'rjly':
'http://bbs.ghtt.net/forum-103-1.html',
'yjns':
'http://bbs.ghtt.net/forum-104-1.html',
'PT':
'http://bbs.ghtt.net/forum-176-1.html',
'wysz':
'http://bbs.ghtt.net/forum-36-1.html',
'ysyy':
'http://bbs.ghtt.net/forum-113-1.html',
'shfw':
'http://bbs.ghtt.net/forum-203-1.html',
'smjy':
'http://bbs.ghtt.net/forum-204-1.html',
'qzqg':
'http://bbs.ghtt.net/forum-132-1.html',
'tzsc':
'http://bbs.ghtt.net/forum-88-1.html',
'zhty':
'http://bbs.ghtt.net/forum-9-1.html',
'lqsk':
'http://bbs.ghtt.net/forum-139-1.html',
'txzq':
'http://bbs.ghtt.net/forum-140-1.html',
'ghtt':
'http://bbs.ghtt.net/forum-82-1.html',
'zwzb':
'http://bbs.ghtt.net/forum-11-1.html'
}

def index(uid):
    index_response = urllib2.urlopen(base_url).read().decode('utf-8')
    if uid == u'hot':
        message = BeautifulSoup(index_response, "html.parser").find('div',id='portal_block_825_content')
    else:
        message = BeautifulSoup(index_response, "html.parser").find('div',id='portal_block_823_content')
    for m in message.find_all('li'):
        template = u'<item uid="%s" arg="%s"><title>%s</title><subtitle></subtitle><icon>icon.jpg</icon></item>' % (
            m.select('img + a')[0]['href'],
            m.select('img + a')[0]['href'],
            m.select('img + a')[0].get_text(),
            )
        result.append(template)
    result.append(u'</items>')
    print(''.join(result))

def plate(uid):
    plate_response = urllib2.urlopen(plate_list[uid]).read().decode('utf-8')
    message = BeautifulSoup(plate_response, "html.parser").find_all(id=re.compile('normalthread_'))
    for m in message:
        template = u'<item uid="%s" arg="%s"><title>%s</title><subtitle>查看: %s | 回复: %s | 创建日期: %s | 最后回复: %s</subtitle><icon>icon.jpg</icon></item>' % (
            m.select('a.s.xst')[0]['href'],
            m.select('a.s.xst')[0]['href'],
            m.select('a.s.xst')[0].get_text(),
            m.select('td.num > em')[0].get_text(),
            m.select('a.xi2')[0].get_text(),
            m.select('em > span')[0].get_text(),
            m.select('cite + em > a')[0].get_text()
            )
        result.append(template)
    result.append(u'</items>')
    print(''.join(result))

