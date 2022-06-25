#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import MedicineSystem
import AdminSystem

class Pharmacy:
    def __init__(self):
        self.medicine = MedicineSystem.MedicineSystem()
        self.admin = AdminSystem.AdminSystem()
        self.id = None

    def getInput(self):
        while True:
            print('''
======== 메뉴 선택 ==========
       1. 약 구매하기
       2. 관리자 모드
=============================
''')
            event = int(input("원하는 메뉴를 선택해주세요 >>> "))
            try:
                if event == 1:
                    print('''
======== 약 구매 방식 ==========
    1. 처방전으로 약 구매
    2. 처방전 없이 약 구매
================================
''')
                    customer_event = int(input("원하는 구매 방식을 선택해주세요 >>> "))
                    try: 
                        if customer_event == 1:
                            print('''
================== 추가 구매 =====================
  ** 결제 후 처방전을 약사에게 제출해주세요. **
       추가로 구매하실 물품이 있으신가요?
                1. 예
               2. 아니요
==================================================
''')
                            payment_event = int(input("입력 >>> "))
                            try:
                                if payment_event == 1:
                                    total = self.medicine.medicineSales(["처방전", 1])
                                    continue
                                elif payment_event == 2: 
                                    self.medicine.medicineSales(["처방전", 1])
                                    total = self.medicine.medicineSales(["", 0])
                                    print("")
                                    print("+++++++++++++++++++++++ 결제 +++++++++++++++++++++++")
                                    print("            결제금액은 ", total, "원 입니다.")
                                    print('            카드를 투입해주세요.')
                                    print('                   결제 중.......')
                                    time.sleep(5)
                                    print("")
                                    print(' 결제가 완료되었습니다! 영수증을 약사에게 제출해주세요.')
                                    print('              @@@@@ 시스템을 종료합니다 @@@@@')
                                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                    print("")
                                    time.sleep(2)
                                    pass
                            except:
                                print('입력값이 올바르지 않습니다. 1')
                                pass
                        elif customer_event == 2:
                            print("")
                            print('================== 약 구매 ===================')
                            print('원하시는 약 이름과 수량을 입력해 주세요.')
                            print("판매하고 있는 약 종류: ", self.medicine.medicineList())
                            name = input("약 이름 >> ")
                            quantity = int(input("수량 >> "))
                            print("===============================================")
                            print("")
                            data = [name, quantity]
                            result = self.medicine.medicineStock(data)
                            # 약과 수량을 올바르게 입력한 경우
                            if result:
                                print('''
================ 추가 구매 =====================
  ** 결제 후 처방전을 약사에게 제출해주세요. **
       추가로 구매하실 물품이 있으신가요?
                1. 예
               2. 아니요
================================================
''')
                                payment_event = int(input("입력 >>> "))
                                try:
                                    if payment_event == 1:
                                        self.medicine.medicineSales(data)
                                        # 재고 반영
                                        self.medicine.medicineStockList(data)
                                        continue
                                    elif payment_event == 2:
                                        # 총액 게산
                                        self.medicine.medicineSales(data)
                                        total = self.medicine.medicineSales(["", 0])
                                        # 재고 반영
                                        self.medicine.medicineStockList(data)
                                        print("")
                                        print("+++++++++++++++++++++++ 결제 +++++++++++++++++++++++")
                                        print("            결제금액은 ", total, "원 입니다.")
                                        print('            카드를 투입해주세요.')
                                        print('                   결제 중.......')
                                        time.sleep(5)
                                        print("")
                                        print(' 결제가 완료되었습니다! 영수증을 약사에게 제출해주세요.')
                                        print('              @@@@@ 시스템을 종료합니다 @@@@@')
                                        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                        print("")
                                        time.sleep(2)
                                        pass
                                except:
                                    print('입력값이 올바르지 않습니다. 2')
                                    pass
                            # 약과 수량 중 하나를 잘못 입력한 경우
                            else: 
                                print('''
================ 추가 구매 =====================
       추가로 구매하실 물품이 있으신가요?
                1. 예
               2. 아니요
================================================
''')
                                payment_event = int(input("입력 >>> "))
                                try:
                                    if payment_event == 1:
                                        continue
                                    elif payment_event == 2: 
                                        print("""
@@@@@ 시스템을 종료합니다. @@@@@
                                        """)
                                        time.sleep(2)
                                        pass
                                except:
                                    print('입력값이 올바르지 않습니다. 3')
                                    pass
                        else: 
                            print('입력값이 올바르지 않습니다. 4')
                            pass
                    except:
                        print('입력값이 올바르지 않습니다. 5')
                        pass
                # 관리자 모드
                elif event == 2:
                    #관리자는 로그인이 필요함 admin 계정은 id: admin / pw: qwer1234 으로 고정
                    print("")
                    print('=========== 관리자 로그인 ==============')
                    print("      ** 로그인이 필요합니다. **")
                    id = input('       아이디 >>> ')
                    pw = input('       비밀번호 >>> ')
                    print('======================================')
                    print("")
                    self.admin.login(id, pw)
                    self.setId(id)
                    # 로그인이 성공한 경우
                    if self.admin.getAdminLogInState():
                        print('''
           환영합니다!

========== 관리자 메뉴 ==========
       1. 약 재고 현황 조회
       2. 매출 현황 조회
================================
''')
                        customer_event = int(input("원하는 메뉴를 선택해주세요 >>> "))
                        try:
                            if customer_event == 1:
                                print("")
                                print("++++++++++++++++ 재고 현황 ++++++++++++++++")
                                self.medicine.medicineStockList(["", 0])
                                print('++++++++++++++++++++++++++++++++++++++++++++')
                                print("")
                                time.sleep(2)
                                print('''
============ 추가 용무 =============
       다른 용무가 있으신가요?
            1. 예
           2. 아니요
====================================
''')
                                admin_event = int(input("입력 >>> "))
                                if admin_event == 1:
                                    continue
                                elif admin_event == 2:
                                    print("")
                                    print('@@@@@ 시스템을 종료합니다 @@@@@')
                                    print("")
                                    time.sleep(2)
                                    pass
                                else:
                                    print('입력값이 올바르지 않습니다. 6')
                                    pass
                            elif customer_event == 2:
                                print("")
                                print('++++++++++++++++ 매출 현황 ++++++++++++++++')
                                total = self.medicine.medicineSales(["", 0])
                                print("현재 총 매출은 ", total, "원 입니다.")
                                print('++++++++++++++++++++++++++++++++++++++++++++')
                                print("")
                                time.sleep(2)
                                print('''
============ 추가 용무 =============
       다른 용무가 있으신가요?
            1. 예
           2. 아니요
====================================
''')
                                admin_event = int(input("입력 >>> "))
                                if admin_event == 1:
                                    continue
                                elif admin_event == 2:
                                    print("")
                                    print('@@@@@ 시스템을 종료합니다 @@@@@')
                                    print("")
                                    time.sleep(2)
                                    pass
                                else:
                                    print('입력값이 올바르지 않습니다. 7')
                                    pass
                            else:
                                print('입력값이 올바르지 않습니다. 8')
                                pass
                        except:
                            print('입력값이 올바르지 않습니다. 9')
                            pass
                    # 로그인에 실패한 경우
                    else: 
                        pass
                else: 
                    print('입력값이 올바르지 않습니다. 10')
                    pass
            except:
                print('입력값이 올바르지 않습니다. 11')
                pass

    def setId(self, id):
        self.id = id

if __name__ == '__main__':
    ts = Pharmacy()
    ts.getInput()
