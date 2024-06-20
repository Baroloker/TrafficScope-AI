# 项目名称

## 项目介绍

本项目是一个基于Django的图像处理应用，用于车辆检测和识别。它利用深度学习模型来分析上传的图像，检测图像中的车辆并标注出来。用户可以通过简单的Web界面上传图像并查看处理结果。

## 安装依赖

在运行项目之前，请确保已经安装了以下依赖库：

- **torch** 和 **torchvision**: 用于深度学习模型的构建和训练。
  ```bash
  conda install pytorch torchvision torchaudio cudatoolkit=<version> -c pytorch
请替换 <version> 为你希望使用的CUDA版本。
  ```

- Pillow: Python Imaging Library，用于图像处理。
  ```bash
  conda install pillow
  如果你还没有安装conda，请先安装miniconda或Anaconda。
  ```

## 使用方法
- 克隆项目仓库
  ```bash
  git clone https://github.com/your/repository.git
  cd repository
  ```
- 设置环境
  创建并激活conda环境（如果尚未创建）：
  ```bash
  conda create -n myenv python=3.8
  conda activate myenv
  ```
- 安装项目依赖

  ```bash
  pip install Django
  pip install torch torchvision
  pip install Pillow
  ```
  除了上述主要模块外，由于项目还处于维护阶段，可能需要根据后续更新需求安装其他依赖项。
- 运行项目
  在项目目录中，运行以下命令启动Django服务器：

  ```bash
  python manage.py runserver
  ```
默认情况下，服务器将在 http://localhost:8000/ 上运行。你可以在浏览器中访问该地址查看项目。
