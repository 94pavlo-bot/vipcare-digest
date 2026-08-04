import json

old = json.load(open('/tmp/vd/digest_content.json'))
used = old['used_urls']
# drop 2 oldest, add 2 new
used = used[2:]
used += [
    "https://casinobeats.com/2026/08/03/macao-casino-revival-in-the-cards-as-tourist-numbers-balloon/",
    "https://asgam.com/2026/07/17/dicj-data-shows-an-18-8-sequential-decline-in-vip-baccarat-ggr-in-2q26/",
]
used = used[-40:]

this_run_post_text = "9 августа, 16:30 UTC. CoinPoker сажает игроков за стол с чеком $215 и гарантией $1,000,000.\n\nРаньше - разовый ивент. Теперь - постоянная строка в календаре: первое воскресенье каждого месяца.\n\nПричина: первые два розыгрыша собрали очередь, после которой турнир перестали считать экспериментом.\n\n$215 - не порог для випа. Цена билета в кино за место в турнире с призовым уровня хайроллерского ивента.\n\nОдни удерживают китов эксклюзивом. CoinPoker удерживает массу ценой входного билета.\n\nРетеншн через доступность, не через эксклюзив.\n\n@vipcare_io"

new_queue_post_text = "Макао снова встречает толпы туристов. Год к году - плюс 14,9%.\n\nОтели забиты под завязку. Строят новые - специально под волну заездов.\n\nКазино не экономят на встрече: носильщики забирают чемоданы прямо у трапа, для випов - отдельная линия на границе и машина без очереди у выхода.\n\nОдин нюанс: за квартал VIP-баккара просела на 18,8%.\n\nТолпы прилетели. За крупный стол никто не сел.\n\nСервис для випов растёт быстрее, чем ставки самих випов.\n\nГостеприимство? Разумеется.\n\n@vipcare_io"

data = {
    "timestamp": "2026-08-04T10:15:28Z",
    "used_urls": used,
    "posts": [{"text": this_run_post_text, "image_html": None}],
    "queue": [{"text": new_queue_post_text, "image_html": None}],
    "linkedin_post": None,
}

with open('/tmp/vd/digest_content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print("used_urls count:", len(used))
print("OK")
