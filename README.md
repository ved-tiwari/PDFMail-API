# PDFMail-API

Zywa techincal Assessment
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone the repository: `git clone https://github.com/ved-tiwari/PDFMail-API.git`
2. Install all necessary dependencies using Python3 PIP
   - `pip install -r requirements.txt`

## Usage
To run the application, run the following:
`python PDFMail-API`

The application will be hosted on port **http://127.0.0.1:5000**

Here's an example of a sample usecase with all perameters
> http://127.0.0.1:5000/info?email=youremail@gmail.com&date1=2024-01-01&date2=2024-06-30

When this link is ran, a document containing all information will automatically be emailed to your desired email from the address **vedt1145@gmail.com**.

Note the sending email can be changed by modifying the following lines of code

```bash
#gets password form envirironment variable
pw = ""
with open(".env", "r") as file:
   pw = file.readline()

def sendEmailTo(email):
   #customize email address 
   sender_email = "yourEmail@domain.com"
   rec_email = email
   password = pw
