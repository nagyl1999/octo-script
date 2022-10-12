#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main File

Starts the application

@Author: nagyl
@Date:   2022.10.07.

"""

from console import Console

app = Console.Console()
app.serve()

# TODO - new command object on each input
# TODO - separate event grabber from test cases
# TODO - unified interface for events
# TODO - unified interface for test cases
# TODO - unified settings handler for test cases
