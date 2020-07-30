# Bulk Emailer

This mass emailer uses the sendgrid api. So before using this make sure you have Sendgrid account which you can create it by visiting sendgrid.com and select the package which fits you right.<br>

## General Information
License: MIT opensource <br>
Author: <a href="https://prashantdey.in">Prashant Kumar Dey </a> <br>
Version: 0.1 <br>
Panel Used: <a href="https://sendgrid.com">Sendgrid</a> <br>
HTML Template: Template was generated through <a href="https://beefree.io/">BeeFree</a> <br>

## Requirements
1. python3 <br>
```
sudo apt-get install python3
```
2. python3-pip <br>
```
sudo apt-get install python3-pip
```

## Sendgrid Account Configuration

Step 1: Go to `Settings` (on left menu bar) and then click on `Mail Settings`. Configure your domain here. <br>
Step 2: Go to `Marketing` and then click on `Senders` and configure the email address that you want to send email from. <br>
Step 3: Go to `Email API` and then click `Integration Guide`. Choose `Web API` and then choose `Python` as programming language. <br>
Step 4: Create `API Key` and save the `API key` somewhere. Check the box which says `I've integrated the code above.` and then click on `Next: Verify Integration` <br>


## Setting Email

```
git clone https://github.com/UnpredictablePrashant/SendgridMassEmailer.git
cd SendgridMassEmailer
```

Replace `YOUR_API_KEY` with the `API_KEY` that you have copied in the previous step and run the below command.

```
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

Install sendgrid python dependency.

```
pip3 install sendgrid
```
Open `emailer.py` file and replace `SENDGRID_API_CREDENTIALS` with the `API_KEY` that you have obtained from the above step.<br>

Change the value of `from_email` from `test@test.com` to the email address that you want to send through.



## Database and HTML Template File

1. Create a database file with the list of email inside the `Database` folder. You can see the sample `testDatabase.txt` file inside the folder `Database`.
2. Create HTML email template file and put this file inside the `EmailTemplates` folder. You can see a sample html file `cybersecurity.html` inside the folder `EmailTemplates`.

## Running the project

```
python3 emailer.py
```

Enter the name of the database file. Example: `database.txt` <br>
Enter the name of the HTML template. Example: `cybersecurity.html`<br>
Enter the subject of the email. Example: `Get Free courses on cybersecurity`

## Reporting

Report is generated inside the `Reports` folder with the date and time when the program was started.

## BUGS or Improvements

If you have identified any bugs or if you feel like there is any source of improvements then feel free to write me at `prashantsavior@gmail.com`
