import os
from flask import Flask

class Http(Flask):
    """http服务"""

    def __init__(self,*args,**kwargs):
        # 初始化
        super().__init__(*args,**kwargs)
