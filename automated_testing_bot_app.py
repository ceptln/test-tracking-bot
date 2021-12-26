"""
***********************************************************************
************************ AUTOMATED TESTING BOT ************************
***********************************************************************

# META
    * Product: App B2B
    * Flow: Add a client
    * Released: 2021-07-20
    * Last Modified: 2021-07-21
    * By: ceptln

# USAGE
    - WHY: 
        Spot tracking bugs on the flow 'Add a client' on the App
    - HOW: 
        (1) Create a bot that simulates human behaviour and navigates on 
        the App following a precisely designed journey 
        (2) Run automated tests on the App 
        (3) Compare its journey with Segment tracking  data 

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

"""

### Ask for the number of tests ###
print(' ')
print(' ')
nb_tests = input("Hi! How many tests do you want to run? --> ")
nb_tests = int(nb_tests)+1
print(' ')
print("Ok, let's go!")
print(' ')

### Import recquired packages ###
from os import truncate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random
from datetime import datetime
import pyperclip

### Start of the tests ###
start_timestamp = datetime.now(tz=None)
time.sleep(0.1)
print('> Processing ...')
time.sleep(0.7)
print('> Success')


### Locate the chromedriver on my device ###
driver_location = "/Users/xxxxxxx/chromedriver"
driver = webdriver.Chrome(driver_location)

### Activate the driver on the webapp ###
url = 'URL_OF_THE_APP'
driver.get(url)

time.sleep(2.5) # waint for the page to load

### Login on the App ###


# Login onto the App
email = 'USER_EMAIL_ADDRESS'
password = 'USER_PASSWORD'

try:
    print(' ')
    print('> Filling email initiated')
    driver.find_element_by_xpath("//input[@id='user.email']").clear()
    driver.find_element_by_xpath("//input[@id='user.email']").send_keys(email, Keys.ENTER)
    time.sleep(1.5)
    print('> Email successfully filled')

    print('> Filling password initiated')
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password, Keys.ENTER)
    time.sleep(0.1)
    print('> Password successfully filled')
    time.sleep(1.7)
    print('> Loading...')
    time.sleep(0.3)

except :
    print("   > FAILED TO LOGIN")

try : 
    driver.find_element_by_xpath("//a[@tracked_item_type='internal_link']").click()

except : 
    pass    

print('> Page successfully loaded')

time.sleep(1)
print(' ')

time.sleep(1)
driver.find_element_by_xpath("//span[contains(@class, 'search-dropdown-title') and contains(text(), '@company_name')]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//div[contains(@class, 'search-dropdown')]/input[@type='text']").send_keys('pleasedontuse')
time.sleep(0.5)
driver.find_element_by_xpath("//li[contains(@tracked_item_name,'automatedtest')]").click()

time.sleep(2)
print(' ')
print('************************************')
print('*****  TESTING BOT ACTIVATED  ******')
print('************************************')
print(' ')
print('--> Start: '+str(start_timestamp))

nb_success = 0 # counts the number of success 
nb_attemps = 0 # counts the number of attemps

