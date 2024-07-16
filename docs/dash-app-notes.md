## Dash app

- app opens with a particular doctor -- this can be taken as a url query parameter 
- onedrive excel file to define:
    - a list of doctors and their IDs
    - available times for doctors 
    - lengths of appointments 
    - the types of appointments per doctor
- the dates and times that are available for a specific doctor are controlled by:
    - above onedrive excel file
    - get endpoint on hospycare server: 
    ```
    curl 'http://nwcdxb.fortiddns.com:6060/hospynwc/r_appointment_rep?p_orgid=1&p_oprid=1&p_mp_rid=44&p_mp_uid=ERP&p_mp_sid=aafffjbedc&p_mp_output=H&p_mp_orientation=P&p_frdt=16/Jul/2024&p_todt=16/Aug/2024&p_e=&p_d=4&p_sp=&p_p=&p_userid=&p_wise=&p_wise=&p_status=C&P_FRTIME=&P_TOTIME=&P_NOSHOW=N&P_PIN=&p_refdocid=&p_reftype=&p_enttype=&p_mob='
    ```
- Patient chooses in the following order
    - date
    - time
    - appointment type
    - name*, mobile*, email*, DOB, patient-ID if known
        - *marked items must be given
    - brief reason for appointment
- when a submission is made
    - web app should say: thanks for your request, we will be in contact to confirm your appointment
    - whatsapp messages sent to whatsapp group where someone must enter appointment into hospycare ASAP
    - once an appointment is created, then the person from the group who created the appointment must send an email or sms or whatsapp to the patient - using an approved template. 

#### Tasks

- understand get endpoint
    - what do the different paramters mean
    - how do booking people understand the different statuses
- deploying app to heroku
    - https://towardsdatascience.com/deploying-your-dash-app-to-heroku-the-magical-guide-39bd6a0c586c 
- opening dash app with doctor name in query parameter
- creating onedrive excel file of doctors, ids, available times, appointment types
    - library to access this file?
- whatsapp & email
    - which library to send messages to group
    - which library to send emails to group
    - whatsapp group of bilal, rhesa, fahim to book appointments
    - templates for whatsapp and email to confirm appointments 

#### tickets
- create app on heroku
- app should have appointment type, date picker, then time picker, then form of patient details -- see calendly for example
- app can disable certain dates and times int he date and time picker:
    - using onedrive excel file
    - using hospycare get endpoint
- open app with url where the url parameter tells us which doctor we are booking for
    - appointment types should be based on the doctor
- app confirms appointment 
    - by sending whatsapp
    - by sending emails