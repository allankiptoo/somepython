import pandas as pd
import json
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
import requests
from datetime import datetime
first_name = input("Enter your first name: ").strip().capitalize() # Asking for input of first name and storing it in a variable and capitalizing
last_name = input("Enter your last name: ").strip().capitalize() # Asking for input of second name and storing it in a variable and capitalizing
print(f"Hello {last_name}, {first_name}") # Display first and the last name
Unit1_discussion_points = 50  # Points for discussion
Unit1_course_project_points = 50  # Points for course project
Unit1_core_assesment_points = 40  # Points for core assessment
task_maximum_points = 50       #maximum points fr each task
total_points_earned = (Unit1_discussion_points + Unit1_course_project_points + Unit1_core_assesment_points) #summing up all the points
print(f"Total Points Earned: {total_points_earned}")  #printing the total summed points
got_maximum_discussion = Unit1_discussion_points == task_maximum_points #comparing discussion points with the maximum points
got_maximum_course_project = Unit1_course_project_points == task_maximum_points #comparing course project points with the maximum points
got_maximum_core_assessment = Unit1_core_assesment_points == task_maximum_points #comparing core assignment points with the maximum points

# getting output for the points and the maximum points
print(f"Got maximum points for Unit 1 discussion? {got_maximum_discussion}")
print(f"Got maximum points for Unit 1 course project? {got_maximum_course_project}")
print(f"Got maximum points for Unit 1 core assessment? {got_maximum_core_assessment}")
#unit 4 update
total_discussion_points = [Unit1_discussion_points, 50, 50,50,50,50]  #list for total discussion points
total_course_project_points = [Unit1_course_project_points, 50, 45,50,50,10]  #list for course project
total_core_assessment_points = [Unit1_core_assesment_points,0,50,50] #list for core assessment
#Total earned points for each task
total_discussion_score = sum(total_discussion_points)
total_course_project_score = sum(total_course_project_points)
total_core_assessment_score = sum(total_core_assessment_points)
#Total maximum points possible calculation
max_discussion_points = 8 * task_maximum_points
max_course_project_points = 8 * task_maximum_points
max_core_assessment_points = 4 * task_maximum_points
# Displaying of current points out of the possible maximum points
print("Currently you have {} points for discussions out of {}".format(total_discussion_score, max_discussion_points))
print("Currently you have {} points for course projects out of {}".format(total_course_project_score, max_course_project_points))
print("Currently you have {} points for core assessments out of {}".format(total_core_assessment_score, max_core_assessment_points))
# Calculation for maximum grade so far
max_grade_discussion_points = len(total_discussion_points) * task_maximum_points
max_grade_course_project_points = len(total_course_project_points) * task_maximum_points
max_grade_core_assessment_points = len(total_core_assessment_points) * task_maximum_points
# Displaying current scores
print(f"So far you have {total_discussion_score} points for discussions out of {max_grade_discussion_points}")
print(f"So far you have {total_course_project_score} points for course projects out of {max_grade_course_project_points}")
print(f"So far you have {total_core_assessment_score} points for core assessments out of {max_grade_core_assessment_points}")
# Checking if all assignment types have the maximum score so far
def check_maximum_scores(scores, max_grade_points, type_name):
    actual_score = sum(scores)  # Code calculating total score
    if actual_score == max_grade_points:
        print(f"Congrats! You got maximum points for ALL {type_name} homeworks so far!")
    else:
        print(f"Unfortunately you did not get maximum points for ALL {type_name} homeworks")

# Calling def function with the correct variables
check_maximum_scores(total_discussion_points, max_grade_discussion_points, "discussion")
check_maximum_scores(total_course_project_points, max_grade_course_project_points, "course project")
check_maximum_scores(total_core_assessment_points, max_grade_core_assessment_points, "core assessment")
# creating classes to store information and adding properties
class Discussions:
    maximum_points_per_task = 50
    tasks_per_semester = 8
    display_name = "Discussions"

class Course_projects:
    maximum_points_per_task = 50
    tasks_per_semester = 8
    display_name = "Course Projects"

class Core_assessments:
    maximum_points_per_task = 50
    tasks_per_semester = 4
    display_name = "Core Assessments"
    #unit 5
   #Creating Task_type class
class TaskType:
    def __init__(self, name, display_name, tasks_per_semester, maximum_points_per_task):
        self.name = name
        self.display_name = display_name
        self.tasks_per_semester = tasks_per_semester
        self.maximum_points_per_task = maximum_points_per_task
        #reading json file
        # Define the full path to the JSON file
file_path = r"C:/Users/hp/Desktop/pool on this side/2025/nancy/tasks.json"

# Open and read the JSON file
with open(file_path, "r") as file:
    data = json.load(file)
    # List to store task types
