'''
Created on Mar 5, 2021
GCDS Database Scanner
Narration: This program allows the user to perform multiple functions using the GCDS data csv file. The user can count, search, change, update, add, delete, and graph data.
The user can also perform multiple functions in one run. All changes of the file will overwrite the old version.
Features: Counting a single term, Counting multiple terms, searching by a single term, searchign by multiple terms, delete a student, add student, update/modify student, graph, loop, try and except.
Log 1.0: Inital version, copy and pasted stub
Log 1.1: Added single search function for names
Log 1.1.2: added rest of the search terms
Log 1.2: Added multivariable search
Log 1.3: added single term search
Log 1.4: added loop and try and except
Log 1.5: Added add student
Log 1.6: Added delete student
Log 1.7: Added modify/update student
Log 1.8: added frequency count using dict.
Log 1.9: Added graph using plotly
Log 1.10: Bug fixing and documentation
Bugs: Person not found, returns error, file not found, returns error
@author: apauley24
'''
#Import tools necessary to delete and graohy
import plotly.express as px
import os
#tool to take the first x amount of items from a dictionary
from itertools import islice


def main():
    print("GCDS Database")
    try:   
    #Try to catch errors
        main_loop = True
        while main_loop == True:
            file_in = open('gcds_data.csv')
            #Opens the file to be able to be read
            
            choice_mode = input("What do you want to do?\n 'MS' for finding a persons data using multiple inputs.\n 'SS' for searching by name, advisor, sex, etc.\n 'AS' for adding a student.\n 'DS' for deleting a student.\n 'CT' for counting a term.\n 'FC' for counting frequency of names, cities, etc, and graphing them.\n 'US' for updating a student.\n 'Quit' for ending the program.")
            #Main choice of mode
            
            if choice_mode.lower() == 'ms':
                search_mode = input("How many terms do you want to search by. (Max 5) > ?")
                if search_mode == '1':
                    first_search = input("What is the 1st variable you want to search by? > ")
                    #Asks user for search term
                    print(single_term_search(file_in, first_search))
                    #Runs function and prints result
                    file_in.close()   
                    #Closes file to avoid opening multiple times
                elif search_mode == '2':
                    first_search = input("What is the 1st variable you want to search by? > ")
                    second_search = input("What is the 2nd variable you want to search by? > ")
                    print(two_term_search(file_in, first_search, second_search))
                    file_in.close()   
                elif search_mode == '3':
                    first_search = input("What is the 1st variable you want to search by? > ")
                    second_search = input("What is the 2nd variable you want to search by? > ")
                    third_search = input("What is the 3rd variable you want to search by? > ")
                    print(three_term_search(file_in, first_search, second_search, third_search)) 
                    file_in.close()   
                elif search_mode == '4':
                    first_search = input("What is the 1st variable you want to search by? > ")
                    second_search = input("What is the 2nd variable you want to search by? > ")
                    third_search = input("What is the 3rd variable you want to search by? > ")
                    fourth_search = input("What is the 4th variable you want to search by? > ")
                    print(four_term_search(file_in, first_search, second_search, third_search, fourth_search))
                    file_in.close()   
                    
                elif search_mode == '5':
                    first_search = input("What is the 1st variable you want to search by? > ")
                    second_search = input("What is the 2nd variable you want to search by? > ")
                    third_search = input("What is the 3rd variable you want to search by? > ")
                    fourth_search = input("What is the 4th variable you want to search by? > ")
                    fifth_search = input("What is the 5th variable you want to search by? > ")
                    print(five_term_search(file_in, first_search, second_search, third_search, fourth_search, fifth_search))
                    file_in.close()   
                
                #Elif block to determine how many variables to search by
                    
                else:
                    print("Please only input an integer from 1 to 5.")
                    file_in.close()   
                    
                    
            elif choice_mode.lower() == 'ss':
                search_choice = input("What do you want to search by?\n '1' for first name.\n '2' for middle name.\n '3' for last name.\n '4' for full name. (First Middle Last) \n '5' for grade.\n '6' for sex.\n '7' for advisor name.\n '8' for city.\n '9' for state.\n '10' for zipcode.")
                if search_choice == '1':
                    first_name = input("What is the first name you want to search by?")
                    first_name = first_name.lower()
                    print(search_first_name(file_in, first_name))
                    file_in.close()   
                    
                elif search_choice == '2':
                    middle_name = input("What is the middle name you want to search by?")
                    middle_name = middle_name.lower()
                    print(search_middle_name(file_in, middle_name))
                    file_in.close()   
                    
                elif search_choice == '3':
                    last_name = input("What is the last name you want to search by?")
                    last_name = last_name.lower()
                    print(search_last_name(file_in, last_name))
                    file_in.close()   
                    
                elif search_choice == '4':
                    full_name = input("What is the full name you want to search by?")
                    full_name = full_name.lower()
                    full_name = full_name.split(' ')
                    #Splits the full name into a list in order to be used in boleans
                    print(search_full_name(file_in, full_name))
                    file_in.close()   
                    
                elif search_choice == '5':
                    grade_number = input("What is the grade you want to search by?")
                    print(search_grade_name(file_in, grade_number))
                    file_in.close()   
                    
                elif search_choice == '6':
                    sex_search = input("What is the sex you want to search by?")
                    sex_search = sex_search.lower()
                    print(search_sex(file_in, sex_search))
                    file_in.close()   
                    
                elif search_choice == '7':
                    advisor_name = input("What is the advisor name you to want search by?")
                    advisor_name = advisor_name.lower()
                    advisor_name = '"' + advisor_name + '"'
                    #Adds quotations to each end because the csv has that for the advisor name.
                    advisor_name = advisor_name.split(' ')
                    
                    print(search_advisor_name(file_in, advisor_name))
                    file_in.close()   
                    
                elif search_choice == '8':
                    city_search = input("What is the city you want to search by?")
                    city_search = city_search.lower()
                    print(search_city(file_in, city_search))
                    file_in.close()   
                    
                elif search_choice == '9':
                    state_search = input("What is the state you want to search by?")
                    state_search = state_search.lower()
                    print(search_state(file_in, state_search))
                    file_in.close()   
                    
                    
                elif search_choice == '10':
                    zip_code_search = input("What is the zipcode you want to search by?")
                    print(search_zip_code(file_in, zip_code_search))
                    file_in.close()   
                    
                else:
                    print(" Please input one of the options")
                    file_in.close() 
                
            elif choice_mode.lower() == 'ds':
                file_in.close()
                file_read = open("gcds_data.csv", 'r')
                #Closes then reopens the csv for read mode
                temp_file = open('temp_file.csv', 'w')
                #creates a new file to write to
                name_del = input("Who do you want to delete? (Firstname Lastname)")
                del_lines = delete_student(file_read, name_del)
                file_read.close()
                temp_file.write(del_lines)
                #Write all of the lines except the deleted student to the temp file
                temp_file.close()
                os.remove('gcds_data.csv')
                #Deletes the gcds csv
                os.rename('temp_file.csv', 'gcds_data.csv')
                #Renames the temporary file to gcds_data.csv, basically replacing it with the new content
            
            if choice_mode.lower() == 'as':
                file_in.close()
                file_append = open('gcds_data.csv', 'a')
                new_student = input('Input the new students information:\n(Firstname,Middlename,Lastname,Grade,Sex,"AdvisorLastname,AdvisorFirstname",Town,State,Zipcode)')
                test_split = new_student.split(',')
                if len(test_split) == 10:
                    new_student = new_student + '\n'
                    file_append.write(new_student)
                #writes in append mode, adding the new student to the end of the csv
                    file_append.close()
                else:
                    print("Not enough data, or commas in wrong places")
                    file_append.close()
            
            elif choice_mode.lower() == 'ct':
                count_choice = input("What do you want to count by?\n '1' for first name.\n '2' for middle name.\n '3' for last name.\n '4' for full name. (First Middle Last) \n '5' for grade.\n '6' for sex.\n '7' for advisor name.\n '8' for city.\n '9' for state.\n '10' for zipcode.")
                if count_choice == '1':
                    first_name = input("What is the first name you want to count by?")
                    first_name = first_name.lower()
                    print(count_first_name(file_in, first_name))
                    file_in.close()   
                    
                elif count_choice == '2':
                    middle_name = input("What is the middle name you want to count by?")
                    middle_name = middle_name.lower()
                    print(count_middle_name(file_in, middle_name))
                    file_in.close()   
                    
                elif count_choice == '3':
                    last_name = input("What is the last name you want to count by?")
                    last_name = last_name.lower()
                    print(count_last_name(file_in, last_name))
                    file_in.close()   
                    
                elif count_choice == '4':
                    full_name = input("What is the full name you want to count by? (First Middle Last)")
                    full_name = full_name.lower()
                    full_name = full_name.split(' ')
                    print(count_full_name(file_in, full_name))
                    file_in.close()   
                    
                elif count_choice == '5':
                    grade_number = input("What is the grade you want to count by?")
                    print(count_grade_name(file_in, grade_number))
                    file_in.close()   
                    
                elif count_choice == '6':
                    sex_search = input("What is the sex you want to count by?")
                    sex_search = sex_search.lower()
                    print(count_sex(file_in, sex_search))
                    file_in.close()   
                    
                elif count_choice == '7':
                    advisor_name = input("What is the advisor name you want to count by?")
                    advisor_name = advisor_name.lower()
                    advisor_name = '"' + advisor_name + '"'
                    advisor_name = advisor_name.split(' ')
                    print(count_advisor_name(file_in, advisor_name))
                    file_in.close()   
                    
                elif count_choice == '8':
                    city_search = input("What is the city you want to count by?")
                    city_search = city_search.lower()
                    print(count_city(file_in, city_search))
                    file_in.close()   
                    
                elif count_choice == '9':
                    state_search = input("What is the state you want to count by?")
                    state_search = state_search.lower()
                    print(count_state(file_in, state_search))
                    file_in.close()   
                    
                    
                elif count_choice == '10':
                    zip_code_search = input("What is the zipcode you want to count by?")
                    print(search_zip_code(file_in, zip_code_search))
                    file_in.close()   
                    
                else:
                    print(" Please input one of the options")
                    file_in.close()
                    
            elif choice_mode.lower() == 'us':
                file_in.close()
                update_choice = input("What do you want to update?\n '1' for first name.\n '2' for middle name.\n '3' for last name. \n '4' for grade.\n '5' for sex.\n '6' for city.\n '7' for state.\n '8' for zipcode.")
                if update_choice == '1':
                    list_value = 0
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                if update_choice == '2':
                    list_value = 1
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                if update_choice == '3':
                    list_value = 2
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                if update_choice == '4':
                    list_value = 3
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                if update_choice == '5':
                    list_value = 4
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                if update_choice == '6':
                    list_value = 7
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                if update_choice == '7':
                    list_value = 8
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                if update_choice == '8':
                    list_value = 9
                    #Elif block to determine which column of the csv to update
                    first_name_update = input("Input the first name of the person you want to update.")
                    last_name_update = input("Input the last name of the person you want to update")
                    updated_value = input("Input your change/updated value.")
                    tfile = open('tempfile.csv', 'w')
                    rfile = open('gcds_data.csv', 'r')
                    for line in rfile:
                        #For loop to read out every line of the csv from top to bottom
                        if first_name_update in line and last_name_update in line:
                            #If statement to check if the line contains the name of the desired student
                            line_split = line.split(',')
                            #Splits the line into a list to compare certain values
                            line_split[list_value] = updated_value
                            #Changes the value in the list to the new one
                            new_line = ','
                            #Sets up a variable to use in join function
                            new_line = new_line.join(line_split)
                            #Joins the list by putting a comma between each value and converting it to string
                            if update_choice == '8':
                                new_line = new_line + '\n'
                            tfile.write(new_line)
                        else:
                            tfile.write(line)
                    tfile.close()
                    rfile.close()
                    os.remove('gcds_data.csv')
                    os.rename('tempfile.csv', 'gcds_data.csv')
                    
                    
                
                
            elif choice_mode.lower() == 'fc':
                frequency_choice = input("What do you want to update?\n '1' for first name.\n '2' for middle name.\n '3' for last name. \n '4' for grade.\n '5' for sex.\n '6' for city.\n '7' for state.\n '8' for zipcode.")
                if frequency_choice == '1':
                    list_value = 0
                if frequency_choice == '2':
                    list_value = 1
                if frequency_choice == '3':
                    list_value = 2
                if frequency_choice == '4':
                    list_value = 3
                if frequency_choice == '5':
                    list_value = 4
                if frequency_choice == '6':
                    list_value = 7
                if frequency_choice == '7':
                    list_value = 8
                if frequency_choice == '8':
                    list_value = 9
                count_freq = {}
                #Sets up a blank dictionary
                for line in file_in:
                    if frequency_choice == '8':
                        line = line.strip('\n')
                        line = line + ','
                    #If statement to check for zipcode because the zipcode contains a new line
                    split_line = line.split(',')
                    if (split_line[list_value] in count_freq):
                    #Checks if the value from the csv is in the dictionary
                        count_freq[split_line[list_value]] += 1
                        #Adds one to the count of the dictionary
                    else:
                        count_freq[split_line[list_value]] = 1
                        #Adds the value to the dictionary
                count_freq = dict(sorted(count_freq.items(), key=lambda count_freq: count_freq[1], reverse=True))
                #Sorts the dictionary from  largest to smallest
                print(count_freq)
                graph_question = input("Would you like to graph this data? 'Y' for yes.(Can only show top 10 results)")
                if graph_question.lower() == 'y':
                    first_values = 10
                    #Sets up a variable to use in later function
                    nth_items = take_first_nth_values(first_values, count_freq.items())
                    #Function to take the first nth values in a dictionary

                    y_values, x_values = zip(*nth_items.items())
                    #Splits the dictionary into y values and x values
                    fig = px.pie(values=x_values, names=y_values, title="Result Of Counting. Only showing top 10 results")
                    #creates a graph from y and x values
                    fig.show()
                    #Shows graph by creating it on web browser
                    
                    
                        
                    
                
                    
            elif choice_mode.lower() == 'quit':
                main_loop = False
                print("Done!")
                
            else:
                print("Please input one of the options")
                file_in.close()
                                          
    
    except:
        print("Something went wrong. Person not found")

