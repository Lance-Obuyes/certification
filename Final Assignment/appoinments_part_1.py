

class Appointment():
    """Appointment Class"""

    # Constructor Function
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ""        
        self.__client_phone = 0       
        self.__appt_type = 0          
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    
    # Getter Functions
    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appt_type

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour
    
    
    # Appointment Type Function
    def get_appt_type_desc(self, __appt_type):

        appt_desc = ""

        match __appt_type:
            case 0:
                appt_desc = "Available"
            case 1:
                appt_desc = "Mens Cut"
            case 2:
                appt_desc = "Ladies Cut"
            case 3:
                appt_desc = "Mens Colouring"
            case 4:
                appt_desc = "Ladies Colouring"
            case _:
                appt_desc = "Unknown Appointment Type"

        return appt_desc
    
        # Appointment Type Description and Price Function
    def get_appt_type_desc_and_price(self, appt_type):
        appt_desc = ""
        price = 0

    # ask about contants for this function

        match appt_type:
            case 0:
                appt_desc = "Available"
                price = 0  
            case 1:
                appt_desc = "Mens Cut"
                price = 40
            case 2:
                appt_desc = "Ladies Cut"
                price = 60
            case 3:
                appt_desc = "Mens Colouring"
                price = 40
            case 4:
                appt_desc = "Ladies Colouring"
                price = 80
            case _:
                appt_desc = "Unknown Appointment Type"
                price = 0

        return f"{appt_type}: {appt_desc} ${price}"


    

    # End of Appointment Function
    def get_end_time_hour(self, __start_time_hour):

        end_time_hour = 0
        end_time_hour = __start_time_hour + 1

        return end_time_hour
    

    # Setter Functions
    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    
    # Schedule Function
    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type
    
    # Cancel Function
    def cancel(self):   
        self.__client_name = ""
        self.__client_phone = 0
        self.__appt_type = 0

    
    # Format Record Function
    def format_record(self):
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{'0' + str(self.__start_time_hour) if self.__start_time_hour < 10 else str(self.__start_time_hour)}"
    

    # Str Function
    def __str__(self):
        start_hour = f"{self.__start_time_hour:02}:00"

        end_hour = f"{self.get_end_time_hour(self.__start_time_hour):02}:00"

        appt_type_desc = self.get_appt_type_desc(self.__appt_type)
        
        return f"{self.__client_name} {self.__client_phone} {self.__day_of_week} {start_hour} - {end_hour} {appt_type_desc}"
    

def main():
    pass


if __name__ == "__main__":
    main()