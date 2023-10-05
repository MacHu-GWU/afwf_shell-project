# -*- coding: utf-8 -*-

"""
本模块用于研究如何打印出类似于下面这样的效果. 第一行是一个文本输入框, 下面会输出一些 bullet, 但是
光标始终在第一行. 其中 ``|`` 符号表示光标所在位置

::

    [Query]: hello world|
    - line 1
    - line 2
"""

import time
import sys
import blessed

t = blessed.Terminal()

# 先打印第一行
print(f"[Query]: alice")
sys.stdout.flush()
time.sleep(1)

# 打印第一个 bullet
print(f"- line 1")
sys.stdout.flush()
time.sleep(1)

# 打印第二个 bullet
print(f"- line 2")
sys.stdout.flush()
time.sleep(1)

# 向上移动三行, 到第一行
print(t.move_up(3), end="")
# 移动到第一行的末尾
print(t.move_right(len(f"[Query]: alice")), end="")
sys.stdout.flush()
time.sleep(1)

# 继续打印 xyz 三个字符
print("xyz", end="")
sys.stdout.flush()
time.sleep(1)

# 光标回到行首
print("\r", end="")
sys.stdout.flush()
time.sleep(1)

# 光标向右移动 9 个字符, 在冒号的右边
print(t.move_right(9), end="")
sys.stdout.flush()
time.sleep(1)

# 回到整段输出的末尾
print(t.move_down(3), end="")
print(t.move_left(100), end="")
sys.stdout.flush()
time.sleep(1)
