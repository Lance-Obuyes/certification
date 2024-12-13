import appoinments_part_1 as ap
from appt_manager import AppointmentManager as am
import csv

def main():
    exit = False
    appt_list = []


    


    while exit == False:
        menu = am.printMenu()
        match menu:
            case "0":
                print("** Exit the system ***")
                saveInput=input("Would you like to save all scheduled appointments to a file (y/n?): ").lower()
                if saveInput == "y":
                    am.save_schedule_appointments(appt_list)
                    print(f"{len(appt_list)} scheduled appointments have been success")
                    exit = True
                print("Goodbye!")
                exit = True
            case "1":
                found = False
                index = 0
                print("*** Schedule an appointment ***")
                clientApptDay = input("Enter day of the week: ").lower()
                am.input_day_of_week(clientApptDay)
                clientApptHour = int(input("Enter start hour: "))
                if clientApptHour < 9 or clientApptHour > 16:
                    print("Sorry that time slot is not in the weekly calendar!")
                    clientApptHour=""
                    am.printMenu()
                client = ap.Appointment(clientApptDay,clientApptHour)
                appt_list.append(client)
                clientName = input("Client Name: ")
                clientPhone = input("Client Phone: ")
                print("Appointment Types")
                clientApptType = int(input("Type of Appointment: "))
                client.schedule(clientName,clientPhone,clientApptType)
                print(f"Appointment for {client.get_client_name().capitalize()} has been for {clientApptDay.capitalize()} at {client.get_start_time_hour()}:00")               


                
                exit = False
                
            case "2":
                print("*** Find appointment by name ***")
                findClient = input("Enter client name: ")
                for clientNames in appt_list:
                    clientNames = ap.Appointment.get_client_name()
                    print(clientNames)
                #am.find_appointments_by_name(appt_list,findClient)

            case _:
                print("Invalid")
                exit = False


            



if __name__ == "__main__":
    main()