# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

#Enter name of database file with extension, should be kept on the Database folder
database_file = str(input("Enter Database File Name: "))


database_exists_flag = os.path.isfile('Database/'+database_file)
if database_exists_flag == True:

    #Enter name of html template file with extension
    template_file = str(input("Enter HTML File name: "))
    template_file_exist_flag = os.path.isfile('EmailTemplates/'+template_file)

    if template_file_exist_flag == True:

        #name of the report file is the date and time of sending email
        fileName = str(datetime.now())+".csv"


        #Location of the template goes here and it should be html files. The images should fetch from the live server
        with open('EmailTemplates/'+template_file, 'r') as f:
            html_string = f.read()

        with open('Database/'+database_file,'r') as t:    #database name should be inserted. list of emails is just inserted here
            for line in t:
                email_db = line.strip()
                report= open('Reports/'+fileName,"a+")

                message = Mail(
                    from_email='test@test.com',  #From email is mentioned, it should be configured from the sendgrid admin panel
                    to_emails=email_db,
                    subject='Sending First File',
                    html_content=html_string)
                try:
                    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_CREDENTIALS')) #API id is created from the sendgrid admin panel
                    response = sg.send(message)
                    if response.status_code==202:
                        print(email_db, 'success')
                        list1 = email_db +'\t'+ 'success'
                        report.write(str(list1)+'\n')
                    else:
                        report.write(email_db, 'failed')
                        print(email_db, 'failed')
                        list1 = email_db + '\t' + 'failed'
                        report.write(str(list1)+'\n')
                except Exception as e:
                    print(e.message)
                report.close()
        
        print("Report has been generated")
    else:
        print("Template File doesn't exist or wrong name, please check")
        exit()
else:
    print("Database File doesn't exist or wrong name, please check")
    exit()
                    

