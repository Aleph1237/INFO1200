#import csv and sys
import csv
import sys


#global constant for file name, it will make a new file if there is none. Sadly, it is located in the home directory of the user instead of the directory containing the program file.
FILENAME = "movies_test.csv"

# exit program functioin
def exit_program():
    #print exit message after using sys.exit()
    print("Terminating program.")
    sys.exit()


# opens and reads movies from csv files
def read_movies():
    # attempts to open and read file
    try:
        #declare movies list
        movies = []
        #opens file using reader object
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            # add file contents to movies list
            for row in reader:
                movies.append(row)
        return movies
        # error if file not found
    except FileNotFoundError as e:
        #print(f"Could not find {FILENAME} file.")
        #exit_program()
        return movies
    #all other exceptions
    except Exception as e:
        #prints out the exception type and exits the program
        print(type(e), e)
        exit_program()


#open file and write to it
def write_movies(movies):
    #try to open file for writing
    try:
        #open file using writer object
        with open(FILENAME, "w", newline="") as file:
            ## raise BlockingIOError("Tests the OSError exception.")
            writer = csv.writer(file)
            #write the entered movies to the file
            writer.writerows(movies)
    except OSError as e:
        print(type(e), e) 
        exit_program()
    #exception for all other exceptions
    except Exception as e:
        #print the exception type and exit the program
        print(type(e), e)
        exit_program()


#iterates through movies list and lists them
def list_movies(movies):
    #for loop to iterate through the movies
    for i, movie in enumerate(movies, start=1):
        #print each movie row 
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
   

#add movie to the file
def add_movie(movies):
    #retieves user inut for the new movie
    name = input("Name: ")
    while True:
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Invalid year, try again")
            continue
        if year <= 0:
            print("Year must be greater than 0")
            continue
        else:
            break
    #append movie info to the list
    movie = [name, year]
    movies.append(movie)
    #write movie to the file
    write_movies(movies)
    #print success message
    print(f"{name} was added.\n")


#remove a movie from the list
def delete_movie(movies):
    #while loop to ask user for valid movie to delete
    while True:
        #try to check for a valid number for movie
        try:
            number = int(input("Number: "))
            #catching value errors
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        #further validation for range
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    #remove the movie from the movies list
    movie = movies.pop(number - 1)
    #write the modified list to the file
    write_movies(movies)
    #print success message
    print(f"{movie[0]} was deleted.\n")


#display the command menu and the program name
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    


#execute main code
def main():
    #show main menu
    display_menu()
    #read movied from the file
    movies = read_movies()
    #while true, continue to ask for user command
    while True:    
        #check what command is indicated by user    
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


# checks if current module is main module
if __name__ == "__main__":
    main()
