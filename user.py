import json

class UIDA:
    def __init__(self):
        files = open('data.json')
        self.__data = json.load(files)

    def _get_aadhar_details(self, id = None):
        if id is not None:
            for uniquedata in self.__data["aadhar_details"]:
                if uniquedata["uid"] == id:
                    print(uniquedata)
        else:
            self.__aadhar_details = self.__data["aadhar_details"]
            print(self.__aadhar_details)
    
    def check_employee_id(self, user_id):
        if user_id in self.__data["emp_details"]:
            return True




class GovernmentPortal(UIDA):
    def __init__(self):
        super().__init__()

    def get_user_info(self):
        user_status = str(input("Enter the employee or user:"))
        if user_status == "employee":
            user_id = str(input("Enter the employee unique id:"))
            if super().check_employee_id(user_id):
                details = super()._get_aadhar_details(True)
            else:
                print("Kindly Check the unique Id")
        else:
            user_id = int(input("Enter the aadharno:"))
            details = super()._get_aadhar_details(user_id)
        
        

unique = GovernmentPortal()
unique.get_user_info()


        


