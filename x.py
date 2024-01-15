import random as r
from time import sleep
import os

chars = '1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'

SURGE_DOMAIN = 'surge.sh'
LINKS_FILE_SUF = 'surge_links'
TIMEOUT = 10


def get_sub_domain(a=6, b=10):
    chars_count = r.randint(a, b)
    return ''.join(r.choices(chars, k=chars_count))


def write_link(domain):
    file_name = f'C:\\diss\{LINKS_FILE_SUF}_{team}.txt'
    dis_endpoint_page = DISS_ENDPOINDTS[dis]
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'https://{domain}/{dis_endpoint_page}\n')


words = [
    'help',
    'reply',
    'email',
    'recover',
    'test',
    'together',
    'today',
    'fix',
    'best',
    'validate',
    'maintenace',
    'table',
    'function',
    'data',
    'fix',
    'main',
    'good',
    'life',
    'complete',
    'verify',
    'maintane',
    'top',
    'keep',
    'skip',
    'mix',
    'available',
    'commit',
    'concil',
    'product',
    'site',
    'host',
    'ajax',
    'py',
    'life',
    'service',
    'org',
    'com',
    'wiki',
    'domain',
]


def get_surge_domain_name():
    name = r.choices(words, k=2)
    name.insert(0, get_sub_domain(4, 5))
    return '-'.join(name) + '.surge.sh'


TEAMS = {
    'hnd1',
    'hnd2',
    'hnd3',
    'hnd4',
    'hnd5',
    'hnd6',
    'hnd8',
    'hnd9',
    'hnd10',
    'hnd11',
    'hnd12',
    'hnd13',
    'hnd14',
    'hnd15',
    'hnd16',
}

DISS = {
    'spi', 'mpc',
}

DISS_ENDPOINDTS = {
    'spi': 'checkpoint/',
    'mpc': 'appel/'
}

dis = 'mpc'
links_count = 10
print('\n\n')
for team in TEAMS:
    team_dis_name = f'{dis}_{team}'
    diss_path = f'C:\\diss\\MPC\\teams_html\\{team}'
    for links_num in range(links_count):
        print(f'Link #{links_num + 1} for {team}')
        domain = get_surge_domain_name()
        command = f'surge {diss_path} {domain}'
        print(command)
        os.system(command)
        write_link(domain)
        sleep(TIMEOUT)
