# CS4243-Lab-Materials
This repo contains lab materials for CS4243 - [Computer Vision and Pattern Recognition](https://nusmods.com/modules/CS4243/computer-vision-and-pattern-recognition) in AY22/23 Sem 1.
I will be updating the link of my slides and other related materials here.
* [Lab Contents](#lab-contents)
* [Environment Setup](#environment-setup)
    - [For Linux & OS X (Intel)](#for-linux-and-os-x-intel)
    - [For OS X (Apple Silicon)](#for-os-x-apple-silicon)
    - [For Windows](#for-windows)


## Lab Contents
* [Week 3 Lab 1](https://github.com/ljhgabe/CS4243-Lab-Materials/tree/main/W3L1)

## Environment Setup
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
The method listed below needs pip. If you don't have it on your computer, I would strongly recommend you to [download
it](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Step%201%3A%20Download%20the%20get,where%20the%20above%20file%20exists.&text=Step%204%3A%20Now%20wait%20through%20the%20installation%20process.)
onto your computer first.

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




