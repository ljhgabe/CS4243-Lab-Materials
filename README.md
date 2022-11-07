# CS4243-Lab-Materials
This repo contains lab materials for CS4243 - [Computer Vision and Pattern Recognition](https://nusmods.com/modules/CS4243/computer-vision-and-pattern-recognition) in AY22/23 Sem 1.
I will be updating the link of my slides and other related materials here.
* [Lab Contents](#lab-contents)
* [Environment Setup](#environment-setup)
    - [Google Colab](#google-colab)
    - [For Linux & OS X (Intel)](#for-linux-and-os-x-intel)
    - [For OS X (Apple Silicon)](#for-os-x-apple-silicon)
    - [For Windows](#for-windows)


## Lab Contents
* [Week 3 Lab 1](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W3L1)
* [Week 4 Lab 2](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W4L2)
* [Week 5 Lab 3](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W5L3)
* [Week 6 Lab 4](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W6L4)
* [Week 7 Lab 5](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W7L5)
* [Week 8 Lab 6](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W8L6)
* [Week 9 Lab 7](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W9L7)
* [Week 10 Lab 8](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W10L8) (Credits to [Prof Bresson's Lab](https://github.com/xbresson/CS4243_2022))
* [Week 12 Lab 9](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W12L9) (Credits to [Prof Bresson's Lab](https://github.com/xbresson/CS4243_2022))
* [Week 13 Lab 10](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W13L10) (Credits to [Prof Bresson's Lab](https://github.com/xbresson/CS4243_2022))

## Environment Setup
### Google Colab
* Follow the instruction in this notebook:
    https://colab.research.google.com/drive/1ew1wrAGItstR7HrYD8KJJlEsj750sOAR?usp=sharing
* Open you Google Drive
* Go to CS4243-Lab-Materials

### For Linux and OS X Intel
* Execute the following commands in terminal
1. Install Miniconda3
    ```sh
    # For Linux
    curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh -J -L -k
    # For OS X (x86_64)
    curl https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o miniconda.sh -J -L -k
    chmod +x miniconda.sh
    ./miniconda.sh
    source ~/.bashrc # source ~/.zshrc if you are using zsh
    ```
2. Install the Python libraries
    ```sh
    # Clone this repo
    git clone https://github.com/ljhgabe/CS4243-Lab-Materials.git
    cd CS4243-Lab-Materials

    # Install python libraries
    conda create -n tf python=3.9
    conda activate tf
    pip install -r requirements.txt
    ```
3. Run Jupyter Notebook
    ```sh
    jupyter notebook
    ```
    
### For OS X Apple Silicon
* I found previous commands did not work for installing tensorflow on Mac with Apple Silicon. 
Here is a solution that works on my Mac M1. Shout out to [Better Data Science](https://github.com/better-data-science/TensorFlow/blob/main/000_TensorFlow_Installation_M1.md).

1. Install Homebrew:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2. Install Xcode build tools (if you don't have it yet):
    ```sh
    xcode-select --install
    ```
3. Download and install Miniforge from the following URL:
    - https://github.com/conda-forge/miniforge
    - Download the ARM64 version
    - Now you have a file called `Miniforge3-MacOSX-arm64.sh`
    ```sh
    chmod +x Miniforge3-MacOSX-arm64.sh
    ./Miniforge3-MacOSX-arm64.sh
    source ~/.bashrc # source ~/.zshrc if you are using zsh
    ```
4. Create a new virtual environment and activate it:
    ```sh
    # Clone this repo
    git clone https://github.com/ljhgabe/CS4243-Lab-Materials.git
    cd CS4243-Lab-Materials
    
    conda create -n tf python=3.9
    conda activate tf
    ```
5. Install TensorFlow and other libraries:
    ```sh
    conda install -c apple tensorflow-deps
    pip install -r requirements_arm.txt
    conda install jupyter
    ```
6. Run Jupyter Notebook
    ```sh
    jupyter notebook
    ```
   
### For Windows

1. Install Anaconda 3
   - https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

2. Go to Application -> Anaconda3 -> Anaconda Prompt
3. Install git (if you don't have it yet)
   ```sh
   conda install git
   git clone https://github.com/ljhgabe/CS4243-Lab-Materials.git
   cd CS4243-Lab-Materials
   ```
4. Create your conda environment
   ```sh
    conda create -n tf python=3.9
    conda activate tf
    ```
5. Install TensorFlow and other libraries:
    ```sh
    pip install -r requirements.txt
    ```
6. Run Jupyter Notebook
   ```sh
   jupyter notebook
   ```