for i in range(1,nb_tests) :
    
    nb_attemps = nb_attemps+1
    wanted_contracts = []

    print(' ')
    print('***** TEST N°'+str(i)+' INITIATED *****')
    
    driver.refresh() # refreshing the page
    test_start_timestamp = datetime.now(tz=None)
    time.sleep(2)
    
    try :
        # Starting Add a client flow
        driver.find_element_by_xpath("//button[@tracked_item_name='menu_add_client_desktop']").click()
        time.sleep(3)

        ## Page: Need Type
        sales_name = 'Test'
        driver.find_element_by_xpath("//input[@id='account_client.additional_data.added_by_which_sales']").send_keys(sales_name+str(datetime.now(tz=None)))
        time.sleep(0.5)
        print('> Sales name filled')

        driver.find_element_by_xpath("//button[@tracked_item_name='button_start_journey']").click()
        time.sleep(1)

        ## Page: Personal Information
        first_name = 'Test'
        last_name = 'Test'
        email = "testcamautomated+"+str(random.randint(10000,10000000))+"@company_name.com"
        address = '2 Rue Lecourbe 75015 Paris'
        address_supplement = 'Test address supplement automated'
        previous_tenant = 'Test previous penant automated'
        elec_grid_id= '12345678912345'
        gas_grid_id = '12345678912345'
        real_estate_agent_comments = 'Test comments automated'
        callback_date = '01/06/2023'

        # Essential Infos
        driver.find_element_by_xpath("//input[@id='client.first_name']").send_keys(first_name+str(datetime.now(tz=None)))
        time.sleep(0.2)

        driver.find_element_by_xpath("//input[@id='client.last_name']").send_keys(last_name+str(datetime.now(tz=None)))
        time.sleep(0.2)

        driver.find_element_by_xpath("//input[@id='client.email']").send_keys(email)
        time.sleep(0.2)

        pyperclip.copy('600000000') # the input box cannot be filled normally - copy pasting the phone number is only working solution
        driver.find_element_by_xpath("//input[@id='client.phone_number_fr']").send_keys(Keys.COMMAND, 'v')
        print('> Essential infos filled')
        time.sleep(0.2)

        # Fill the address field (not always easy)
        try:
            # The address field completion is not an easy one neither
            driver.find_element_by_xpath("//input[@id='housing.address']").send_keys(address)
            time.sleep(0.5)
            # Select the first proposition
            driver.find_element_by_xpath("//input[@id='housing.address']").send_keys(Keys.DOWN)
            time.sleep(0.2)
            # Press enter --> the address is entered
            driver.find_element_by_xpath("//input[@id='housing.address']").send_keys(Keys.ENTER)
            time.sleep(0.2)

            address_status = '> Address successfully filled'
            print(address_status)

        except: 
            try:
                # Entering the address - second try (with another xpath)
                driver.find_element_by_xpath("//input[@id='housing.address']").clear()
                driver.find_element_by_xpath("//input[@id='housing.address']").send_keys(address)
                time.sleep(0.2)
                driver.find_element_by_xpath("//input[@id='housing.address']").send_keys(Keys.DOWN)
                time.sleep(0.7)
                driver.find_element_by_xpath("//input[@id='housing.address']").send_keys(Keys.ENTER)
                time.sleep(0.2)

                address_status = '> Address successfully filled'
                print(address_status)

            except: 
                address_status = '> Address failed'
                print(address_status)
                pass
        
        # Additional info
        element = driver.find_element_by_xpath("//input[@id='housing.address_supplement']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        driver.find_element_by_xpath("//input[@id='housing.address_supplement']").send_keys(address_supplement)
        time.sleep(0.2)
        
        driver.find_element_by_xpath("//div[@id='housing.tenantship-tenant']").click()
        time.sleep(0.2)
        
        driver.find_element_by_xpath("//input[@id='housing.previous_tenant']").send_keys(previous_tenant)
        time.sleep(0.2)
        
        driver.find_element_by_xpath("//input[@id='housing.elec_grid_id']").send_keys(elec_grid_id)
        time.sleep(0.2)
        
        driver.find_element_by_xpath("//input[@id='housing.gas_grid_id']").send_keys(gas_grid_id)
        time.sleep(0.2)
        
        driver.find_element_by_xpath("//textarea[@id='client.real_estate_agent_comments']").send_keys(real_estate_agent_comments)
        time.sleep(0.2)

        # Pick the callback date
        try:
            # Scrolling down to the date picker element (wound't open otherwise)
            element = driver.find_element_by_xpath("//span[contains(text(),'À quelle ')]")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(0.2)

            # First try
            driver.find_element_by_xpath("//div[./mat-datepicker]").click()
            time.sleep(0.2)

            date_status = '> Date picker completed'
            print(date_status)

        except:
            try:
                # Second try
                driver.find_element_by_xpath("//input[@id='call_back_date_non_edge']").click()
                time.sleep(0.2)

                date_status = '> Date picker completed (2nd attempt)'
                print(date_status)

            except:
                try :
                    # Third try
                    driver.find_element_by_xpath("//input[@id='call_back_date_non_edge']").click()
                    time.sleep(0.2)

                    date_status = '> Date picker completed (3rd attempt)'
                    print(date_status)
                except:
                    try:
                        # Fourth try
                        time.sleep(0.5)
                        driver.find_element_by_xpath("//input[@type='date']").click()
                        date_status = '> Date picker completed (4th attempt)'
                        print(date_status)

                    except:
                        date_status = '> Date picker failed (4th attempt)'
                    pass
        
        # Pick the callback time slot
        try:
            driver.find_element_by_xpath("//div[@class='mat-calendar-arrow']").click()
            time.sleep(0.5)

            driver.find_element_by_xpath("//div[text()=' 2022 ']").click()
            time.sleep(0.5)

            driver.find_element_by_xpath("//div[text() = ' JANV. ']").click()
            time.sleep(0.5)

            driver.find_element_by_xpath("//div[text() = ' 4 ']").click()

            date_status = '> Date correctly selected'
            print(date_status)

        except:
            if date_status == '> Date picker failed (4th attempt)':
                pass

            else:
                print('> Date could not be selected')
            pass

        time.sleep(0.7)
        
        try:
            driver.find_element_by_xpath("//div[./div[text()='10h30 - 11h00']]").click()
            time.sleep(0.5)

            time_status = '> Time slot correctly selected - 10h30'
            print(time_status)

        except:
            try:
                driver.find_element_by_xpath("//div[./div[text()='15h30 - 16h00']]").click()
                time.sleep(0.5)

                time_status = '> Time slot correctly selected - 15h30'
                print(time_status)

            except:
                try:
                    driver.find_element_by_xpath("//div[./div[text()='16h00 - 16h30']]").click()
                    time.sleep(0.5)

                    time_status = '> Time slot correctly selected - 16h00'
                    print(time_status)

                except:
                    if date_status == '> Date correctly selected':
                        time_status = '> Time picker failed'
                        print(time_status)
                    else:
                        pass
            pass

        # Wanted contracts
        try: 
            # Scrolling down to contract list (wound't work otherwise)
            element = driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-Energy']")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-Energy']").click()

            wanted_contracts.append('Energy')
            time.sleep(0.1)

        except:
            try:
                driver.find_element_by_xpath("//div[text()='Energie']").click()

            except:
                wc_status = '> Energy Failed'
                print(wc_status)
                pass

        try: 
            driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-InternetAcces']").click()

            wanted_contracts.append('Box')
            time.sleep(0.1)

        except :
            try:
                driver.find_element_by_xpath("//div[text()='Box']").click()

                wanted_contracts.append('Box')
                time.sleep(0.1)

            except:
                time.sleep(0.5)
                pass
        
        # Not picking Insurance because special flow
        #driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-HousingInsurance']").click()
        #time.sleep(0.5)

        try: 
            driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-Mobile']").click()

            wanted_contracts.append('Cellular')
            time.sleep(0.1)

        except :
            pass
        
        try: 
            driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-Moving']").click()

            wanted_contracts.append('Moving')
            time.sleep(0.1)
        except :
            pass

        try: 
            driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-MailRedirection']").click()

            wanted_contracts.append('MailRedirection')
            time.sleep(0.1)
        except :
            pass

        try: 
            driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-DPN']").click()

            wanted_contracts.append('DPN')
            time.sleep(0.1)
        except :
            pass
        
        try :
            driver.find_element_by_xpath("//div[@id='client.wanted_contracts-france-HomeAssistance']").click()

            wanted_contracts.append('HomeAssistance')
            time.sleep(0.1)

        except :
            pass

        # Optin
        time.sleep(0.5)

        try :

            element = driver.find_element_by_xpath("//p[contains(text(),'Oui')]")
            driver.execute_script("arguments[0].scrollIntoView();", element)

            driver.find_element_by_xpath("//label[@class='checkbox-centered']").click()
            optin_status = '> Optin completed'
            print(optin_status)
            time.sleep(0.5)

        except :
            optin_status = "> Optin failed"
            print(optin_status)
            pass

        # Confirm
        
        try :
            driver.find_element_by_xpath("//button[@id='custom.button_terminer_sticky']").click()
            end_status = '> Personal_info page converted'
            print(end_status)

        except :
            end_status = "> Couldn't click on 'Finaliser'"
            print(end_status)
            pass
        
        ## Page : Housing_data_page


        driver.find_element_by_xpath("//div[@id='housing.house_type-house']").click()

        try : 
            driver.find_element_by_xpath("//input[@type = 'number' and @min='0']").clear()
            driver.find_element_by_xpath("//input[@type = 'number' and @min='0']").send_keys('100')
            time.sleep(0.2)

        except : 
            end_status = "> Couldn't enter surface"
            print(end_status)
            pass

        try:
            element = driver.find_element_by_xpath('//div[@id="housing.house_use_case-main"]')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(0.1)

            driver.find_element_by_xpath('//div[@id="housing.house_use_case-main"]').click()
            time.sleep(0.2)


        except : 
            end_status = "> Couldn't fill the fields of housing_data_page"
            print(end_status)
            pass

        time.sleep(0.5)
        
        try :
            driver.find_element_by_xpath("//button[@id='custom.button_terminer_sticky']").click()
            end_status = '> Housing_data_page page converted'
            print(end_status)

        except :
            end_status = "> Couldn't click on 'Finaliser'"
            print(end_status)
            pass

        try :
            driver.find_element_by_xpath('//div[@id="energy-subscription.energy_type-Elec"]').click()
            time.sleep(0.2)

            driver.find_element_by_xpath('//div[@id="energy-subscription.water_heat-elec"]').click()
            time.sleep(0.2)

            driver.find_element_by_xpath('//div[@id="energy-subscription.heat-elec"]').click()
            time.sleep(0.2)

            driver.find_element_by_xpath('//div[@id="energy-subscription.baking-elec"]').click()
            time.sleep(0.2)
            
            driver.find_element_by_xpath('//input[@id="housing.elec_grid_id"]').clear()
            driver.find_element_by_xpath('//input[@id="housing.elec_grid_id"]').send_keys(elec_grid_id)
            time.sleep(0.2)

            #driver.find_element_by_xpath('//input[@id="housing.gas_grid_id"]').clear()
            #driver.find_element_by_xpath('//input[@id="housing.gas_grid_id"]').send_keys(gas_grid_id)
            #time.sleep(0.2)
        
        except :
            pass

        try :
            driver.find_element_by_xpath("//button[@id='custom.button_terminer_sticky']").click()
            end_status = '> Housing_data_page page converted'
            print(end_status)

        except :
            end_status = "> Couldn't click on 'Finaliser'"
            print(end_status)
            pass

        ## Page: Back to monitor-client dashboard
        time.sleep(0.5)
        try :
            driver.find_element_by_xpath("//div[@class='wrapper-full-drawer__close-container--icon' and @tracked_item_page='full_drawer_new_client_dashboard']").click()
            time.sleep(0.2)
            print('> Wanted contracts: '+', '.join(wanted_contracts))
            print('***** TEST N°'+str(i)+' COMPLETED *****')
            nb_success = nb_success+1

        except : 
            end_status = "didn't reach full_drawer_new_client_dashboard page"

            print('Error :'+end_status)
            print('***** TEST N°'+str(i)+' - FAILED ******')
            pass

    except :
        driver.find_element_by_xpath("//div[@class='wrapper-full-drawer__close-container--icon']").click()
        print('Error : unknown')
        print('***** TEST N°'+str(i)+' - FAILED  *****')
        pass
    
    # Computing the test duration
    test_end_timstamp = datetime.now(tz=None)
    test_time_diff = test_end_timstamp - test_start_timestamp
    test_time_diff_sec = test_time_diff.seconds
    print('  \__ duration: '+str(round(test_time_diff_sec))+' s')

    time.sleep(0.5)

# Closing the browser
driver.close()
driver.quit()

# Computing the whole test session duration
end_timestamp = datetime.now(tz=None)
tests_duration = end_timestamp - start_timestamp
tests_duration_min = int(tests_duration.seconds/60)
tests_duration_rest_sec = tests_duration.seconds - tests_duration_min*60

print(' ')
print('--> End: '+str(end_timestamp))
print(' ')
time.sleep(0.5)

print('************************************')
print('***** TESTING BOT DESACTIVATED *****')
print('************************************')

time.sleep(0.5)
print(' ')

print('MAIN TAKEAWAYS:')
print('  Output: '+str(nb_success)+' successful tests out of '+str(nb_attemps)+(' attemps.'))
print('  Total duration: '+str(tests_duration_min)+' min '+str(tests_duration_rest_sec)+ 's.')

print(' ')
print("We're done here.")
print('See you soon! :)')