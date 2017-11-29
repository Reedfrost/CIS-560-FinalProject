import sys
from query import Query


class assign:

    def display():
        print("\n*** THE FOLLOWING ARE THE POSSIBLE COMMANDS ***\n")
        print("> search <student id>")
        print("> offenders")
        print("> allStudents")
        print("> viewStrikes")
        print("> strike")
        print("> fire <student id>")
        print("> newStrike")
        print("> newStudent")
        print("> schedule")
        print("> quit")
        print(">(Not case sensitive)")

    def menu(id, query):
        command = None;

        # Main user input loop
        while(True):
            try:
                assign.display()
                command = input()
                command = command.lower()
                tokens = command.split()
                if(tokens[0] == "offenders"):
                    print("\nSearching for Students with 3 Strikes...\n")
                    query.list_offenders()
                    # TODO: Call function in query.py to print offenders
                    
                elif(tokens[0] == "allstudents"):
                    print("\nListing all students...\n")
                    # TODO: Call function to print all students and their IDs and their strikes
                    query.searchQuery("all")
                
                elif(tokens[0] == "viewstrikes"):
                    print("\nListing all strikes...\n")
                    # TODO: Call function to print all strikes and their IDs
                    query.viewStrikes()
                
                elif(tokens[0] == "quit"):
                    print("\nGoodbye\n")
                    query.close()
                    break
                
                elif(tokens[0] == "newstrike"):
                    print("\nEnter Name of the New Strike: \n")
                    name = input()
                    print("\nEnter description: \n")
                    description = input()
                    query.newStrike(description, name)
                    # TODO: Call function to create new Strike
                    print("\nCreating Strike: " + name + "...\n")
                
                elif(tokens[0] == "newstudent"):
                    print("\nEnter Name of New Student: \n")
                    name = input()
                    query.newStudent(name)
                    # TODO: Call function to add new student
                    print("\nNew student " + name + " added\n")
                
                elif(tokens[0] == "strike"):
                    print("\nEnter Student ID\n")
                    student = input()
                    print("\nEnter Strike ID\n")
                    strike = input()
                    print("\nEnter Day\n")
                    day = input()
                    print("\nEnter Month\n")
                    month = input()
                    print("\nEnter Year\n")
                    year = input()
                    print("\n" + month)
                    print(year)
                    #Need to index id because it is an object
                    # TODO: Call function to validate student ID
                    if(not query.validateName(student)):
                        print("\nInvalid Student ID\n")
                        continue
                    # TODO: call function to validate strike ID
                    elif(not query.validateStrike(strike)):
                        print("\nInvalid Strike ID\n")
                        continue
                    else:
                    # TODO: if all good call function give student the new strike
                        query.strike(id[0], student, strike, day, month, year)
                        print("\nGiving student with ID " + student + " a new strike...\n")
                
                elif(tokens[0] == "search" and len(tokens) == 2):
                    print("\nSearching for student with ID " + tokens[1] + "...\n")
                    # TODO: Call function to validate student ID
                    print(query)
                    query.searchQuery(tokens[1])
                    if(False):
                        print("\nInvalid Student ID\n")
                        continue
                    # TODO: Call function to display student information
                
                elif(tokens[0] == "fire" and len(tokens) == 2):
                    # TODO: Call function to validate student ID
                    query.fired(tokens[1])
                    if(False):
                        print("\nInvalid Student ID\n")
                        continue
                    while(True):
                        print("\nAre you sure you wish to fire this student? (y/n)\n")
                        confirmation = input()
                        confirmation = confirmation.lower()
                        if(confirmation == "y" or confirmation == "yes"):
                            # TODO: Call function to fire student
                            print("\nStudent with ID " + tokens[1] + " has been fired.\n")
                            break
                        elif(confirmation == "n" or confirmation == "no"):
                            print("\nNot firing the student.\n")
                            break
                        else:
                            print("\n***Invalid confirmation*** (yes/no)\n")
                            
                elif(tokens[0] == "schedule"):
                    print("\nLoading Schedules")
                    query.schedule()
                
                else:
                    print("\n****INVALID COMMAND****\n")
            
            except:
                print("ERROR")


def main():
    if(len(sys.argv) >= 3):
        try:
            # TODO: Call function for user authentication and return id, -1 if invalid
                # assign.menu(sys.argv[1], sys.argv[2])
                queries = Query()
                print(queries)
                id = queries.kramer_login(sys.argv[1], sys.argv[2])
                if(id != -1):
                    assign.menu(id, queries)
                else:
                    print("Invalid Login")
        except:
            print("\n****ERROR OCCURED WITH LOGIN****\n")
    else:
        print("\nInvalid Username or Password\n")


if __name__ == '__main__':
        main()
