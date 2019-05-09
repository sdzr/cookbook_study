# 定义带额外状态的生成器函数
# 没有知识点，只是将属性包含到类中，然后包装一个生成器

from collections import deque


class LineHistory:
    def __init__(self, lines, hislen=3):
        self.lines = lines
        self.history = deque(maxlen=hislen)
    