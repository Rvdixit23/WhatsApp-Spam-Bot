from selenium import webdriver
from selenium import common
from getopt import getopt
import time
import sys

from selenium.webdriver import chrome
from selenium.webdriver import firefox


version = "1.0"
"""
@todo
Adding other browsers
Sending Images
Sending voice recordings
Different formats for text spamming
Conversion into a browser extension
"""

def spamMessages(broswerDriver, receiverName, message,\
    count, verbose, index):

    
    # Waiting for the user to scan the QR Code
    time.sleep(10)
    try:
        chatBox = browserDriver.find_element_by_xpath\
            ("//span[@title='{}']".format(receiverName))
        chatBox.click()

        messageBox = browserDriver.find_element_by_xpath\
            ("//div[@id='main']/footer[1]/div[1]/div[2]")

        if index:
            for i in range(count):
                messageBox.send_keys(str(i) + message)
                time.sleep(0.1)
                sendButton = browserDriver.find_element_by_xpath\
                    ("//div[@id='main']/footer[1]/div[1]/div[3]")
                sendButton.click()
        else:
            for i in range(count):
                messageBox.send_keys(message)
                time.sleep(0.1)
                sendButton = browserDriver.find_element_by_xpath\
                    ("//div[@id='main']/footer[1]/div[1]/div[3]")
                sendButton.click()

    except common.exceptions.ElementClickInterceptedException:
        # obstructButton = broswerDriver.find_element_by_class("_2eK7W _3PQ7V")
        # obstructButton.click()
        print("Obstructed by popup")
        print("This problem is generally seen in firefox due to")
    except common.exceptions.NoSuchElementException:
        print("You have 10 seconds to scan the QR code")

if __name__ == "__main__":
    # Defaults
    browser = "chrome"
    verbose = False
    count = 10
    index = False
    name = ""
    message = ""
    # Command Line arguments
    options, remainder = getopt(sys.argv[1:], "n:m:c:b:vi", \
        ["name=", "message=", "count=", "broswer=", "verbose", "index"])
    for option, argument in options:
        if option in ("-n", "--name"):
            receiverName = argument
        elif option in ("-m", "--message"):
            message = argument
        elif option in ("-c", "--count"):
            count = int(argument)
        elif option in ("-b", "--browser"):
            browser = argument
        elif option in ("-v", "--verbose"):
            verbose = True
        elif option in ("-i", "--index"):
            index = False
        else:
            print("INVALID INPUT\nProgram aborted")
            exit()

    if verbose:
        print(options)
    # Handling invalid input
    if(not options):
        print("You did not enter options")
        print("Look at readME.md for usage details")
        exit()
    if(not receiverName):
        print("You forgot to enter the contact's name")
        exit()
    if(not message):
        print("You did not enter the message")
        exit()

    # Opening Browser
    if browser.lower() == "chrome":
        chrome_options = chrome.options.Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--disable-notifications")
        browserDriver = webdriver.Chrome(options=chrome_options)

    elif browser.lower == "firefox":
        firefox_options = firefox.options.Options()
        # @todo Fix the popup issue
        firefox_options.add_argument("--use-fake-ui-for-media-stream")
        firefox_options.add_argument("--disable-notifications")
        browserDriver = webdriver.Firefox(options=firefox_options)
        
    
    browserDriver.get("https://web.whatsapp.com/")
    time.sleep(5)
    # Calling the spam function
    spamMessages(browserDriver, receiverName, message, \
        count, verbose, index)