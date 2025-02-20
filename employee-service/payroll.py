from esb_core import ESB

class PayrollService:
    def __init__(self):
        self.esb = ESB()

    def handle_employee_data(self, body, message):
        employee = body
        salary = employee.get('salary', 0)
        print(f"Processing payroll for {employee['name']} with salary {salary}")
        message.ack()

if __name__ == '__main__':
    payroll_service = PayrollService()
    print("Payroll service is listening...")
    payroll_service.esb.receive_message('payroll_service', payroll_service.handle_employee_data)
