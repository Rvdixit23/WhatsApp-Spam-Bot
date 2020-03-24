# Whatsapp Web Spam Bot

## Installation  
### **NOTE** : Python3 and pip are required
    # Clone the repository
    git clone https://github.com/Rvdixit23/WhatsApp-Spam-Bot.git

    # Change the working directory to spamBot
    cd spamBot

    # Install python3 and pip if they are not installed

    # Install the requirements
    pip install -r requirements.txt

## Linux Browser Driver installation
    # Geckodriver for Firefox
    wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
    sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
    sudo chmod +x /usr/bin/geckodriver
    rm geckodriver-v0.23.0-linux64.tar.gz

    # Chromedriver for Chrome
    wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    sudo chmod +x chromedriver
    sudo mv chromedriver /usr/bin/
    rm chromedriver_linux64.zip


## Usage
```bash
python3 spamBot.py [OPTIONS]
```
1. If the name/message has non alphanumerica characters, make sure to enter the name in quotes
2. Upon running the program the browser is opened in a new window and a new WhatsApp Web session is created
3. Scan the QR Code from the phone containing the registered number(It waits 10 seconds for you. Be quick xD)
4. The script will take action in a few seconds

Example  
```bash
python3 spamBot.py -n "Ninja Man" -m "Hello there" -b "chrome" -i
```


### Program Options
```
-n, --name CONTACT_NAME          The name of the person as saved in your contacts  
-m, --message MESSAGE            The message to be sent  
-c, --count MESSAGE_COUNT        The number of times to send the message(defaults to 10)
-b, --browser BROWSER_NAME       The browser to be used  
                                 (Currently supports  'chrome' and 'firefox')  
                                 Chrome by default
-v, --verbose                    Gives verbose output(defaults to False)
-i, --index                      Sends each message with its number
                                 i.e the 10th message will be 10: [Message]
```


#### Can be run on an IPython console for continued usage  
