#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import dummy
import time

class MedicineSales:
    dummy1 = ['타이레놀', '3000', 5]
    dummy2 = ['후시딘', '1000', 20]
    dummy3 = ['써버 쿨', '2500', 15]
    dummy4 = ['게보린', '3000', 10]
    medicines = [dummy1, dummy2, dummy3, dummy4]
    medicine_sales = [] #판매 금액 리스트

    # 매출 현황
    def medicineSales(self, data):
        # medicine_sales = 0 #판매 총액
        for i in range(len(self.medicines)):
            if data[0] == self.medicines[i][0]:
                self.medicine_sales.append(int(self.medicines[i][1])*data[1])
        #처방전을 선택한 경우
        if data[0] == "처방전":
            self.medicine_sales.append(3800)
            return self.medicine_sales
        #매출 현황을 조회한 경우
        total_price = 0
        if data[0] == "":
            for i in range(len(self.medicine_sales)):
                total_price += self.medicine_sales[i]
            return total_price
        return self.medicine_sales
