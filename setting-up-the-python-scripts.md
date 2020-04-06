---
description: Python Dependencies Setup
---

# Setting Up

## Pip Installation

Downloading/Upgrading to Python 3 should give you a working version of pip. This allows you to install the necessary packaging needed to make this application run.

```python
#Run this through your terminal if pip isn't downloaded
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#and then run this to load
python get-pip.py
```

Now that pip is installed, we can go ahead and install the python libraries needed for this app to run

Open the command prompt and run this command

```python
#Go to the utils directory
#This will be different for every user
C:\>cd Users/cjang.WILDCAT/Desktop/EIS/utils
#PRESS ENTER

#display the contents
C:\Users\cjang.WILDCAT\Desktop\EIS\utils> dir
#PRESS ENTER
```

The output should look like this

![VERIFY THAT THERE IS A REQUIREMENTS.TXT FILE IN THE FOLDER](.gitbook/assets/image%20%2812%29.png)

Make sure that there is a txt file that says requirements on it. Requirements is a list of stuff we need for this program to run. This is crucial as we can download all our dependencies in one command.

```python
#Install our dependencies
pip install -r requirements.txt
#PRESS ENTER
```

The output should return a statement saying that the dependencies are loaded, and we should be good to go.

