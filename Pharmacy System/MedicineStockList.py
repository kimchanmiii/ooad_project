#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import dummy

class MedicineStockList:
    dummy1 = ['타이레놀', '3000', 5]
    dummy2 = ['후시딘', '1000', 20]
    dummy3 = ['써버 쿨', '2500', 15]
    dummy4 = ['게보린', '3000', 10]
    medicines = [dummy1, dummy2, dummy3, dummy4]
    medicine_stock = [dummy1[2], dummy2[2], dummy3[2], dummy4[2]] #재고 현황

    # 약 재고 리스트 관리
    def medicineStockList(self, data):
        for i in range(len(self.medicines)):
            if data[0] == self.medicines[i][0]:
                self.medicine_stock[i] -= data[1]
        # 재고 현황 메뉴를 선택했을 경우
        if data[0] == "":
            print(self.dummy1[0], " 수량 : ", self.medicine_stock[0])
            print(self.dummy2[0], " 수량 : ", self.medicine_stock[1])
            print(self.dummy3[0], " 수량 : ", self.medicine_stock[2])
            print(self.dummy4[0], " 수량 : ", self.medicine_stock[3])
        return self.medicine_stock
