#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import  Enum

class HttpCode(str,Enum):
    """业务状态码"""
    SUCCESS = "success" # 成功状态码
    FAIL = "fail"  # 失败状态码
    NOT_FOUND = "not_found" # 未找到
    UNAUTHORIZED = "unauthorized"  # 未授权
    FORBIDDEN = "forbidden"  # 无权限
    VALIDATE_ERROR = "validation_error"  # 数据校验错误

