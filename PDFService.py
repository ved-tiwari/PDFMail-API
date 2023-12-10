import pdfkit

def createPDF(data):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transaction Details</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f8f8;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333333;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 10px;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Transaction Details</h1>
        <table>
            <thead>
                <tr>
                    <th>User Email</th>
                    <th>Date of Transaction</th>
                    <th>Amount</th>
                </tr>
            </thead>
            <tbody>
    '''

    for i in data:
        email = list(i)[0]
        date = list(i)[1]
        amount = "$" + str(list(i)[2])
        html += f'''
<tr>
                    <td>{email}</td>
                    <td>{date}</td>
                    <td>{amount}</td>
                </tr>
'''

    html += '''
    </tbody>
        </table>
    </div>
</body>
</html>

    '''

    pdfkit.from_string(html, "static/output.pdf")