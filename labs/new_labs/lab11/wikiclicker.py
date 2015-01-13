from urllib import request
from bs4 import BeautifulSoup
import re

base = 'https://en.wikipedia.org'

def valid_link(ref, paragraph):
  if '.ogg' in ref:
    return False
  if ref[0] == '#':
    return False
  if 'Help:' in ref:
    return False
  if 'Wikipedia:' in ref:
    return False
  if 'For other uses, see' in paragraph:
    return False
  if 'This article is about' in paragraph:
    return False
  if 'id="coordinates"' in paragraph:
    return False
  for paren in re.findall(r'\([^)]*\)', paragraph):
    if ref in paren:
      return False
  return True

def valid_paragraph(paragraph):
  name = paragraph.name
  is_paragraph = name == 'p'
  is_list = name == 'ul'
  return is_paragraph or is_list

def get_first_link(wikipage):
  req = request.Request(base + wikipage, headers={'User-Agent' : 'Python Browser'})
  page = request.urlopen(req)
  data = page.read()
  soup = BeautifulSoup(data)
  soup = soup.find(id='mw-content-text')
  for paragraph in soup.find_all(valid_paragraph, recursive=False):
    for link in paragraph.find_all('a'):
      ref = link.get('href')
      if valid_link(str(ref), str(paragraph)):
        return ref
  return False

def get_random():
  req = request.Request(base + '/wiki/Special:Random', headers={'User-Agent' : 'Python Browser'})
  page = request.urlopen(req)
  url = page.geturl()
  url = url[len(base):]
  return url

def main():
  next_link = get_first_link(get_random())
  print(next_link)

if __name__ == '__main__':
  main()
