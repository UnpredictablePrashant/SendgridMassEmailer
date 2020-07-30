# Bulk Emailer

This mass emailer uses the sendgrid api. So before using this make sure you have Sendgrid account which you can create it by visiting sendgrid.com and select the package which fits you right.<br>

## General Information
License: MIT opensource <br>
Author: <a href="https://prashantdey.in">Prashant Kumar Dey </a> <br>
Version: 0.1 <br>
Panel Used: Sendgrid <br>

## Requirements
<li> python3 <br>
`sudo apt-get install python3`
<li> python3-pip <br>
`sudo apt-get install python3-pip`

## Sendgrid Account Configuration

<li> Step 1: Go to `settings` (on left menu bar) and then click on `Mail Settings`. Configure your domain here.
<li> Step 2: Go to `marketing` and then click on `senders` and configure the email address that you want to send email from.
<li> Step 3: Go to `Email API` and then click `Integration Guide`. Choose `Web API` and then choose `Python` as programming language.
<li> Step 4: Create `API Key` and save the `API key` somewhere. Check the box which says `I've integrated the code above.` and then click on `Next: Verify Integration`


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


## Database and HTML Template File

<li> Create a database file with the list of email inside the `Database` folder. You can see the sample database.txt file inside the `Database` folder.
<li> Create HTML email template file and put this file inside the `EmailTemplates` folder. You can see a sample html file inside the folder.

## Running the project

```
python3 emailer.py
```

Enter the name of the database file. Example: `database.txt` <br>
Enter the name of the HTML template. Example: `cybersecurity.html`

## Reporting

Report is generated inside the `Reports` folder with the date and time when the program was started.

## BUGS or Improvements

If you have identified any bugs or if you feel like there is any source of improvements then feel free to write me at `prashantsavior@gmail.com`
