class User:
    def __init__(self, username, email, password):
        self.username= username
        self.email = email
        self.password = password
        self.workout = []

class Workout:
    def __init__(self, date, duration, exercises):
        self.date = date
        self.duration = duration
        self.exercises = exercises

        

class FitnessApp:
    def __init__(self):           
        self.users = []

    def register_user(self, username, email, password):
        new_user = User (username, email, password)
        self.users.append (new_user)
    
        return new_user

    def log_workout(self, user, date, duration, exercises):
        new_workout = Workout(date, duration, exercises)
        user.workout.append(new_workout)
        return new_workout
            

def print_separator():
        print("=" * 40)

def main():
    fitness_app = FitnessApp()  

    while True:
        print_separator()
        print("Welcome to your Fitness app")
        print_separator()
        print("1. Register\n2. Log Workout\n3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            fitness_app.register_user(username, email ,password)
            print_separator()
            print("User registered successfully")
  
        elif choice == "2":
            username = input("Enter username:")
            user = next((u for u in fitness_app.users if u.username == username), None)

            if user:
                date = input("Enter workout date (YYYY-MM-DD): ")
                duration = int(input("Enter workout duration (minutes): "))
                exercises = input("Enter exercises (comma- separation: )"). split(',')
                fitness_app.log_workout(user, date, duration, exercises)
                print_separator()
                print(f"Workout logged successfully on {date}")

            else:
                print_separator()
                print("User not found. Please register first.")
    
        elif choice == "3":
            print_separator()
            print("Exiting the fitness app. Goodbye!")
            break

        else:
            print_separator()
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()