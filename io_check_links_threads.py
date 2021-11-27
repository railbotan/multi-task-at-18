import concurrent.futures as futures
from urllib.request import Request, urlopen

links = open('res.txt', encoding='utf8').read().split('\n')


def check_url(url: str):
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


with futures.ThreadPoolExecutor(max_workers=10) as executor:
    tasks = {executor.submit(check_url, url): url for url in links}
    for task in futures.as_completed(tasks):
        task.result()
