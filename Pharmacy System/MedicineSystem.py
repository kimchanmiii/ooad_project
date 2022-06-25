#!/usr/bin/python
# -*- coding: utf-8 -*-
import MedicineList
import MedicineStock
import MedicineStockList
import MedicineSales

class MedicineSystem:
    # 약 이름 반환
    def medicineList(self):
        medicineManager = MedicineList.MedicineList()
        return medicineManager.medicineList()

    # 구매 가능한 재고가 남아있는지 확인
    def medicineStock(self, data):
        medicineManager = MedicineStock.MedicineStock()
        return medicineManager.medicineStock(data)
    
    # 재고 현황
    def medicineStockList(self, data):
        medicineManager = MedicineStockList.MedicineStockList()
        return medicineManager.medicineStockList(data)
    
    # 매출 현황
    def medicineSales(self, data):
        medicineManager = MedicineSales.MedicineSales()
        return medicineManager.medicineSales(data)