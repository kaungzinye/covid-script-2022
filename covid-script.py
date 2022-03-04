from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# THIS IS THE FORMAT FOR THE MESSAGE TO BE SENT BY TRIAGING MEDIC AFTER TRIAGING A COVID POSITIVE PATIENT

# COVID (I.E. PA-ART +VE) PATIENT DETAILS

# PATIENT NUMBER: 

# Triaging Medic: John Doe
# COVID MO: Dr John Doe

# Full Name: John Doe Tan
# NRIC: T0123456z
# Coy & 4D: Alpha 1234

# Symptoms and Duration:
# RUNNY NOSE - 1/7
# COUGH - 1/7

# History of Previous COVID and Date: Y/N
# BMI>35: Y/N
# Weight>100: Y/N

# VITALS:
# T: 37.6
# HR: 76
# BP: 110/70

# ==========
# DOB(YYYYMMDD): 20011111
# Postal Code: 123456
# Block and Street: BLK 123 EXAMPLE STREET 1
# Level and Unit Number : 12-345
# Nationality: SINGAPOREAN
# Mobile No: 12345678
text = open('test.txt','r')
inputMessage = text.read()
PATH = "C:/Users/Kaung/chromedriver.exe"
driver = webdriver.Chrome(PATH)
if "Triaging Medic" in inputMessage:
    firstIndex = inputMessage.find("Triaging Medic")+16
    lastIndex = inputMessage.find("COVID MO")
    medicNameWithRank=inputMessage[firstIndex:lastIndex].strip()
    if "LCP" in medicNameWithRank:
        medicName = medicNameWithRank[3:].strip()
    elif "CPL" in medicNameWithRank:
        medicName = medicNameWithRank[3:].strip()
    elif "PTE" in medicNameWithRank:
        medicName = medicNameWithRank[3:].strip()
    elif "CFC" in medicNameWithRank:
        medicName = medicNameWithRank[3:].strip()
    else:
        medicName = medicNameWithRank
    print(medicName)

if "Full Name" in inputMessage:
    firstIndex = inputMessage.find("Full Name")+10
    lastIndex = inputMessage.find("NRIC")
    patientName=inputMessage[firstIndex:lastIndex].strip()
    print(patientName)
    
if "NRIC" in inputMessage:
    firstIndex = inputMessage.find("NRIC")+6
    lastIndex = inputMessage.find("Coy")
    NRIC=inputMessage[firstIndex:lastIndex].strip()
    print(NRIC)

if "DOB" in inputMessage:
    firstIndex = inputMessage.find("DOB")+14
    lastIndex = inputMessage.find("Postal")
    DOB=inputMessage[firstIndex:lastIndex].strip()
    if "/" in DOB:
        DOB.replace("/","")
    print(DOB)

if "Postal" in inputMessage:
    firstIndex = inputMessage.find("Postal Code:")+12
    lastIndex = inputMessage.find("Block")
    postalCode=inputMessage[firstIndex:lastIndex].strip()
    if postalCode[0].upper== "S":
        postalCode=postalCode[1:]
    postalCodeInt = int(postalCode)
    print(postalCodeInt)

if "Block" in inputMessage:
    firstIndex = inputMessage.find("Block and Street:")+17
    lastIndex = inputMessage.find("Level")
    blockAndStreet=inputMessage[firstIndex:lastIndex].strip()
    print(blockAndStreet)

if "Level and Unit Number" in inputMessage:
    firstIndex = inputMessage.find("Level and Unit Number:")+22
    lastIndex = inputMessage.find("Nationality")
    levelAndUnitFull=inputMessage[firstIndex:lastIndex].strip()
    if levelAndUnitFull == 'NIL':
        levelNumber = None
        unitNumber = None
    else:
        hashIndex = levelAndUnitFull.find("#")
        dashIndex = levelAndUnitFull.find("-")
        levelNumber = int(levelAndUnitFull[hashIndex+1:dashIndex])
        unitNumber = int(levelAndUnitFull[dashIndex+1:])
    print(levelNumber)
    print(unitNumber)
