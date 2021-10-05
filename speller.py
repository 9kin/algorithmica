from json import dumps
from lxml.html import fromstring

tree = fromstring(open("yaspeller_report.html", 'r').read())

dictionary = []
skip = {}

def end():
    print(skip)
    print(dumps(dictionary, indent=4, sort_keys=True, ensure_ascii=False, ))
    exit(0)


res = []
for (i, table) in enumerate(tree.xpath('/html/body/div/div/table')):
    for tr in table.xpath("tr")[1:]:
        res.append((tr.find_class("table-name")[0].xpath('span')[0].text_content(),
                    tr.find_class("table-suggest")[0].text_content()))

res = list(set(res))
res.sort()
print(len(res))


for (word, suggest) in res:
    if word in skip or word in dictionary:
        continue
    print(word, suggest)
    res = input('y/n/e ').lower()
    if res == 'y' or res == "":
        dictionary.append(word)
    elif res == "e":
        end()
    else:
        skip.add(word)

end()

