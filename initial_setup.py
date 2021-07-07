import os

os.system("python -m pip install -U pip setuptools")
os.system("python -m pip install -r requirements.txt")
os.system("python -m pip uninstall Keras Keras-Applications Keras-Preprocessing")
os.system("python -m pip install keras==2.3.1")
os.system("python -m pip install tensorflow-gpu==1.14.0")
os.system("python -m pip install requests")
os.system("python -m pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html")