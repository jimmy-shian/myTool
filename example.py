# -*- coding: utf-8 -*-
"""
MyTool 使用範例
"""

from myTool import Tcount, print_title, print_var, print_table, print_colored, help

# 顯示完整說明
print_title("顯示完整說明", width=6)
help()

# 測試 Tcount （阻塞式暫停）
print_title("測試 Tcount", width=6)
print_title("Tcount 測試", color='blue')

print("暫停 2 秒...")
Tcount(2)  # 直接暫停2秒
print("完成！")

print("\n暫停 1 分30秒...")
Tcount("1:30")  # 暫停1分30秒
print("完成！")

# 測試變數列印
print_title("測試變數列印", width=6)
print_title("變數列印測試", color='green')

name = "John"
age = 25
city = "Taipei"
score = 95.5

print_var(name, age, city, score)
print("\n彩色輸出：")
print_var(name, age, colored=True, color='blue')
print_var(city, score, colored=True, color='#ff5733')

# 測試表格
print_title("測試表格", width=6)
print_title("表格列印測試", color='yellow')

data = [
    ["Name", "Age", "City"],
    ["John", "25", "Taipei"],
    ["Mary", "30", "Tokyo"],
    ["Bob", "28", "Seoul"]
]
print_table(data, align='left')

# 測試顏色
print_title("測試顏色", width=6)
print_title("顏色測試", color='magenta')

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
for color in colors:
    print_colored(f"這是 {color} 顏色", color=color)

print("\nHex 色碼測試：")
print_colored("這是 #ff5733 顏色", color='#ff5733', bold=True)
print_colored("這是 #00ff00 顏色", color='00ff00', bold=True)
print_colored("這是 #3498db 顏色", color='3498db', bold=True)

print("\n測試完成！\n")
