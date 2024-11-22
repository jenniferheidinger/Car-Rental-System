# This first class outlines all the functions associated with the general options of the program such as availablilty, renting and returining
class RentalShop:
    # the def__init__ fucntion was used to introduce a new instance of a class. In this case, the class was for the RentalShop and it just initialises the attributes contained within the class ( to assign inital values that will be refered to later in the program) 
    def __init__(self):
        # This self.availability dictionary showcases the name of the car first, how many of each car is available (1), the daily price and lastly the weekly price
        self.availability = {
            "Hatchback": [4, 30, 25],  # 5 available, £30/day, £25/day for week+
            "Sedan": [3, 50, 40],
            "SUV": [3, 100, 90],
        }
    # used to display the availability of the cars in the above dictonary  
    def display_availability(self):
        print("\nAvailable Cars and Prices:")
        for stock, (car_type, details) in enumerate(self.availability.items(), start=1): #This checks the car availability and starts the car count from 1
            available, daily_rate, weekly_rate = details # all the details concerning the availability of the car
            print(
                f"{stock}. {car_type.capitalize()}: {available} available. " #These statements will print the values stored in the dictionaries, each of the car names along with their availabailities, the daily rate and the daily rate over a week
                f"£{daily_rate}/day (<7 days), £{weekly_rate}/day (7+ days)"
            )
        print()

    def rent_car(self, car_type, days):
        if car_type not in self.availability: # This if statement is important because the ability to rent a car is depenfant on the availability of the car so the system first has to check if there are enough cars available to rent
            print("\nInvalid car type selected.\n")
            return None
        available, daily_rate, weekly_rate = self.availability[car_type]
        if available <= 0:
            print(f"\nSorry, {car_type.capitalize()}s are out of stock.\n") # If the car is not available the system will notify the user, and due to the while loop, the customer can then choose another option or car to proceed with
            return None

        # Determine rate
        rate = daily_rate if days < 7 else weekly_rate # the cost of the car per day is dependant on whether they are renting for over a week or less than a week so this if statment is used to differentiate that
        cost = rate * days #This is the rate equation to work out the cost of the car per day

        # Update inventory
        self.availability[car_type][0] -= 1
        print(
            f"\nYou have rented a {car_type.capitalize()} car for {days} days. "
            f"The price of this car is £{rate} per day. Hope you enjoy and see you soon!!!\n"
        )
        return {"car_type": car_type, "days": days, "rate": rate, "cost": cost}

    def return_car(self, car_info):
        car_type = car_info.get("car_type")
        if car_type not in self.availability:
            print("\nSorry that car type is invalid.\n")
            return
        self.availability[car_type][0] += 1
        print("\nCar successfully returned!")
        print("Here is your bill:") # the system prints the customer's personalised bill based on the number of days the car is rented and the type of car rented
        print(
            f"Car Type: {car_info['car_type'].capitalize()}\n"
            f"Rental Period: {car_info['days']} days\n"
            f"Rate per Day: £{car_info['rate']}\n"
            f"Total Cost: £{car_info['cost']}\n"
        )


class Customer: #This is the second class created, that contains all the prompts the user will use to enter their inputs. These generally gather the information needed to use the functions in the first class ('car rental' class)
    def __init__(self, name):
        self.name = name #The name of the user
        self.current_rental = None
# used to print the name of the user when they are searching the car availabaility
    def inquire(self, rental_shop):
        print(f"\n{self.name} is searching for available cars...")
        rental_shop.display_availability()

    def rent_car(self, rental_shop):
        if self.current_rental:
            print(f"\n{self.name}, you already have a rented car. Return it first.\n") 
            return

        # Prompt the user to select a car type
        rental_shop.display_availability()
        car_type_options = list(rental_shop.availability.keys())
        print("Select the car type you would like to proceed with: ")
        for stock, car in enumerate(car_type_options, start=1):
            print(f"{stock}. {car.capitalize()}")

        car_choice = int(input("\nEnter your choice: ")) - 1 #If the car they have chosen is not available the choice will come up as invalid as the availabliity will not be in the range
        if car_choice not in range(len(car_type_options)):
            print("\nSorry, invalid choice.\n")
            return
        car_type = car_type_options[car_choice]

        # Prompts the user to enter the number of days they would like to rent the car for
        days = int(input(f"How many days would you like to rent the {car_type}? "))

        # This processes the action of the car rental
        rental_details = rental_shop.rent_car(car_type, days)
        if rental_details:
            self.current_rental = rental_details
# This message will be displayed if the user has not rented a car but is attempting to return the car. This is not possible as there is no car for the system to return it to
    def return_car(self, rental_shop):
        if not self.current_rental:
            print(f"\n{self.name}, You have not yet rented a car to return.\n")
            return
        rental_shop.return_car(self.current_rental)
        self.current_rental = None


def main(): #the sytem point of entry for the user
    shop = RentalShop()
    customer = Customer("Mr Adeyemi") #the name of the user
# while loop can display the various choices available to the customer- numbered 1-4
    while True:
        print("\nPlease select an option")
        print("1. View the available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Exit")

        choice = int(input("\nEnter your choice: ")) # The customer will unput the numerical value assocated to the action they would like to complete. This refers back to the functions outlined in the classes
        if choice == 1:
            customer.inquire(shop)
        elif choice == 2:
            customer.rent_car(shop)
        elif choice == 3:
            customer.return_car(shop)
        elif choice == 4:
            print("Thank you for using our car rental service!!")
            break
        else:
            print("\nInvalid choice. Please try again.\n") # If the anser the user has given is outside the scope of options they have been given, e.g. if they were to input the number '6' that is an invalid choice as it is not an option


if __name__ == "__main__":
    main()

