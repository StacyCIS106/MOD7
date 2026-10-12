user_prompt = input("Do you want to do this program? (yes/no): ")
num_data = 0
while user_prompt == 'yes' or user_prompt == 'YES' or user_prompt == 'Yes':
    last_name = input("Enter your last name: ")
    exam_one = int(input("Enter your score for Exam One: "))
    exam_two = int(input("Enter your score for Exam Two: "))
    average = (exam_one + exam_two) / 2
    print((last_name), average)
    print("Number of data entered: ", num_data)
    num_data += 1
    user_prompt = input("Do you want to do this program? (yes/no): ")
