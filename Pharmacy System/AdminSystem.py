#!/usr/bin/python
# -*- coding: utf-8 -*-
import AdminManager
import Admin

class AdminSystem:
    def __init__(self):
        self.isAdminLoggedIn = False

    # 관리자 로그인 
    def login(self, id, pw):
        adminManager = AdminManager.AdminManager()
        result = adminManager.validateMember(id, pw)
        #admin 계정 로그인
        if isinstance(result, Admin.Admin):
            self.setAdminLogInState()
        else:
            pass 

    # def logout(self):
    #     self.isAdminLoggedIn = False

    def getAdminLogInState(self):
        return self.isAdminLoggedIn

    def setAdminLogInState(self):
        self.isAdminLoggedIn = True if self.isAdminLoggedIn is False else True
