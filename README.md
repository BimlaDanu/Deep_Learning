## Image reconstruction and classification using CNN

See the detail of [Torchvision documentation](https://docs.pytorch.org/vision/main/index.html)

## Compatible with python 3.11.3 Environment
```python
- !pip uninstall torch torchvision -y
- !pip install torch==2.1.2 torchvision==0.16.2
- !pip show torch torchvision
```


## CUDA Environment
```python
- !pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu124

- import torch
- import torchvision
- !pip show torch torchvision

- print(torch.__version__)
- print(torchvision.__version__)
```