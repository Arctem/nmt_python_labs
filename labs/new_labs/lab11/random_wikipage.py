from urllib import request

base = 'https://en.wikipedia.org'

def get_random():
  req = request.Request(base + '/wiki/Special:Random',
    headers={'User-Agent' : 'Python Browser'})
  page = request.urlopen(req)
  url = page.geturl()
  url = url[len(base):]
  return url

def main():
  rand_url = get_random()
  print('Found random page {}.'.format(rand_url))

if __name__ == '__main__':
  main()