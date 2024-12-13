
class Appointment:
    apptTypeDescDict = {0:"Available",1:"1: Mens Cut $40",2:"2: Ladies Cut $60",3:"3: Mens Colouring $40",4:"4: Ladies Colouring $40"}

    def __init__(self,day_of_week, start_time_hour):
        self._client_name = " "
        self._client_phone = " "
        self._appt_type = 0
        self._day_of_week = day_of_week
        self._start_time_hour = start_time_hour

    # Getter methods for all properties
    def get_client_name(self):
        return self._client_name

    def get_client_phone(self):
        return self._client_phone

    def get_appt_type(self):
        return self._appt_type

    def get_day_of_week(self):
        return self._day_of_week

    def get_start_time_hour(self):
        return self._start_time_hour
    
    def get_end_time_hour(self):
        return self._start_time_hour + 1
    
    def get_appt_type_desc(self):
        return self.apptTypeDescDict.get(self._appt_type)

    # Setter methods for the first three properties
    def set_client_name(self, client_name):
        self._client_name = client_name

    def set_client_phone(self, client_phone):
        self._client_phone = client_phone

    def set_appt_type(self, appt_type):
        self._appt_type = appt_type


    def get_appt_type_desc_and_price(self,apptType):
        return self.apptTypeDescDict.get(apptType)
    
    def cancel(self):
        self._client_name = ""
        self._client_phone = ""
        self._appt_type = 0
        

    # Schedule method to set client_name, client_phone, and appt_type
    def schedule(self, client_name, client_phone, appt_type):
        self._client_name = client_name
        self._client_phone = client_phone
        self._appt_type = appt_type


    def __str__(self):
        return f"{self._client_name}  {self._client_phone}  {self._day_of_week}  {self._start_time_hour}:00 - {self.get_end_time_hour()}:00  {self.get_appt_type_desc()}"