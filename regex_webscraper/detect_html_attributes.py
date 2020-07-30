import bs4
n = int(input())
text = "\n".join(input() for _ in range(n))
soup = bs4.BeautifulSoup(text,'html.parser')
d = dict()
for g_tag in soup.find_all():
    for tag in soup.find_all(g_tag.name):
        if tag.name not in d:
            d[tag.name]=set()
            if tag.attrs:
                for i in tag.attrs.keys():
                    d[tag.name].add(i)
        else:
            if tag.attrs:
                for b in tag.attrs.keys():
                    d[tag.name].add(b)

l = sorted(list(d))
for item in l:
    print(item+":"+",".join(sorted(d[item])))
