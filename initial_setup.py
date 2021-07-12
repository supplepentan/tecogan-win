import subprocess

cmd_list = {
    "Update pip setuptools" : ["python", "-m", "pip", "install", "-U", "pip", "setuptools"],
    "Uninstall Keras Keras-Applications Keras-Preprocessing" : ["python", "-m", "pip", "uninstall", "Keras", "Keras-Applications", "Keras-Preprocessing"],
    "Install requirements.txt" : ["python", "-m", "pip", "install", "-r", "requirements.txt"],
    "Install Pytorch CUDA10.1" : ["python", "-m", "pip", "install", "torch==1.6.0+cu101", "torchvision==0.7.0+cu101", "-f", "https://download.pytorch.org/whl/torch_stable.html"]
    }

for k, v in cmd_list.items():
    print("====", k, "====")
    subprocess.run(v)