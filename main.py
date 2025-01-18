#define  a class for exercise
class Exercise:
    def __init__(self, name, duration_min, intensity):
        self.name = name
        self.duration_min = duration_min
        self.intensity = intensity

#Define class for user
class User:
    def __init__(self,username):
        self.username = username
        self.exercises = []
        self.goalS = {}

    def log_exercise(self, exercise):
        self.exercises.append(exercise)

    def calculate_calories_burned(self):
        total_calories = 0
        for exercise in self.exercises:
            calories=exercise.duration_min*exercise.intensity
            total_calories = calories
        return total_calories
    
    def set_goal(self, goal_type, target_value):
        self.goalS[goal_type] = target_value

    def track_progress(self):
        
        total_calories_burned = self.calculate_calories_burned()
        if 'calories' in self.goalS:
            goal_calories = self.goalS['calories']
            progress_percentage = (total_calories_burned/goal_calories)*100
            return progress_percentage
        else:
            return None
        
#Function to log to Exercise
def log_Exercise(user):
    name=input("Enter the name of the exercise: ")
    duration = int(input("Enter the duration of the exercise in minutes: "))
    intensity = int(input("Enter the intensity of the exercise (1-10): "))
    exercise = Exercise(name, duration, intensity)
    user.log_exercise(exercise)
    print("Exercise logged successfully!")

#Function to set goal
def set_Goal(user):
    goal_type = input("Enter the goal type (e.g., calories) :")
    target_value = int(input("Enter the target value: "))
    user.set_goal(goal_type, target_value)
    print("Goal set successfully!")

# Function to track
def track_progress(user):
    progress = user.track_progress()
    if progress is not None:
        print(f"Progress towards goal: {progress:.2f}%")
    else:
        print("No goal set yes.")

#Main function for user interaction
def main():
    username = input("Enter your username:")
    user = User(username)

    while True:
        print("\n--- Fitness Tracking System ---")
        print("1. Log Exercise")
        print("2. Set Goal")
        print("3. Track Progress")
        print("4. Exit")

        choice = input("Enter u=your choice (1-4):")
        if choice == "1":
            log_Exercise(user)
        elif choice == "2":
            set_Goal(user)
        elif choice =="3":
            track_progress(user)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. please enter a number between 1 and 4")
if __name__ == "__main__":
    main()