if "Nationality" in inputMessage:
    firstIndex = inputMessage.find("Nationality")+12
    lastIndex = inputMessage.find("Mobile")
    nationality=inputMessage[firstIndex:lastIndex].strip()
    print(nationality)
isSingaporean = False
if nationality.upper() == "SINGAPOREAN":
    isSingaporean = True
if "Mobile No" in inputMessage:
    firstIndex = inputMessage.find("Mobile No")+10
    mobileNumber=int(inputMessage[firstIndex:].strip())
    print(mobileNumber)

driver.get('https://form.gov.sg/#!/61dba3b02e385400121757ae')
driver.implicitly_wait(8)
MCField = driver.find_element_by_css_selector('div[name = "61dba5b82efd780012fed4ab"]')
MCField.click()
MCList = MCField.find_elements_by_css_selector('div[role="option"]')
MCBtn = MCList[15]
MCBtn.click()
medicField = driver.find_element_by_id('61dba6712e38540012181588')
medicField.send_keys(medicName)
branchField = driver.find_element_by_css_selector('div[name="61e777526c89fd0012a37472"]')
# time.sleep(2)
branchField.click()
branchList = branchField.find_elements_by_css_selector('div[ng-repeat="option in $select.items track by $index"]')
branchBtn = branchList[0]
branchBtn.click()
yesButton = driver.find_element_by_css_selector('div[class="row ng-scope"]')
yesButton.click()
NRICField = driver.find_element_by_id('61dba7506c60da0012096b4c')
NRICField.send_keys(NRIC)
nameField = driver.find_element_by_id('61dba761b3479f0012db9ac9')
nameField.send_keys(patientName)
DOBField = driver.find_element_by_id('61de97d49c794b001221787b')
DOBField.send_keys(DOB)
genderField = driver.find_element_by_css_selector('div[id="61dba818fb72b000121db877"]')
genderField.click()
maleBtn = genderField.find_element_by_css_selector('div[role="option"]')
maleBtn.click()
nationalityField = driver.find_element_by_css_selector('div[id="radio61dbb1846c60da00120bdf99"]')
if isSingaporean:
    nationality1 = nationalityField.find_element_by_css_selector('div[class="row ng-scope"]')
    nationality1.click()
else:
    nationality1 = nationalityField.find_element_by_css_selector('div[ng-if="ng-if="vm.field.othersRadioButton""]')
    nationality1.click()
    otherNationalityField = nationality.find_element_by_css_selector('input[id="others61dbb1846c60da00120bdf99"]')
    otherNationalityField.send_keys(nationality)
postalField = driver.find_element_by_id("61dba890f46e870012acea01")
postalField.send_keys(postalCodeInt)
streetField = driver.find_element_by_id("61dba8743cff1000125ce40f")
streetField.send_keys(blockAndStreet)
if levelNumber !=None:
    levelField = driver.find_element_by_id("61dba8a42efd780012ff9993")
    levelField.send_keys(levelNumber)
if unitNumber !=None:
    unitField = driver.find_element_by_id("61dba8aa3cff1000125cf196")
    unitField.send_keys(unitNumber)
numberField = driver.find_element_by_id('61de91c7860fdd0014e31e9b')
numberField.send_keys(mobileNumber)
symptomField = driver.find_element_by_css_selector('div[id="radio61dbb13c2efd78001201b198"]')
symptomaticBtn = symptomField.find_element_by_css_selector('div[ng-repeat="option in vm.field.fieldOptions track by $index"]')
symptomaticBtn.click()
countryOfIssueField = driver.find_element_by_css_selector('div[id="radio61dbb1b52e385400121aefef"]')
singaporeBtn = countryOfIssueField.find_element_by_css_selector('div[ng-repeat="option in vm.field.fieldOptions track by $index"]')
singaporeBtn.click()
IDTypeField = driver.find_element_by_css_selector('div[name="61dbaa33f46e870012ad52db"]')
IDTypeField.click()
nricBtn = IDTypeField.find_element_by_css_selector('div[class="ui-select-choices-row ng-scope active"]')
nricBtn.click()

