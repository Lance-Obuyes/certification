import appoinments_part_1 as ap
import csv
class AppointmentManager:
    

    def input_day_of_week(dayOfWeek):
        """This function receives a string a day of the week. Prompts again if invalid input."""
        weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday"]
        while dayOfWeek not in weekdays:
            print("Day must be one of: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday")
            dayOfWeek = input("Enter day of the week: ").lower()
        return dayOfWeek

    def printMenu():
        border = "=" * 38
        print(border)
        print(f"   Hair So Long Appointment Manager   ")
        print(border)
        print("1) Schedule an appointment")
        print("2) Find appointment by name")
        print("3) Print calendar for a specific day")
        selection = input("Enter your selection: ")
        return selection

    def save_schedule_appointments(data_list):
        with open("appointment.csv","w",encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile,delimiter=",")
            writer.writerow(data_list)

    def find_appointments_by_name(appt_list,client_name):

        if ap.Appointment.get_client_name() == client_name:
            for appt in appt_list:
                print(appt)
        else:
            print("not found")


    