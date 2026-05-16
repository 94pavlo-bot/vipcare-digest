import json
with open('/tmp/vd/digest_content.json') as f:
    d = json.load(f)
with open('/tmp/vd/image.html') as f:
    d['posts'][0]['image_html'] = f.read()
with open('/tmp/vd/digest.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False)
print('merged OK')
