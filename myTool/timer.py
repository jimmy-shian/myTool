import time

def Tcount(*args, **kwargs):
    """
    阻塞式暫停函數，支援多種時間格式
    
    使用方式：
        Tcount(10)              # 暫停10秒
        Tcount("10")            # 暫停10秒
        Tcount(1, 30)           # 暫停1分30秒
        Tcount("1:30")          # 暫停1分30秒
        Tcount("1,30,0")        # 暫停1小時30分鐘
        Tcount(hours=1, minutes=30)  # 暫停1小時30分鐘
    
    Args:
        *args: 位置參數，可以是：
               - 單一字串："HH:MM:SS", "MM:SS", "SS" 或逗號分隔格式
               - 三個整數：hours, minutes, seconds
               - 兩個整數：minutes, seconds
               - 一個整數：seconds
        **kwargs: 具名參數 (hours, minutes, seconds)
    
    Example:
        Tcount(10)              # 暫停10秒
        Tcount("10")            # 暫停10秒
        Tcount(1, 30, 0)        # 暫停1小時30分鐘
        Tcount("1:30:00")       # 暫停1小時30分鐘
        Tcount("5:30")          # 暫停5分鐘30秒
        Tcount("1,30,0")        # 暫停1小時30分鐘（逗號分隔）
    """
    hours = 0
    minutes = 0
    seconds = 0
    
    # 處理位置參數
    if args:
        if len(args) == 1:
            # 單一參數
            arg = args[0]
            if isinstance(arg, str):
                # 字串格式：支援逗號或冒號分隔
                if ',' in arg:
                    parts = list(map(int, arg.split(',')))
                elif ':' in arg:
                    parts = list(map(int, arg.split(':')))
                else:
                    parts = [int(arg)]
                
                if len(parts) == 1:  # SS 格式
                    seconds = parts[0]
                elif len(parts) == 2:  # MM:SS 格式
                    minutes, seconds = parts
                elif len(parts) == 3:  # HH:MM:SS 格式
                    hours, minutes, seconds = parts
                else:
                    raise ValueError("無效的時間格式。請使用 HH:MM:SS、MM:SS、SS 或逗號分隔格式")
            else:
                # 單一整數：視為秒數
                seconds = int(arg)
        elif len(args) == 2:
            # 兩個參數：minutes, seconds
            minutes, seconds = map(int, args)
        elif len(args) == 3:
            # 三個參數：hours, minutes, seconds
            hours, minutes, seconds = map(int, args)
        else:
            raise ValueError("位置參數過多。請使用 1-3 個參數")
    
    # 處理具名參數（會覆蓋位置參數）
    hours = kwargs.get('hours', hours)
    minutes = kwargs.get('minutes', minutes)
    seconds = kwargs.get('seconds', seconds)
    
    # 計算總秒數
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    # 帶有倒數顯示的阻塞式暫停
    for remaining in range(total_seconds, 0, -1):
        hrs = remaining // 3600
        mins = (remaining % 3600) // 60
        secs = remaining % 60
        timer_display = f"\r倒數計時：{hrs:02d}:{mins:02d}:{secs:02d} 剩餘"
        print(timer_display, end="", flush=True)
        time.sleep(1)
    print("\n時間到！")
