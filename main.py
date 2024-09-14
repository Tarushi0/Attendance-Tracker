import datetime

def get_login_data():
    # Read login data from file and return as dictionary
    login_data = {}
    with open('login_data.txt', 'r') as f:
        for line in f:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(':')
            username = stripped_line[0]
            password = stripped_line[1]
            username = username.lower()
            login_data[username] = password
    return login_data

def get_module_data():
    # Read module data from file and return as dictionary
    module_data = {}
    with open('modules.txt', 'r') as f:
        for line in f:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(',')
            module_code = stripped_line[0]
            module_name = stripped_line[1]
            module_data[module_code] = module_name
    return module_data

def get_attendance_data(module_code):
    # Read attendance data for a given module from file and return as list
    attendance_data = []
    with open(f'{module_code}.txt', 'r') as f:
        for line in f:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(',')
            student_name = stripped_line[0]
            present_count = stripped_line[1]
            absent_count = stripped_line[2]
            attendance_data.append((student_name, int(present_count), int(absent_count)))
    return attendance_data

def write_attendance_data(module_code, attendance_data):
    # Write attendance data for a given module to file
    with open(f'{module_code}.txt', 'w') as f:
        for student_name, present_count, absent_count in attendance_data:
            f.write(f'{student_name},{present_count},{absent_count}\n')
    

def calculate_average_attendance(attendance_data):
    # Calculate and return the average attendance for a given module
    total_days = sum(present_count + absent_count for module_attendance, present_count, absent_count in attendance_data)
    total_present = sum(present_count for module_attendance, present_count, _ in attendance_data)
    return total_present / total_days * 100

def print_attendance_data(module_code, module_name, attendance_data):
    # Print attendance data for a given module
    print(f'Module Record System - Attendance - {module_code} ({module_name})')
    print('-' * 50)
    num_students = len(attendance_data)
    print(f'There are {num_students} students enrolled.\n')
    for i, (student_name, present_count, absent_count) in enumerate(attendance_data, start=1):
        print(f'Student #{i}: {student_name}')
        print(f'1. Present')
        print(f'2. Absent')
        choice = input('> ')
        while choice not in ('1', '2'):
            print('Invalid choice. Please try again.')
            choice = input('> ')
        if choice == '1':
            present_count += 1
        elif choice == '2':
            absent_count += 1
        attendance_data[i-1] = (student_name, present_count, absent_count)
    write_attendance_data(module_code, attendance_data)
    print(f'\n{module_code}.txt was updated with the latest attendance records.')
    input('Press Enter to continue')

def print_average_attendance_data(module_data):
    # Print average attendance data for all modules
    module_attendance_data = []
    for module_code, module_name in module_data.items():
        # Get attendance data for the module
        attendance_data = get_attendance_data(module_code)
        
        # Calculate the total days and total present
        total_days = 0
        total_present = 0
        for _, present_count, absent_count in attendance_data:
            total_days += present_count + absent_count
            total_present += present_count
        
        # Calculate the average attendance for the module
        if total_days != 0:
            average_attendance = (total_present / total_days) * 100
        else:
            average_attendance = 0

        # Add the module attendance data to the list
        module_attendance_data.append((module_name, module_code, average_attendance))
    # Get current date
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    # Create file name
    file_name = f"{current_date}_attendance_stats.txt"
    
    module_attendance_data = []
    for module_code, module_name in module_data.items():
        # Get attendance data for the module
        attendance_data = get_attendance_data(module_code)
        
        # Calculate the total days and total present
        total_days = 0
        total_present = 0
        for _, present_count, absent_count in attendance_data:
            total_days += present_count + absent_count
            total_present += present_count
        
        # Calculate the average attendance for the module
        if total_days != 0:
            average_attendance = (total_present / total_days) * 100
        else:
            average_attendance = 0

        # Add the module attendance data to the list
        module_attendance_data.append((module_name, module_code, average_attendance))

    # Write the module attendance data to file
    with open(file_name, 'w') as f:
        f.write('Module Record System - Average Attendance\n')
        f.write('-' * 50 + '\n')
        f.write('{:<20}{:<10}{:<10}\n'.format('Module Name', 'Module Code', 'Attendance'))
        f.write('-' * 50 + '\n')
        for module_name, module_code, average_attendance in module_attendance_data:
            f.write('{:<20}{:<10}{:<10.2f}%\n'.format(module_name, module_code, average_attendance))

    # Print the module attendance data
    print('Module Record System - Average Attendance')
    print('-' * 50)
    print('{:<20}{:<10}{:<10}'.format('Module Name', 'Module Code', 'Attendance'))
    print('-' * 50)
    for module_name, module_code, average_attendance in module_attendance_data:
        print('{:<20}{:<10}{:<10.2f}%'.format(module_name, module_code, average_attendance))
    print(f"data has been printed in the {file_name} file")
    # Wait for user input before continuing
    input('Press Enter to continue')
def main():
    # Get login data from file
    login_data = get_login_data()

    # Login
    username = input('Username: ').lower()
    password = input('Password: ')
    while login_data.get(username) != password:
        print('Incorrect username or password. Please try again.')
        username = input('Username: ')
        password = input('Password: ')
    print('Login successful.\n')

    # Get module data from file
    module_data = get_module_data()

    # Menu loop
    while True:
        # Print menu options
        print('Module Record System')
        print('-' * 50)
        print('1. Update Attendance Data')
        print('2. View Average Attendance Data')
        print('3. Exit')

        # Get user choice
        choice = input('> ')
        if choice == '1':
            print("Module Record System - Attendance - Choose a Module")
            print("-" * 50)
            print("1. SOFT_6017")
            print("2. SOFT_6018")
            choice = input("> ")
            if choice == '1':
                # Print attendance data for SOFT_6017
                module_code = "SOFT_6017"
                module_name = module_data[module_code]
                attendance_data = get_attendance_data(module_code)
                print_attendance_data(module_code, module_name, attendance_data)
                
            elif choice == '2':
                # Print attendance data for SOFT_6018
                module_code = "SOFT_6018"
                module_name = module_data[module_code]
                attendance_data = get_attendance_data(module_code)
                print_attendance_data(module_code, module_name, attendance_data)

        elif choice == '2':
            # Print average attendance data
            print_average_attendance_data(module_data)

        elif choice == '3':
            # Exit the program
            print('Exiting...')
            break

        else:
            # Invalid choice
            print('Invalid choice. Please try again.')
            input('Press Enter to continue')
if __name__ == '__main__':
    main()