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
        if "calories" in self.goalS:
            goal_calories = self.goalS["calories"]
            progress_percentage = (total_calories_burned/goal_calories)*100
            return progress_percentage
        else:
            return none
        
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
