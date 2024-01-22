import random as r
chars = '1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'


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
    name.append(get_sub_domain(4,5))
    return '-'.join(name) + '.surge.sh'

def get_sub_domain(a=6,b=10):
    chars_count = r.randint(a,b)
    return ''.join(r.choices(chars, k=chars_count))


def hide_url(url):
    chars = map( lambda char: "'" + char + "'",list(url))
    return '+'.join(chars)

