import requests
from parse import parse_json
import json
import os

if __name__ == '__main__':

    answer_id = 12202014
    file_num = 1

    while True:
        url = 'https://www.zhihu.com/api/v4/answers/{}?include=content'.format(answer_id)
        print(url, end='')
        answer_id += 1
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        }
        r = requests.get(url, headers=headers)
        json_read = json.loads(r.content)
        if not ('error' in json_read.keys()):
            parsed, length = parse_json(json_read)
            if length > 500:
                print('   recorded')
                with open('zhihu_corpus_' + str(file_num) + '.json', 'a') as f:
                    f.write(parsed + '\n')
                    if os.path.getsize('zhihu_corpus_' + str(file_num) + '.json')/1000000 > 100:
                        file_num += 1
            else:
                print('')
        else:
            print('')
