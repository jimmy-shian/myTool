# 🛠️ MyTool

> 一個簡潔強大的 Python 工具包，提供靈活的暫停功能和增強的列印工具

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

## ✨ 特色功能

- ⏱️ **Tcount** - 阻塞式暫停，支援多種時間格式
- 🔧 **print_var** - 自動偵測變數名稱並顯示
- 🎨 **print_colored** - 彩色輸出，支援 Hex 色碼
- 📊 **print_table** - 自動格式化的美觀表格
- 🎯 **print_title** - 彩色標題列印
- 📖 **內建說明** - 隨時查看使用方法
- 🚀 **零依賴** - 純 Python 標準庫實現

## 📦 安裝

### 方法 1: 從 GitHub 安裝（推薦）

```bash
pip install git+https://github.com/jimmy-shian/myTool.git
```

### 方法 2: 本地開發安裝

```bash
git clone https://github.com/jimmy-shian/myTool.git
cd myTool
pip install -e .
```

### 驗證安裝

```python
import myTool
myTool.help()  # 顯示完整使用說明
```

## 🚀 快速開始

```python
import myTool

# 1. 暫停 10 秒
myTool.Tcount(10)

# 2. 自動顯示變數
name = "John"
age = 25
myTool.print_var(name, age)  # 輸出: name = 'John', age = 25

# 3. 彩色輸出
myTool.print_colored("成功！", color='green', bold=True)
myTool.print_colored("自訂顏色", color='#ff5733')
```

或者直接 import 需要的功能：

```python
from myTool import Tcount, print_var, print_colored

Tcount(10)  # 暫停 10 秒
print_var(name, age)
print_colored("成功！", color='green')
```

## 📚 詳細使用

### ⏱️ Tcount - 阻塞式暫停

支援多種時間格式，直接呼叫即可暫停程式執行：

```python
from myTool import Tcount

# 方法 1: 單一數字（秒）
Tcount(10)              # 暫停 10 秒
Tcount("10")            # 暫停 10 秒

# 方法 2: 位置參數
Tcount(1, 30)           # 暫停 1 分 30 秒
Tcount(1, 30, 0)        # 暫停 1 小時 30 分鐘

# 方法 3: 字串格式 - 冒號分隔
Tcount("1:30")          # 暫停 1 分 30 秒
Tcount("1:30:00")       # 暫停 1 小時 30 分鐘

# 方法 4: 字串格式 - 逗號分隔
Tcount("1,30,0")        # 暫停 1 小時 30 分鐘

# 方法 5: 具名參數
Tcount(hours=1, minutes=30, seconds=0)

# 使用範例
print("開始處理...")
Tcount(5)  # 暫停 5 秒
print("處理完成！")
```

**注意**：`Tcount` 是阻塞式的，呼叫後會暫停程式執行指定的時間。

### 🎨 print_colored - 彩色列印

支援預設顏色和 Hex 色碼，不需要 `ColorPrinter.` 前綴：

```python
from myTool import print_colored

# 使用預設顏色
print_colored("紅色文字", color='red')
print_colored("粗體藍色", color='blue', bold=True)

# 使用 Hex 色碼（支援真彩色）
print_colored("橘紅色", color='#ff5733')
print_colored("綠色", color='00ff00')  # 可省略 #
print_colored("自訂顏色", color='#3498db', bold=True)
```

**支援的預設顏色：**
`red` | `green` | `yellow` | `blue` | `magenta` | `cyan` | `white` | `black`

### 🔧 print_var - 自動變數顯示

自動偵測變數名稱，無需手動輸入：

```python
from myTool import print_var

name = "Alice"
age = 30
city = "Taipei"
score = 95.5

# 基本用法
print_var(name, age, city)
# 輸出: name = 'Alice', age = 30, city = 'Taipei'

# 彩色輸出
print_var(name, age, colored=True, color='green')
print_var(city, score, colored=True, color='#00ff00')

# 不換行
print_var(name, newline=False)
print(" 繼續在同一行")
```

### 📊 print_table - 表格列印

自動格式化的美觀表格：

```python
from myTool import print_table

# 基本表格
data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "Taipei"],
    ["Bob", "25", "Tokyo"],
    ["Charlie", "35", "Seoul"]
]

print_table(data)

# 自訂對齊方式
print_table(data, align='center')  # left, center, right
print_table(data, align='right')
```

### 🎯 print_title - 標題列印

```python
from myTool import print_title

# 基本標題
print_title("我的應用程式")

# 彩色標題
print_title("成功", color='green')
print_title("警告", color='#ffaa00')

# 自訂寬度和字元
print_title("重要通知", width=60, char='*', color='red')
```

