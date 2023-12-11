# Holiday absence tracker
# Some initial code for an absence tracker. It should automate the tracking by taking an input from outlook where a manager initially books someone off and then add them all up over the year. In the future, it store could the calculated data in excel.  
Outlook_input = "Barry is on holiday"       # Input would come from outlook calendar where it would take an event that was posted on a certain date saying "Barry on holiday" or "Trevor is sick" EG 15/11/23. Not quite sure how to do this as of right now, assuming requires some sort of API.

staff_absences = {                          # Dictionary which stores staff name and number of absences.
    "Barry"  : 0,
    "Trevor" : 0,
    "Reece" : 0,
    "Olly"  : 0,
    "Gary" : 0
}

for key in staff_absences:
    if key in Outlook_input:
        staff_absences[key] += 1

print(staff_absences[key])                  # LogicError ,prints 0 when expecting the number of absences for barry as 1. Unsure whether I'm meant to solve this or this is JUST a fun game for you guys.