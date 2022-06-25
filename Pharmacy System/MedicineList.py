#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import dummy

class MedicineList:
    dummy1 = ['타이레놀', '3000', 5]
    dummy2 = ['후시딘', '1000', 20]
    dummy3 = ['써버 쿨', '2500', 15]
    dummy4 = ['게보린', '3000', 10]
    medicines = [dummy1, dummy2, dummy3, dummy4]

    # 약 이름 반환
    def medicineList(self):
        medicines = []
        for i in range(len(self.medicines)):
            medicines.append(self.medicines[i][0])
        return medicines