def take_first_nth_values(first_values, iterable):
    return dict(islice(iterable, first_values))
    #Returns the first nth values in a dictionary


def delete_student(file_read, name_del):
    total_line = ''
    for line in file_read:
        split_line = line.split(',')
        split_name = name_del.split(' ')
        if split_line[0] != split_name[0] or split_line[2] != split_name[1]:
            #Checks if the last name and first name fit the line
            total_line = total_line + line
            #Adds the total line to later write it to a function
    return total_line
    
def single_term_search(file_in, first_search):
    print(file_in)
    match_counter = 0
    data_string = ''
    for line in file_in:
        print(line)
        if first_search in line:
            print(line)
            data_string = data_string + line
            match_counter = match_counter + 1
    if match_counter == 0:
        return "No Match"
    else:
        return data_string.replace(',', ' ')

def two_term_search(file_in, first_search, second_search):
    match_counter = 0
    data_string = ''
    for line in file_in:
        if first_search in line and second_search in line:
            data_string = data_string + line
            match_counter = match_counter + 1
    if match_counter == 0:
        return "No Match"
    else:
        return data_string.replace(',', ' ')
    
def three_term_search(file_in, first_search, second_search, third_search):
    match_counter = 0
    data_string = ''
    for line in file_in:
        if first_search in line and second_search in line and third_search in line:
            data_string = data_string + line
            match_counter = match_counter + 1
    if match_counter == 0:
        return "No Match"
    else:
        return data_string.replace(',', ' ')

    
