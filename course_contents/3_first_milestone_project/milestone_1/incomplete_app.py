
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movies():
    
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    

def list_movies(movies):
    print(movies)
    

def  find_movies():
        show_movie(movies)
        
        
def show_movie(movie):
     for movi in movie:
            print("Movie title",movi['title'])
            print("Movie director",movi['director'])
            print("Realeased Movie year",movi["year"])


def select_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movies()
        elif selection == "l":
           list_movies(movies)
        elif selection == "f":
           find_movies() 
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)
select_menu()
