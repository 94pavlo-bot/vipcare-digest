import json
with open('/tmp/vd_repo/digest_content.json') as f:
    d = json.load(f)
with open('/tmp/vd_repo/image.html') as f:
    d['posts'][0]['image_html'] = f.read()
with open('/tmp/vd_repo/digest.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False)
print('merged OK')
