from machine import Pin
from neopixel import NeoPixel
import utime

class implantedRGB():
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 100, 0)
    CYAN = (0, 255, 255)
    PURPLE = (255, 0, 255)
    WHITE = (255, 255, 255)
    ORANGE = (255, 20, 0)
    GOLD = (255, 100, 0)
    PINK = (255, 12, 12)

    def __init__(rgb) -> None: 
        rgb.np = NeoPixel(Pin(48, Pin.OUT), 1) 

    def color_transition(rgb, start_color=(0, 0, 0), end_color=(0, 0, 0), brightness=1, steps=100, delay=5):
        """
        颜色渐变转换函数
        :param np: NeoPixel对象
        :param start_color: 起始颜色 (r, g, b)
        :param end_color: 结束颜色 (r, g, b)
        :param steps: 渐变的步数
        :param delay: 每步的延迟时间 (ms)
        """
        if brightness!=1:
            start_color = rgb.produceCOLOR(start_color, brightness)
            end_color = rgb.produceCOLOR(end_color, brightness)

        for step in range(steps + 1):
            # 计算每个颜色通道的插值
            r = start_color[0] + (end_color[0] - start_color[0]) * step // steps
            g = start_color[1] + (end_color[1] - start_color[1]) * step // steps
            b = start_color[2] + (end_color[2] - start_color[2]) * step // steps

            # 设置颜色
            rgb.np[0] = (r, g, b)
            rgb.np.write()
            utime.sleep_ms(delay)

    def setRGB(rgb, colorValue, brightness = 1):
        rgb.np[0] = rgb.produceCOLOR(colorValue, brightness)
        rgb.np.write()

    def produceCOLOR(rgb, colorValue=WHITE, brightness=0.2):
        r, g, b = colorValue
        return (int(r * brightness), int(g * brightness), int(b * brightness))
    
import _thread, machine
machine.freq(240000000)

def threading(func):
    def wrapper(*args, **kwargs):
        # 创建并启动新线程运行该函数
        def thread_func(*args):
            func(*args, **kwargs)
        _thread.start_new_thread(thread_func, args)
    return wrapper

def time_counter(tick_type: int=0):
    if tick_type == 1: tick_func = utime.ticks_us  # 微秒
    elif tick_type == 2: tick_func = utime.ticks_cpu  # 纳秒
    else: tick_func = utime.ticks_ms  # 毫秒，默认为毫秒
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = tick_func()
            result = func(*args, **kwargs)
            end_time = tick_func()
            elapsed_time = time.ticks_diff(end_time, start_time)
            
            # 输出运行时间
            if tick_type == 0:
                print(f"Function took {elapsed_time} miliseconds.")
            elif tick_type == 1:
                print(f"Function took {elapsed_time} microseconds.")
            elif tick_type == 2:
                print(f"Function took {elapsed_time} CPU Clock_Ticks.")
                print(f"i.e., Function took {elapsed_time * 1000000 / machine.freq()} microseconds.")
            
            return result
        return wrapper
    return decorator

@threading
def BreathRGB():
    rgb = implantedRGB()
    while True:
        rgb.color_transition(end_color=rgb.GREEN, brightness=0.2, steps=300)
        rgb.color_transition(start_color=rgb.GREEN, brightness=0.2, steps=300)
        rgb.color_transition(end_color=rgb.BLUE, brightness=0.2, steps=300)
        rgb.color_transition(start_color=rgb.BLUE, brightness=0.2, steps=300)
        rgb.color_transition(end_color=rgb.RED, brightness=0.2, steps=300)
        rgb.color_transition(start_color=rgb.RED, brightness=0.2, steps=300)
        rgb.color_transition(end_color=rgb.YELLOW, brightness=0.2, steps=300)
        rgb.color_transition(start_color=rgb.YELLOW, brightness=0.2, steps=300)

BreathRGB()