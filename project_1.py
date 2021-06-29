import csv
def write_into_csv(student_data_list):
    with open('student_data.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()== 0:

            writer.writerow(["Name","Age","Mobile_Number","E-mail.iD"])
            # If we want to use writerow function ,then the argument which we are passing should be in the form of list so.,we need to split the given information into the list

        writer.writerow(student_data_list)


if __name__ == '__main__': # Here this line is the entry point for the entire program and the program execution of the program also starts here
    condition= True
    student_count = 1

    while(condition):

        student_data = input("Enter the information of student #{} in the list as shown here(Name Age Mobile_Number E-mail.iD)  : ".format(student_count))

        #splitting the given information with comma for csv file

        student_data_list= student_data.split(' ')
        print("\nEntered information is : \nName: {}\nAge: {}\nMobile_Number: {}\nE-mail.iD: {}" .format(student_data_list[0],student_data_list[1],student_data_list[2],student_data_list[3],))
        t = input("Please Conform the information you entered with (y/n): ")
        if t =="y":

            write_into_csv(student_data_list)

            condition_check= input("Please type y if you want to enter the next student data else type n : ")
            if condition_check == "y":

                condition= True
                student_count+=1

            elif condition_check == "n":

                condition = False

            elif t =="n":
                print("\nRelax")
                print("\n Please re-enter the values!!")
