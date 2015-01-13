import urllib
from urllib import request
from bs4 import BeautifulSoup
import re

#Based heavily on http://stackoverflow.com/questions/18916616/get-first-link-of-wikipedia-article-using-wikipedia-api

base = 'http://tvtropes.org'

def valid_link(link, current_page):
  ref = link.get('href')
  if 'twikilink' not in link.get('class'):
    return False
  if ref[0] == '#':
    return False
  if ref.endswith(current_page):
    return False
  if ref == base:
    return False
  # for paren in re.findall(r'\([^)]*\)', paragraph):
  #   if ref in paren:
  #     return False
  #print(base + ref)
  return True


def valid_paragraph(paragraph):
  name = paragraph.name
  return name in ['p', 'ul']

def get_first_link(wikipage):
  #print('Page: ', base + wikipage)
  req = request.Request(base + wikipage, headers={'User-Agent' : 'Python Browser'})
  page = request.urlopen(req)
  data = page.read()
  soup = BeautifulSoup(data)
  content = soup.find(id='wikitext')
  for link in content.find_all('a'):
    #print(link)
    if valid_link(link, wikipage):
      return link
  return False

def get_random():
  req = request.Request(base + '/pmwiki/randomitem.php?p=1', headers={'User-Agent' : 'Python Browser'})
  page = request.urlopen(req)
  url = page.geturl()
  url = url[len(base):]
  print(base + url)
  return url

def main():
  #visited = ['/wiki/New_Mexico_Institute_of_Mining_and_Technology']
  #visited = [get_random()]
  for visited in [get_random() for x in range(1)]:
    #visited = ['/wiki/' + visited]
    visited = [visited]
    while True:
      next_link = get_first_link(visited[-1])
      if next_link is False:
        print('Broke after {}.'.format(visited[-1]))
        break
      next_link = next_link.get('href')[len(base):]
      if 'Philosophy' in next_link:
        print('{} reached Philosophy in {} jumps.'.format(visited[0], len(visited)))
        break
      elif next_link in visited:
        print('Cycled back to {} after {} jumps.'.format(next_link, len(visited)))
        break
      elif next_link is False:
        print('Found no link in {}.'.format(visited[-1]))
      else:
        visited.append(next_link)
        print(base + next_link)
    #print(visited)


if __name__ == '__main__':
  main()