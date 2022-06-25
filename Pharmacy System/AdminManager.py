#!/usr/bin/python
# -*- coding: utf-8 -*-
import Admin
import time

class AdminManager:
    admin = Admin.Admin()
    members = [admin]
    
    # 관리자 인지 아닌지 판별
    def validateMember(self, id=None, pw=None):
        for member in self.members:
            if id == member.id and pw == member.pw:
                return member
        print('''
**************** 알림 *****************
    아이디 혹은 비밀번호가 틀렸습니다.
        초기화면으로 돌아갑니다.
****************************************
''')
        time.sleep(2)
        return False