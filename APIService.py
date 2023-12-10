from flask import Flask, render_template, request

import DBService
import PDFService
import EmailService

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    #sample URL
    # http://127.0.0.1:5000/info?email=vedt2@outlook.com&date1=2024-01-01&date2=2024-06-30

    email = request.args.get('email', default = '*', type = str)
    date1 = request.args.get('date1', default = '*', type = str)
    date2 = request.args.get('date2', default = '*', type = str)

    print(email, date1, date2)


    #pass arguments into Database Service
    transactions = DBService.getTransactions(date1, date2)

    #pass transactions into PDF Generation Service
    PDFService.createPDF(transactions)

    #pass the email to the Email Service
    EmailService.sendEmailTo(email)


    message = "PDF Successfully Generated!"
    return render_template('result.html', message=message)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
