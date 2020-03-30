from urllib.parse import urlparse
import re


def domain_name(url):
  t1 = re.findall('\www', url)
  t2 = re.findall('\:', url)
  t3 = re.findall('\S', url)
  if bool(t2) == True and bool(t1) == False:
    domain = urlparse(url).netloc
    result = (domain.split('.')[0])
  elif bool(t1) == True and bool(t2) == False:
    domain = urlparse('https://' + url).netloc
    result = (domain.split('.')[1])
  elif bool(t1) == False and bool(t2) == False:
    domain = urlparse('https://' + url).netloc
    result = (domain.split('.')[0])
  elif bool(t1) == True and bool(t2) == True:
    domain = urlparse(url).netloc
    result = (domain.split('.')[1])
  return result


def domain_name(url): #the best solution of this task from codewars web-site
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

print(domain_name("http://google.com"))
print(domain_name("http://google.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name('icaan.org'))




# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]