task_types = []
# Reading tasks from JSON and creating TaskType objects
for key, value in data["Homeworks"].items():
    task = TaskType(
        name=key,
        display_name=value["DisplayName"],
        tasks_per_semester=value["NumberOfTasksPerSemester"],
        maximum_points_per_task=value["MaximumPointsPerSubmission"]
    )
    task_types.append(task)
    # Calculate the total maximum points 
total_maximum_points = sum(task.tasks_per_semester * task.maximum_points_per_task for task in task_types)

# Displaying the points
print(f"Total maximum points a student can earn in this class: {total_maximum_points}")
#unit 6 update
# Pull request
url = "http://worldtimeapi.org/api/timezone/America/Chicago"

try:
    # API request
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    
    # JSON response
    time_data = response.json()

    #  timestamp
    now_date = datetime.utcfromtimestamp(time_data["unixtime"])
    now_day = now_date.timetuple().tm_yday  # Get the day of the year

    # course start date 
    begin_course_day = datetime(2025, 1, 14).timetuple().tm_yday

    # completed units 
    days_completed = now_day - begin_course_day
    units_completed = int(max(0, days_completed / 7) )  # Prevent negative values
    #ip
    client_ip = response.json()
    client_ip = client_ip.get("client_ip", "Unknown IP")

    # Display 
    print(f"Your public IP address is: {client_ip}")
    print(f"Today's date: {now_date.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Today is day {now_day} of the year.")
    print(f"The course began on day {begin_course_day}.")
    print(f"You have completed {units_completed} Units of 8.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching time data: {e}")


#unit 7
df = pd.read_csv('C:/Users/hp/Desktop/pool on this side/2025/nancy/grades.csv') #this is code for reading the created csv file
# Display the contents of the CSV file
print("\nThis are the contents of the csv file:")   #\n creates a new line 
print(df)  #displaying the contents of the csv
# Display all grades for only discussions
discussion_grades = df[df['type'] == 'discussion']
print("\nThe Discussion Grades are as follows:")
print(discussion_grades)
# Displaying grades for week 1 only
week1_grades = df[['type', 'week1']]
print("\nWeek 1 Grades for All Types are as follows:")
print(week1_grades)
# Extract maximum possible grades from JSON
max_grades = {
    "discussion": data["Homeworks"]["Discussions"]["MaximumPointsPerSubmission"],
    "core_assessment": data["Homeworks"]["CoreAssessment"]["MaximumPointsPerSubmission"],
    "course_project": data["Homeworks"]["CourseProject"]["MaximumPointsPerSubmission"]
}

# Convert all grade columns to numeric, handling errors
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# Function to clean grades
def clean_grade(value, assignment_type):
    if pd.isnull(value):  # Keep NaN values unchanged
        return value
    value = float(value)  # Convert to float
    max_grade = max_grades.get(assignment_type, 50)  # Default max to 50
    return max(0, min(value, max_grade))  # Ensure within range [0, max_grade]

# Apply cleaning function based on assignment type
for index, row in df.iterrows():
    assignment_type = row["type"].lower()  # Ensure type is in lowercase
    if assignment_type in max_grades:
        df.iloc[index, 1:] = df.iloc[index, 1:].apply(lambda x: clean_grade(x, assignment_type))

# Display cleaned data
print("\nCleaned Data:")
print(df)
#Unit 8
# Load CSV file
grades_0 = pd.read_csv('C:/Users/hp/Desktop/pool on this side/2025/nancy/grades_50.csv')

# Extract maximum points from JSON
max_grades = {
    "discussion":data["Homeworks"]["Discussions"]["MaximumPointsPerSubmission"],
    "core_assessment":data["Homeworks"]["CoreAssessment"]["MaximumPointsPerSubmission"],
    "course_project":data["Homeworks"]["CourseProject"]["MaximumPointsPerSubmission"]
}

# Clean grades function
def clean_grade(value, assignment_type):
    if pd.isnull(value):
        return 0
    value = float(value)
    max_grade = max_grades.get(assignment_type, 50)
    return max(0, min(value, max_grade))

# Apply cleaning
for index, row in grades_0.iterrows():
    assignment_type = row["type"].lower()
    if assignment_type in max_grades:
        grades_0.iloc[index, 1:] = row[1:].apply(lambda x: clean_grade(x, assignment_type))

# Calculate total points
grades_0['Total'] = grades_0.iloc[:, 1:].sum(axis=1)
total_points = grades_0['Total'].sum()
total_maximum_points = sum(
    task["NumberOfTasksPerSemester"] * task["MaximumPointsPerSubmission"]
    for task in data["Homeworks"].values()
)

# Display total points
print(f"You have {total_points} out of {total_maximum_points}")

# Calculate percentage
percentage = (total_points / total_maximum_points) * 100
print(f"Your percentage is {percentage:.2f}")

# Letter grade calculation
if percentage > 90:
    letter_grade = 'A'
elif percentage > 80:
    letter_grade = 'B'
elif percentage > 70:
    letter_grade = 'C'
elif percentage > 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display letter grade
print(f"Your letter grade is: {letter_grade}")
