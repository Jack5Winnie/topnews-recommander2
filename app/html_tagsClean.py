import regex as re
import lxml.html

def strip_markdown(x):
    links_sub = re.sub(r'\[(.+)\]\([^\)]+\)', r'\1', x)
    bold_sub = re.sub(r'\*\*([^*]+)\*\*', r'\1', links_sub)
    emph_sub = re.sub(r'\*([^*]+)\*', r'\1', bold_sub)
    unic_sub = re.sub(r'\s', r' ' ,emph_sub)
    return unic_sub

def strip_html(x):
    return lxml.html.fromstring(x).text_content() if x else ''

def strip_all_tags(x):
    str = strip_markdown(strip_html(x))
    return str #.replace(u'\xa0', ' ')