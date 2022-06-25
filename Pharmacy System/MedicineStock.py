#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import dummy
import time

class MedicineStock:
    dummy1 = ['타이레놀', '3000', 5]
    dummy2 = ['후시딘', '1000', 20]
    dummy3 = ['써버 쿨', '2500', 15]
    dummy4 = ['게보린', '3000', 10]
    medicines = [dummy1, dummy2, dummy3, dummy4]

    # 구매 가능한 재고가 남아있는지 확인
    def medicineStock(self, data):
        for i in range(len(self.medicines)):
            if data[0] == self.medicines[i][0]:
                if data[1] <= self.medicines[i][2]:
                    return True
                else: 
                    print('**************** 알림 *****************')
                    print('재고가 부족합니다. 남은 수량: ', self.medicines[i][2])
                    print('****************************************')
                    time.sleep(2)
                    return False
        print('해당 약을 찾을 수 없습니다. 올바른 약을 입력해주세요.')
        time.sleep(2)
        return False
