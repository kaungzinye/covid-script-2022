# Covid Form Submitting Script

This python script was created by me as a way to automate the
submission of details of PA-ART +VE patients in camp.

# Why did I make this script?

Previously, the triaging medic would send a message containing the required details of
PA-ART +VE patient to a group chat. I would then need to manually copy the required information
into a form that is to be submitted to record these patients in MOH's database of C+ patients.
The process was tedious and there were 20+ patiets daily hence I decided to automate it using python
to save hours worth of time.

## HOW TO INSTALL

Make sure you have python 3 downloaded and then glone this git repository

## HOW TO USE:

1. The triaging medic should send a message using the format below to send the details of the
   patient, both for the Doctor to gain key info about the patient's condition, as well as to include
   details such as the patient's address and phone number so that MOH can keep track of which
   patients have had contracted COVID-19.

### THIS IS THE FORMAT FOR THE MESSAGE TO BE SENT BY TRIAGING MEDIC AFTER TRIAGING A COVID POSITIVE PATIENT

```COVID (I.E. PA-ART +VE) PATIENT DETAILS

PATIENT NUMBER: (Number of total covid positive patients for easy tracking.)

Triaging Medic: John Doe
COVID MO: Dr John Doe

Full Name: John Doe Tan
NRIC: T0123456z
Coy & 4D: Alpha 1234

Symptoms and Duration:
RUNNY NOSE - 1/7
COUGH - 1/7

History of Previous COVID and Date: Y/N
BMI>35: Y/N
Weight>100: Y/N

VITALS:
T: 37.6
HR: 76
BP: 110/70

========
DOB(YYYYMMDD): 20011111
Postal Code: 123456
Block and Street: BLK 123 EXAMPLE STREET 1
Level and Unit Number : 12-345
Nationality: SINGAPOREAN
Mobile No: 12345678
```

2. Copy paste this message from your respective group chat and into the test.txt
   file.

3. Run the covid-script.py, a window should open up in a chromium browser with all
   of the fields in the form filled.

4. Double check that all of the details are accurate, and click submit. Boom,
   you just saved 5 minutes of cross checking and doing this form manually, which in turn
   will save you many hours of mindless copy pasting. The only cost of using this being
   the many hours I spent trying to make this script. Enjoy!
