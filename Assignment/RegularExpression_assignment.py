import re

my_string = """<link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">"""
  
  
#print(my_string)

list_href = re.findall(r'href="([^"]*)', my_string)

#print(list_href)

for item in list_href:
    print(item)
    
list_rel = re.findall(r'rel="([^"]*)',my_string)

print(list_rel)

list_links = re.findall(r'link"([^"]*)', my_string)

print(list_links)