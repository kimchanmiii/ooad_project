#!/usr/bin/python
# -*- coding: utf-8 -*-

from Member import Member


class Admin(Member):
    def __init__(self):
        self.id = 'admin'
        self.pw = 'qwer1234'
        self.name = 'admin'

