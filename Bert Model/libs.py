import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import pip

def installl(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

installl("torch==1.4.0+cu100 torchvision==0.5.0+cu100 -f")
install("ignite")
install("pytorch-ignite")
install("dgl-cu100")
install("transformers")
