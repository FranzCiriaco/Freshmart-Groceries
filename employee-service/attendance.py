from esb_core import ESB

class AttendanceService:
    def __init__(self):
        self.esb = ESB()
        self.attendance_records = {}

    def handle_employee_data(self, body, message):
        employee = body
        self.attendance_records[employee['id']] = {'name': employee['name'], 'attendance': []}
        print(f"Initialized attendance for {employee['name']}")
        message.ack()

    def record_attendance(self, employee_id, status):
        if employee_id in self.attendance_records:
            self.attendance_records[employee_id]['attendance'].append(status)
            print(f"Recorded attendance for {self.attendance_records[employee_id]['name']}: {status}")
        else:
            print(f"No employee found with ID {employee_id}")

if __name__ == '__main__':
    attendance_service = AttendanceService()
    print("Attendance service is listening...")
    attendance_service.esb.receive_message('attendance_service', attendance_service.handle_employee_data)
