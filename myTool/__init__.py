"""
MyTool - 一個簡潔強大的 Python 工具包

主要功能：
- Tcount: 阻塞式暫停函數
- print_var: 自動變數名稱顯示
- print_colored: 彩色文字輸出
- print_title: 標題列印
- print_table: 表格列印
"""

from .timer import Tcount
from .printer import (
    print_title, 
    print_var, 
    print_table, 
    print_colored,
    ColorPrinter
)
from .help import show_help, H, h, help

__version__ = '0.1.0'
__all__ = [
    'Tcount',
    'print_var',
    'print_colored',
    'print_title', 
    'print_table', 
    'ColorPrinter',
    'show_help',
    'H',
    'h',
    'help'
]
