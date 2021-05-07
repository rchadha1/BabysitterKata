# BabysitterKata


Note: 
I chose the Babysitter kata to complete for the TDD the Industry X way. I rounded up hours completed since fractional hours did not count (ex: 3.5 hours is rounded up to 4 hours worth of pay). I added validation for family name entered, start time must be no earlier than 5:00 PM, and end time must be no later than 4:00 AM. For start time / end time there were a lot of different ways a user could input the wrong things, so I decided to not create multiple validation checking. The user must input time the correct way (HH:MM AM/PM). 

How to build:
To run the babysitter.py file you will need python3 or later.

Command:
python3 babysitter.py

You will then have to input family name, start time, end time for babysitter. 

After user input is completed the babysitters resulting pay will be printed. 


Testing:
To run test_babysitter.py you will need python3 or later as well.

Command:
python3 -m unittest test_babysitter.py -v

I added multiple assert cases for checking if total pay returned was correct.






