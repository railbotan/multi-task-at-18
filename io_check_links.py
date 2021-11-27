from urllib.request import Request, urlopen

links = open('res.txt', encoding='utf8').read().split('\n')

count = 0
for url in links:
    count += 1
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)
    print(f"{count} links checked!")
