class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type= vehicle_type



class Automobile (Vehicle):
    def __init__(self, year="", make="", model="", doors=0, roof="" ):
        self.year=year
        self.make = make
        self.model=model
        self.doors = doors
        self.roof = roof
        super().__init__("car")
    def __str__(self):
        NL = '\n'
        ret_str = ""
        ret_str += "Vehicle type: "+ "car"+ NL
        ret_str += "Car year: " + self.year+ NL
        ret_str += "Car make: " +self.make+NL
        ret_str += "Car model: " + self.model+NL
        ret_str += "Car doors: " +str(self.doors)+NL
        ret_str += "Car roof: "+ self.roof+NL
        return ret_str




# main program
def main():

    year=input ("Enter the year of the car: ")
    make = input ("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = int(input ("Enter the doors of the cars 2 or 4: "))
    roof = input("Enter the roof of the car: ")
    
    
  

    #. The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
    auto =  Automobile( year,make, model, doors, roof)

    print(auto)


main()