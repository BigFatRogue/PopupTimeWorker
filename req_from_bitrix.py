import requests

cookies = {
    'showStatsColumns': 'Y',
    'BITRIX_CALL_HASH': 'b900536f5ae1c6a6d09758777b8d8763',
    'BITRIX_SM_LOGIN': 'p.golubev%40als-sk.ru',
    'BITRIX_SM_UIDL': 'p.golubev%40als-sk.ru',
    'BITRIX_SM_UIDD': 'q8tjk1ukrq2zesonhip0tqskbnx09cov',
    'BX_USER_ID': 'd177b6a9c6bc0d06d62611fb09a73e42',
    'PHPSESSID': 'GQD5bGRECKbzOiGRswgBT9gpd7oaIiUm',
    'BITRIX_SM_UIDH': 'arC4Cx8uQI1kVbYvSV5Ma9sHJRymvsl9',
}

headers = {
    'bx-cache-mode': 'HTMLCACHE',
}

params = {
    'apply_filter': 'Y',
    'REPORT_PERIOD_datesel': 'RANGE',
    'REPORT_PERIOD_from': '01.02.2024',
    'REPORT_PERIOD_to': '29.02.2024',
}

response = requests.get('https://alfalservice.bitrix24.ru/timeman/timeman.php',
                        params=params, cookies=cookies, headers=headers)

print(response.text)