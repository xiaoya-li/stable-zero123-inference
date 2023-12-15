# stable-zero123-inference
Repository for inferring the stabilityai/stable-zero123 model.


## Requirements

```bash 
conda create -n  stablezero python=3.8
conda activate stablezero
# https://github.com/threestudio-project/threestudio#installation
# torch1.12.1+cu113
# pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
# or torch2.0.0+cu118
# pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
## refer to https://pytorch.org/get-started/previous-versions/
### if cuda==11.8 
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.8 -c pytorch -c nvidia
### if cuda==11.3 
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
# optional, recommendation 
pip install ninja
### if timeout and an error is raised
#### "fatal: unable to access 'https://github.com/KAIR-BAIR/nerfacc.git/': GnuTLS recv error (-110): The TLS connection was non-properly terminated."
apt-get install gnutls-bin
git config --global http.sslVerify false
git config --global http.postBuffer 1048576000
git config --global --unset https.proxy
git config --global http.proxy ""
# install dependencies 
pip install -r threestudio_requirements.txt
## install pysdf==0.1.9
wget  https://files.pythonhosted.org/packages/1d/72/7fa831288ed26b7116ef04c413a51298e68e3b6fab0888f62a85da5b239a/pysdf-0.1.9.tar.gz
tar -zxvf pysdf-0.1.9.tar.gz
cd pysdf-0.1.9
sudo apt install libeigen3-dev
python3 setup.py install 
```

## Inference 
```bash
bash threestudio/scripts/xiaoya_test_demo.sh 
```




