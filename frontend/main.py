import sys
import query.py as query

class assign:
    def display():
        print("\n*** THE FOLLOWING ARE THE POSSIBLE COMMANDS ***\n")
        print("> search <student id>")
        print("> offenders")
        print("> strike <student id> <strike id>")
        print("> fire <student id>")
        print("> newStrike")
        print("> quit")
        print(">(Not case sensitive)")
    def menu(id, query):
        command = None;

        #Main user input loop
        while(True):
            try:
                assign.display()
                command = input()
                command = command.lower()
                tokens = command.split()
                if(tokens[0] == "offenders"):
                    print("\nSearching for Students with 3 Strikes...\n")
                    #TODO: Call function in query.py to print offenders
                elif(tokens[0] == "quit"):
                    print("\nGoodbye\n")
                    break
                elif(tokens[0] == "newstrike"):
                    print("\nEnter Name of the New Strike: \n")
                    name = input()
                    print("\nEnter description: \n")
                    description = input()
                    #TODO: Call function to create new Strike
                    print("\nCreating Strike: " + name + "...\n")
                elif(tokens[0] == "strike" and len(tokens) == 3):
                    print("\nGiving student with ID " + tokens[1] + " a new strike...\n")
                    #TODO: Call function to validate student ID
                    if(False):
                        print("\nInvalid Student ID\n")
                        continue
                    #TODO: call function to validate strike ID
                    if(False):
                        print("\nInvalid Strike ID\n")
                        continue
                    #TODO: if all good call function give student the new strike
                elif(tokens[0] == "search" and len(tokens) == 2):
                    print("\nSearching for student with ID " + tokens[1] + "...\n")
                    #TODO: Call function to validate student ID
                    if(False):
                        print("\nInvalid Student ID\n")
                        continue
                    #TODO: Call function to display student information
                elif(tokens[0] == "fire" and len(tokens) == 2):
                    #TODO: Call function to validate student ID
                    if(False):
                        print("\nInvalid Student ID\n")
                        continue
                    while(True):
                        print("\nAre you sure you wish to fire this student? (y/n)\n")
                        confirmation = input()
                        confirmation = confirmation.lower()
                        if(confirmation == "y" or confirmation == "yes"):
                            #TODO: Call function to fire student
                            print("\nStudent with ID " + tokens[1] + " has been fired.\n")
                            break
                        elif(confirmation == "n" or confirmation == "no"):
                            print("\nNot firing the student.\n")
                            break
                        else:
                            print("\n***Invalid confirmation*** (yes/no)\n")
                else:
                    print("\n****INVALID COMMAND****\n")
            except:
                print("ERROR")
def main():
    if(len(sys.argv) >= 3):
        try:
            #TODO: Call function for user authentication and return id, -1 if invalid
            if(True):
                assign.menu(sys.argv[1], sys.argv[2])
            else:
                print("Invalid Login")
        except:
            print("\n****ERROR OCCURED WITH LOGIN****\n")
    else:
        print("\nInvalid Username or Password\n")
if __name__ == '__main__':
        main()
