# Automation senior
To run the tests you must have set up environment with Python version 3.10.  
Android SDK, Appium, Chromedriver, Geckodriver, Google Chrome, Mozilla Firefox, conference.apk and Jitsi Meet also have to be installed.  
Tests are intended for a real Android device, Firefox and Chrome browsers, so in `appium_setup.py` file
you should change `deviceName, app` options to adjust for your Android device, and also allow USB Debugging option in developer settings.
   
To install the dependencies run - ``pip install -r requirements.txt``    

Command ``pytest -v --html=html.report`` is used to run all three test cases  
``-v`` flag is used for verbose mode  
``--html`` flag is used for generating html report   
you can optionally use ``-k`` flag to run specific feature file, for which there are 3 - `conference, github and jitsi` for example `pytest -v --html=html_report -k github` to run only the github scenario.  

Intended to run on currently latest Firefox and Chrome versions and Android version 14  
  
IMPORTANT: For the Jitsi meet test you have to log in with a gmail account from you Android phone with credentials ``doej54190@gmail.com
and doejohn222@`` so that i does not ask for you to log in all the time.  
    
Tests are structured with human readable feature files and test steps that are located under tests folder  
For better readibility pages files are used to store locators; contest.py and appium_setup is being used for setup/teardown