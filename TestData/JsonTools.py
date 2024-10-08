import json
import os
from types import SimpleNamespace

from userConf.config import JOSN_ROOT_PATH


class Dataloader():
    def __init__(self, filename):
        self.path = os.path.join(JOSN_ROOT_PATH, filename)

    def load(self):
        with open(self.path, 'r') as f:
            # 从JSON文件中加载数据，并将其解析为SimpleNamespace对象
            data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
        return
