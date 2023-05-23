import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

def load_projects():
    projects = []
    project_name = input('Project file name:')
    try:
        with open(f"{project_name}", "r") as f:
            next(f)
            for line in f:
                name, start_date, priority, estimate, completion = line.strip().split("\t")
                projects.append(Project(name, start_date, int(priority), float(estimate), int(completion)))
    except FileNotFoundError:
        pass
    return projects

def save_projects(projects):
    project_name = input('Project file name to save to:')
    with open(f"{project_name}", "w") as f:
        for project in projects:
            f.write(f"{project.name},{project.start_date.strftime('%d/%m/%Y')},{project.priority},{project.estimate},{project.completion}\n")

def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in filtered_projects:
        print(f"  {project}")

def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_completion = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    project.completion = new_completion
    project.priority = new_priority

def main():
    projects = []

    while True:
        print("\n- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()
        if choice == "l":
            projects = load_projects()
        elif choice == "s":
            save_projects(projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            break

if __name__ == '__main__':
    main()
