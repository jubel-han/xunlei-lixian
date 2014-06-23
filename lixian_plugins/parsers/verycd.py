import urllib2
import re

from lixian_plugins.api import page_parser


def parse_links(html):
    html = re.search(r'<!--eMule begin-->.*?<!--eMule end-->', html, re.S).group()
    links = re.findall(r'value="([^"]+)"', html)
    return [x for x in links if x.startswith('ed2k://')]


def verycd_links(url):
    assert url.startswith('http://www.verycd.com/topics/'), url
    return parse_links(urllib2.urlopen(url).read())


@page_parser('http://www.verycd.com/topics/')
def extend_link(url):
    links = verycd_links(url)
    from lixian_hash_ed2k import parse_ed2k_file

    return [{'url': x, 'name': parse_ed2k_file(x)} for x in links]

