from .printer import ColorPrinter

def show_help():
    """顯示 myTool 套件的使用說明"""
    
    ColorPrinter.print_colored("\n" + "="*60, "cyan", bold=True)
    ColorPrinter.print_colored("MyTool 工具包使用說明".center(60), "cyan", bold=True)
    ColorPrinter.print_colored("="*60 + "\n", "cyan", bold=True)
    
    # Tcount 使用說明
    ColorPrinter.print_colored("【Tcount - 阻塞式暫停】", "yellow", bold=True)
    print("""
使用方式：
    from myTool import Tcount
    # 或
    import myTool
    myTool.Tcount(10)  # 暫停10秒
    
    # 方法 1: 單一數字（秒）
    Tcount(10)              # 暫停10秒
    Tcount("10")            # 暫停10秒
    
    # 方法 2: 位置參數
    Tcount(1, 30)           # 暫停1分30秒
    Tcount(1, 30, 0)        # 暫停1小時30分鐘
    
    # 方法 3: 字串格式（冒號或逗號分隔）
    Tcount("1:30")          # 暫停1分30秒
    Tcount("1:30:00")       # 暫停1小時30分鐘
    Tcount("1,30,0")        # 暫停1小時30分鐘（逗號分隔）
    
    # 方法 4: 具名參數
    Tcount(hours=1, minutes=30, seconds=0)
    
    注意：Tcount 是阻塞式的，呼叫後會暫停程式執行。
""")
    
    # print_title 使用說明
    ColorPrinter.print_colored("【print_title - 列印標題】", "yellow", bold=True)
    print("""
使用方式：
    from myTool import print_title
    
    print_title("我的標題")
    print_title("彩色標題", color='blue')
    print_title("自訂標題", color='#ff5733', width=60, char='*')
""")
    
    # print_var 使用說明
    ColorPrinter.print_colored("【print_var - 自動顯示變數】", "yellow", bold=True)
    print("""
使用方式：
    from myTool import print_var
    
    name = "John"
    age = 25
    city = "Taipei"
    
    # 自動顯示變數名稱和值
    print_var(name, age, city)
    # 輸出: name = 'John', age = 25, city = 'Taipei'
    
    # 彩色輸出
    print_var(name, age, colored=True, color='green')
    print_var(name, age, colored=True, color='#00ff00')
    
    # 不換行
    print_var(name, newline=False)
""")
    
    # print_table 使用說明
    ColorPrinter.print_colored("【print_table - 列印表格】", "yellow", bold=True)
    print("""
使用方式：
    from myTool import print_table
    
    # 帶表頭的表格
    data = [
        ["Name", "Age", "City"],
        ["John", "25", "Taipei"],
        ["Mary", "30", "Tokyo"]
    ]
    print_table(data)
    
    # 自訂對齊方式
    print_table(data, align='center')  # 'left', 'center', 'right'
""")
    
    # print_colored 使用說明
    ColorPrinter.print_colored("【print_colored - 彩色列印】", "yellow", bold=True)
    print("""
使用方式：
    from myTool import print_colored
    # 或
    import myTool
    myTool.print_colored("文字", color='red')
    
    # 使用預設顏色名稱
    print_colored("紅色文字", color='red')
    print_colored("粗體藍色", color='blue', bold=True)
    
    # 使用 hex 色碼
    print_colored("自訂顏色", color='#ff5733')
    print_colored("另一種顏色", color='00ff00')  # 可省略 #
""")
    
    # 支援的顏色列表
    ColorPrinter.print_colored("\n【支援的預設顏色】", "yellow", bold=True)
    print("\n可用的顏色名稱：")
    
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black']
    for color in colors:
        ColorPrinter.print_colored(f"  • {color}", color=color)
    
    print("\n此外，您也可以使用任何 hex 色碼（例如：#ff5733 或 ff5733）")
    
    ColorPrinter.print_colored("\n" + "="*60 + "\n", "cyan", bold=True)
    print("更多資訊請參考：https://github.com/jimmy-shian/myTool\n")

# 別名支援
H = show_help
h = show_help
help = show_help
