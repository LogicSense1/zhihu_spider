import json
import re
from hashlib import md5
import datetime


def parse_json(json_read):
    re_h = re.compile('</?\w+[^>]*>')
    content = re_h.sub('', json_read['content'])
    output = {'id': json_read['id'],
              'url': json_read['url'],
              'title': json_read['question']['title'],
              'clean_time': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
              'digest': md5(content.encode('utf-8')).hexdigest(),
              'length': len(content),
              'content': content}
    parsed = json.dumps(output, separators=(',', ': '), ensure_ascii=False)
    return parsed, len(content)


if __name__ == '__main__':
    with open('./example.json') as f:
        json_read = json.loads(f.read())
    print(parse_json(json_read))
