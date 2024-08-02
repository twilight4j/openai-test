
# Quick start
## Install python

To download Python, head to the [official Python website](https://www.python.org/downloads/) and download the latest version.

## Install the OpenAI Python library

### Windows

Set system variable (Change in `{}`)
```
setx Path C:\Users\{twili}\AppData\Local\Programs\Python\Python{312}
setx Path C:\Users\{twili}\AppData\Local\Programs\Python\Python{312}\Scripts
```
### Install library

```bash
pip install --upgrade openai
```

## Set up your API key for a single project
### Make the `.env` file

`.env`
```
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.

OPENAI_API_KEY=abc123

```

### Install libaray
```bash
pip install python-dotenv
```

## Sending your first API request
```bash
python .\test_completion.py
```

# Testcase
## imageGeneration
상세 가이드 없음

## embeddings
1. Registry setting to enable long paths
    transformers 설치 시 선 작업 필요(관리자권한)
    ```bash
    New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
    ```

2. Install library
    ```bash
    pip install pandas
    pip install tiktoken
    pip install transformers
    pip install plotly
    pip install matplotlib
    pip install scikit-learn
    pip install torch
    pip install torchvision
    pip install scipy
    pip install ipython
    ```