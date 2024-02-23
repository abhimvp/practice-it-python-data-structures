from collections import namedtuple
from csv import reader
def main():
    #add code here
    #read data/Customer.csv
    with open("data/Customer.csv","r") as open_csv:
        read = reader(open_csv)
        Person = namedtuple("Person",next(read))
        # Creates a namedtuple type called "Person." The field names for this namedtuple are 
        # dynamically determined from the first row (header row) of the CSV file.
        # person = Person(*line)
        # Creates a new Person object using the data from the current line. The * operator unpacks the elements of line 
        # (which is a list) into individual arguments passed to the Person constructor.
        for line in read:
            person = Person(*line)
            print(person)
            # Person(CustomerID='100', FirstName='Teressa', LastName='Jordin', Email='tjordin8@ovcaa.org', 
            # Phone='1(215)950-6571', Address='1 South Road', City='Philadelphia', State='PA', Zipcode='19178')
    #Create workable objects with each line
    # return

if __name__ == "__main__":
    main()