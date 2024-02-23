from collections import namedtuple

def can_take_order(driver,num_people):
    return driver.capacity>=num_people

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    Driver = namedtuple("driver",["name","carType","capacity"])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    iris=Driver("Iris","BMW",5)
    mickkie=Driver("Mickey","Pacifica",7)
    abhi=Driver("JaiAJi","Audi",9)
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(iris,3))

if __name__ == "__main__":
    main()