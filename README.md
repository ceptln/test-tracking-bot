# DESCRIPTION
Selenium automated testing bot which simulates human behavior on a website in order to spot tracking errors
The use case here is a workflow on an app to add a new client (think of it as a B2B tool to add new leads)

# USAGE
    - WHY: 
        Spot tracking bugs on the flow 'Add a client' on the App
    - HOW: 
        (1) Create a bot that simulates human behaviour and navigates on 
        the App following a precisely designed journey 
        (2) Run automated tests on the App 
        (3) Compare its journey with Segment tracking  data (or any other tracking tool)

    - WHAT:
        Selenium Chrome Webdriver setup and managed by Python

# REQUIREMENTS
    // Downloads (in browser)
        ChromeDriver
            > https://chromedriver.chromium.org/downloads 
            > Check your Chrome version first (Parameters > About Chrome)
        ChroPath
            > https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo
            > (Optional) Cool extension that helps to spot the right HTML xpath

    // Installation (in terminal)   
        pip
            Check if pip is installed: $ -python -m pip --version
            If not: $ sudo easy_install pip (or: https://bootstrap.pypa.io/get-pip.py -o get-pip.py)
        python
            Check if python3 is installed: $ -python3 --version
            If not: $ sudo apt install python3-pip
        Selenium
            $ pip install selenium
        Packages: time, pandas, random, datetime, pyperclip, coloredlogs
            $ pip install ~
