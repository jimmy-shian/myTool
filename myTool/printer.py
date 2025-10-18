import inspect

class ColorPrinter:
    """顏色列印工具類別"""
    
    # ANSI 顏色碼
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'black': '\033[90m',
        'reset': '\033[0m'
    }
    
    @staticmethod
    def hex_to_rgb(hex_color):
        """
        將 hex 色碼轉換為 RGB
        
        Args:
            hex_color (str): hex 色碼，例如 "#ffffff" 或 "ffffff"
            
        Returns:
            tuple: (r, g, b) 值
        """
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def print_colored(text, color='white', bold=False):
        """
        列印彩色文字（支援預設顏色名稱或 hex 色碼）
        
        Args:
            text (str): 要列印的文字
            color (str): 顏色名稱（red, green, blue 等）或 hex 色碼（#ffffff）
            bold (bool): 是否粗體顯示
        """
        # 檢查是否為 hex 色碼
        if color.startswith('#') or (len(color) == 6 and all(c in '0123456789abcdefABCDEF' for c in color)):
            r, g, b = ColorPrinter.hex_to_rgb(color)
            color_code = f'\033[38;2;{r};{g};{b}m'
        else:
            color_code = ColorPrinter.COLORS.get(color.lower(), ColorPrinter.COLORS['white'])
        
        bold_code = '\033[1m' if bold else ''
        reset_code = ColorPrinter.COLORS['reset']
        print(f"{bold_code}{color_code}{text}{reset_code}")

# 獨立的 print_colored 函數，不需要 ColorPrinter. 前綴
def print_colored(text, color='white', bold=False):
    """
    列印彩色文字（支援預設顏色名稱或 hex 色碼）
    
    Args:
        text (str): 要列印的文字
        color (str): 顏色名稱（red, green, blue 等）或 hex 色碼（#ffffff）
        bold (bool): 是否粗體顯示
    
    Example:
        print_colored("紅色文字", color='red')
        print_colored("自訂顏色", color='#ff5733', bold=True)
    """
    ColorPrinter.print_colored(text, color, bold)

def print_title(title, width=50, char='=', color='blue'):
    """
    列印格式化的標題（支援彩色）
    
    Args:
        title (str): 標題文字
        width (int): 標題框的總寬度
        char (str): 用來繪製邊框的字元
        color (str): 標題顏色
    """
    border = char * width
    ColorPrinter.print_colored(f"\n{border}", color)
    ColorPrinter.print_colored(f"{title:^{width}}", color)
    ColorPrinter.print_colored(f"{border}\n", color)

def print_var(*args, newline=True, colored=False, color='green'):
    """
    列印變數名稱和值（支援彩色顯示）
    
    Args:
        *args: 要列印的變數
        newline (bool): 是否在列印後換行
        colored (bool): 是否顯示彩色輸出
        color (str): 輸出顏色（當 colored=True 時）
        
    Example:
        a = 10
        b = 'hello'
        print_var(a, b)  # 輸出: a = 10, b = 'hello'
        print_var(a, b, colored=True, color='blue')  # 彩色輸出
    """
    if not args:
        return
        
    # 取得呼叫此函數的框架
    frame = inspect.currentframe().f_back
    try:
        # 從原始碼取得變數名稱
        call_line = inspect.getframeinfo(frame).code_context[0]
        # 從函數呼叫中擷取參數
        var_names = call_line[call_line.find('(') + 1:call_line.rfind(')')].split(',')
        var_names = [name.strip() for name in var_names]
        
        # 建立輸出字串
        output = []
        for name, value in zip(var_names, args):
            # 移除任何尾隨的換行或其他空白字元
            name = name.strip()
            output.append(f"{name} = {value!r}")
            
        # 合併並列印
        final_output = ', '.join(output)
        if colored:
            ColorPrinter.print_colored(final_output, color)
        else:
            print(final_output, end='\n' if newline else '')
    finally:
        del frame  # 避免參考循環

def print_table(data, headers=None, align='left'):
    """
    列印表格
    
    Args:
        data (list): 表格資料，每列為一個列表
        headers (list, optional): 表頭
        align (str): 對齊方式 ('left', 'center', 'right')
    """
    if not data:
        return
        
    # 計算每欄的最大寬度
    if headers:
        all_rows = [headers] + data
    else:
        all_rows = data
    
    col_widths = []
    for i in range(len(all_rows[0])):
        max_width = max(len(str(row[i])) for row in all_rows)
        col_widths.append(max_width + 2)  # 加一點間距
    
    # 對齊函數
    def align_text(text, width):
        if align == 'center':
            return f"{text:^{width}}"
        elif align == 'right':
            return f"{text:>{width}}"
        else:
            return f"{text:<{width}}"
    
    # 列印表頭
    if headers:
        header_line = '│'.join(align_text(str(h), col_widths[i]) for i, h in enumerate(headers))
        print(header_line)
        print('├' + '┼'.join('─' * w for w in col_widths) + '┤')
    
    # 列印資料列
    for row in data:
        row_line = '│'.join(align_text(str(cell), col_widths[i]) for i, cell in enumerate(row))
        print(row_line)
    
    print()  # 最後換行
