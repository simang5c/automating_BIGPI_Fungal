#BIGPI Fungal Automation 
#Before running it split the Amino acid Fasta file to maximum 200 sequences in a file
#run it using:
# python automate_bigpi.py 

#program:
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from json import dumps
import re
import glob
import os
import json
import sys

#pass the name of file
fastas=glob.glob("*.fasta") # Fasta files are in the same directory where the python code is stored

new_url0="https://mendel.imp.ac.at/gpi/fungi_server.html"  #providing the link to BIGPI FUngal server
chromedriver = "/home/labor2/chromedriver_linux64/chromedriver"    #Provide the location of the chromedriver[alternatively you can also use other web browser drivers]
driver=webdriver.Chrome(chromedriver)
driver.implicitly_wait(100) #waiting to open the browser and go to the link
driver.get(new_url0)

for fasta in fastas:
    with open(fasta, 'r') as myfile:
        data = myfile.read()
        search = driver.find_element_by_name('Sequence')
        search.clear()
        driver.execute_script(f"arguments[0].value={dumps(data)};",search)
        driver.find_element_by_xpath("//input[@type='SUBMIT']").click()
        name_out=re.sub('fasta', 'html', fasta)
        with open(name_out, 'w') as f:            #writing the html file to file
            f.write(driver.page_source)
            driver.back() 
 

driver.close()