def four_term_search(file_in, first_search, second_search, third_search, fourth_search):
    match_counter = 0
    data_string = ''
    for line in file_in:
        if first_search in line and second_search in line and third_search in line and fourth_search in line:
            data_string = data_string + line
            match_counter = match_counter + 1
    if match_counter == 0:
        return "No Match"
    else:
        return data_string.replace(',', ' ')
    
def five_term_search(file_in, first_search, second_search, third_search, fourth_search, fifth_search):
    match_counter = 0
    data_string = ''
    for line in file_in:
        if first_search in line and second_search in line and third_search in line and fourth_search in line and fifth_search in line:
            data_string = data_string + line
            match_counter = match_counter + 1
    if match_counter == 0:
        return "No Match"
    else:
        return data_string.replace(',', ' ')

def search_full_name(file_in, full_name):
    counter = 0
    data_first = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[0:2] == full_name[0:2]:
            data_first = data_first + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data_first.replace(',', ' ')

def search_first_name(file_in, first_name):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[0] == first_name:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def search_middle_name(file_in, middle_name):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[1] == middle_name:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def search_last_name(file_in, last_name):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[2] == last_name:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def search_grade_name(file_in, grade_number):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[3] == grade_number:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def search_sex(file_in, sex_search):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",") 
        if list_of_words[4] == sex_search:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def search_advisor_name(file_in, advisor_name):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",") 
        list_of_words[6] = list_of_words[6].strip(' ')

        if list_of_words[5:7] == advisor_name:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def search_city(file_in, city_search):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[7] == city_search:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def search_state(file_in, state_search):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[8] == state_search:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')
    
