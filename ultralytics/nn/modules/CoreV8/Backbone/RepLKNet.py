import torch
import torch.nn as nn
import torch.nn.functional as F    

'''
YOLOv8 + "CPNRepLKBlock", "CSCRepLKBlock", "ReNLANRepLKBlock", "C3_RepLKBlock", "C2f_RepLKBlock", 改进
- 只需要加上对应改进的核心模块，该项目代码就可以直接运行各种`YOLOv8-xxx.yaml`网络配置文件，乐高式创新改进，一键运行即可
- 相关改进有报错等 可以支持答疑服务。详情见 ⭐⭐⭐ https://github.com/iscyy/ultralyticsPro/wiki/YOLOv8 ⭐⭐⭐ 说明
'''

# ...code

class CSCRepLKBlock(nn.Module):
    def __init__(self, c1, c3, c4):  
        super().__init__()
        # 🎈YOLOv8 + "CPNRepLKBlock", "CSCRepLKBlock", "ReNLANRepLKBlock", "C3_RepLKBlock", "C2f_RepLKBlock", 改进==👇'
        # 👉获取所有Backbone主干、Neck融合等改进核心模块, 详情见, 详情见 https://github.com/iscyy/ultralyticsPro/wiki/YOLOv8
        pass

class C2f_RepLKBlock(nn.Module):
    def __init__(self, c1, c3, c4):  
        super().__init__()
        # 🎈YOLOv8 + "CPNRepLKBlock", "CSCRepLKBlock", "ReNLANRepLKBlock", "C3_RepLKBlock", "C2f_RepLKBlock", 改进==👇'
        # 👉获取所有Backbone主干、Neck融合等改进核心模块, 详情见, 详情见 https://github.com/iscyy/ultralyticsPro/wiki/YOLOv8
        pass

class C3_RepLKBlock(nn.Module):

    def __init__(self, c1, c3, c4):  
        super().__init__()
        # 🎈YOLOv8 + "CPNRepLKBlock", "CSCRepLKBlock", "ReNLANRepLKBlock", "C3_RepLKBlock", "C2f_RepLKBlock", 改进==👇'
        # 👉获取所有Backbone主干、Neck融合等改进核心模块, 详情见, 详情见 https://github.com/iscyy/ultralyticsPro/wiki/YOLOv8
        pass

class CPNRepLKBlock(nn.Module):
    def __init__(self, c2, c3, c4):  
        super().__init__()
        # 🎈YOLOv8 + "CPNRepLKBlock", "CSCRepLKBlock", "ReNLANRepLKBlock", "C3_RepLKBlock", "C2f_RepLKBlock", 改进==👇'
        # 👉获取所有Backbone主干、Neck融合等改进核心模块, 详情见, 详情见 https://github.com/iscyy/ultralyticsPro/wiki/YOLOv8
        pass

class ReNLANRepLKBlock(nn.Module):
    def __init__(self, c1, c3, c4):  
        # 🎈YOLOv8 + "CPNRepLKBlock", "CSCRepLKBlock", "ReNLANRepLKBlock", "C3_RepLKBlock", "C2f_RepLKBlock", 改进==👇'
        # 👉获取所有Backbone主干、Neck融合等改进核心模块, 详情见, 详情见 https://github.com/iscyy/ultralyticsPro/wiki/YOLOv8
        pass