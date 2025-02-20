from flask import Flask, jsonify, request
from esb_core import ESB

app = Flask(__name__)

employees = []
esb = ESB()

@app.route('/employee', methods=['POST'])
def add_employee():
    employee = request.json
    employees.append(employee)
    
    # Notify Payroll and Attendance services
    esb.send_message('payroll_service', employee)
    esb.send_message('attendance_service', employee)
    
    return jsonify({"message": "Employee added", "employee": employee}), 201

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({"employees": employees})

if __name__ == '__main__':
    app.run(port=5000)
        