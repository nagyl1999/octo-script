#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ZCode API

This object will provide an API to
the ZCode System. Credentials are
required within the .env file.

@Author: nagyl
@Date:   2022.10.09.

"""

import requests


class Session(requests.Session):
    """ ZCode Session """
    url_login = 'https://zcodesystem.com/vipclub/do_login.php'
    url_logout = 'https://zcodesystem.com/vipclub/logout.php'
    url_scorespredictor = 'https://zcodesystem.com/scorespredictor/score_games_list_n1.php'

    def __init__(self):
        """ Inicializing credentials, login """
        self.credentials = {
            'emailaddress': '',
            'password': '',
            'json_result': 1
        } # TODO - .env results