### 📖 內建說明系統

```python
import myTool

# 顯示完整使用說明（包含所有功能和顏色列表）
myTool.help()   # 或 myTool.H() 或 myTool.h()
```

## 💡 實用範例

### 範例 1: 簡單的倒數計時

```python
from myTool import Tcount, print_colored

print_colored("程式將在 5 秒後開始...", color='yellow')
Tcount(5)
print_colored("開始執行！", color='green', bold=True)
```

### 範例 2: 處理進度顯示

```python
from myTool import Tcount, print_colored, print_title
from tqdm import tqdm

print_title("任務執行中", color='blue')

# 使用 tqdm 顯示進度
for i in tqdm(range(100), desc="處理中"):
    Tcount(0.1)  # 每次暫停 0.1 秒

print_colored("✅ 任務完成！", color='green', bold=True)
```

### 範例 3: 系統監控顯示

```python
from myTool import print_var, print_colored, print_title, Tcount

while True:
    print_title("系統監控", color='cyan')
    
    cpu = 45.2
    memory = 78.5
    disk = 92.1
    
    print_var(cpu, memory, disk, colored=True, color='green')
    
    Tcount(1)  # 每秒更新一次
```

### 範例 4: 資料報表

```python
from myTool import print_table, print_title, print_colored

print_title("銷售報表", color='yellow')

sales_data = [
    ["產品", "數量", "金額"],
    ["筆電", "50", "$50,000"],
    ["手機", "120", "$36,000"],
    ["平板", "80", "$24,000"]
]

print_table(sales_data, align='center')
print_colored("報表生成完成", color='green', bold=True)
```

### 範例 5: 使用 import myTool

```python
import myTool

# 直接使用主要功能
myTool.Tcount(10)  # 暫停 10 秒

name = "Test"
myTool.print_var(name)  # 顯示變數

myTool.print_colored("成功！", color='green')  # 彩色輸出

myTool.help()  # 查看完整說明
```

## 🎯 API 參考

### 主要函數

```python
# Tcount - 阻塞式暫停
Tcount(*args, **kwargs)
# 參數：位置參數（1-3個整數或單一字串）或具名參數（hours, minutes, seconds）

# print_var - 自動變數顯示
print_var(*args, newline=True, colored=False, color='green')

# print_colored - 彩色輸出
print_colored(text, color='white', bold=False)

# print_title - 標題列印
print_title(title, width=50, char='=', color='blue')

# print_table - 表格列印
print_table(data, headers=None, align='left')
```

## 📋 系統需求

- **Python**: >= 3.6
- **依賴**: 無（純 Python 標準庫）
- **終端機**: 支援 ANSI 色碼（Windows Terminal、PowerShell 7+、大部分 Linux/Mac 終端機）

## 🔧 開發

### 運行範例

```bash
# 完整範例
python example.py

# 簡單測試
python test_simple.py
```

### 快速測試

```bash
python -c "import myTool; myTool.Tcount(1); print('OK')"
```

## 📝 更新日誌

### v0.1.0 (2025-10-18)
- ✨ 初始版本發布
- ⏱️ Tcount 阻塞式暫停（支援多種格式）
- 🎨 print_colored 彩色列印（支援 Hex 色碼）
- 🔧 print_var 自動變數名稱偵測
- 📊 print_table 表格列印功能
- 🎯 print_title 標題列印
- 📖 內建說明系統

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

**貢獻指南：**
- 程式碼符合 PEP 8 規範
- 新增適當的測試案例
- 更新相關說明文件
- 保持向後相容性

## 💡 常見問題

**Q: Tcount 和 time.sleep 有什麼不同？**

A: `Tcount` 提供更靈活的時間格式輸入，例如 `Tcount("1:30")` 比 `time.sleep(90)` 更直觀。

**Q: 如何顯示所有支援的顏色？**

A: 使用 `myTool.help()` 會顯示所有支援的預設顏色。

**Q: 可以在 Jupyter Notebook 中使用嗎？**

A: 可以！所有功能都支援 Jupyter Notebook。

**Q: 顏色無法正常顯示怎麼辦？**

A: 確保您的終端機支援 ANSI 色碼。Windows 用戶建議使用 Windows Terminal 或 PowerShell 7+。

## 📄 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 👤 作者

Jimmy Shian - [@jimmy-shian](https://github.com/jimmy-shian)

專案連結: [https://github.com/jimmy-shian/myTool](https://github.com/jimmy-shian/myTool)

## ⭐ Star History

如果這個專案對您有幫助，請給它一個 ⭐️！

---

<p align="center">Made with ❤️ by Jimmy Shian</p>
