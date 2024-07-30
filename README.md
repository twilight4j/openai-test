
## Install python

To download Python, head to the [official Python website](https://www.python.org/downloads/) and download the latest version.

## Install the OpenAI Python library

### Windows

Enroll system variable (Change in `{}`)
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