def search_zip_code(file_in, zip_code_search):
    counter = 0
    data = ''
    for line in file_in: 
        line = line + ','
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  
        if zip_code_search in list_of_words[9]:
            data = data + line
            counter = counter + 1
    if counter == 0:
        return("No Match")
    else: 
        return data.replace(',', ' ')

def count_first_name(file_in, first_name):
    counter = 0
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[0] == first_name:
            counter = counter + 1
    return counter

def count_middle_name(file_in, middle_name):
    counter = 0
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[1] == middle_name:
            counter = counter + 1
    return counter

def count_last_name(file_in, last_name):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[2] == last_name:
            data = data + line
            counter = counter + 1
    return counter

def count_full_name(file_in, full_name):
    counter = 0
    data_first = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[0:2] == full_name[0:2]:
            data_first = data_first + line
            counter = counter + 1
    return counter

def count_grade_name(file_in, grade_number):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[3] == grade_number:
            data = data + line
            counter = counter + 1
    return counter

def count_sex(file_in, sex_search):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[4] == sex_search:
            data = data + line
            counter = counter + 1
    return counter

def count_advisor_name(file_in, advisor_name):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",") 
        list_of_words[6] = list_of_words[6].strip(' ')

        if list_of_words[5:7] == advisor_name:
            data = data + line
            counter = counter + 1
    return counter

def count_city(file_in, city_search):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[7] == city_search:
            data = data + line
            counter = counter + 1
    return counter

def count_state(file_in, state_search):
    counter = 0
    data = ''
    for line in file_in: 
        
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  

        if list_of_words[8] == state_search:
            data = data + line
            counter = counter + 1
    return counter

def count_zip_code(file_in, zip_code_search):
    counter = 0
    data = ''
    for line in file_in: 
        line = line + ','
        lower_line = line.lower()
        list_of_words = lower_line.split(",")  
        if zip_code_search in list_of_words[9]:
            data = data + line
            counter = counter + 1
    return counter

if __name__ == "__main__":
    main()