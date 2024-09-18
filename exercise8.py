#exercise 8 task 1
'''
def display_message():
    print("Hello, this is a Python program. I learned to do this while studying AWS re/start")

display_message()
'''

#exercise 8 task 2
'''
def favorite_book(title):
    print(f"My favoriate book is {title}")

favorite_book("To Kill a Mockingbird")
'''

#exercise 8 task 3
'''
def make_shirt(size, message):
    if size =="Large":
        print(f"I love python")
    elif size =="Small":
        print(f"hey small stuff")
    else:
        print(f"hey heres your message {message}")

make_shirt("Large", "I love coding")
make_shirt(message = "large", size = "Love you boo")
'''

#exercise 8 task 4
'''
def describe_city(city="Dublin", country="Ireland"):
    print(f"The city of {city} is in {country}.")

describe_city("Glasgow", "Scotland")
describe_city(country="France", city="paris")
describe_city()
'''

#exercise 8 task 5

#getting input from user
artist_name=input("Please enter name of Artist")
album_name=input("Please enter name of Album")

#create a blank dictonairy list to hold the list of ablums
playlist={"artist": "me", "album": "me again"}

#function to add an ablum to the playlist dic
def create_album_playlist(artist_name, album_name):
    #get input and add it to a list of strings to make album object
    new_album={"artist": artist_name, "album": album_name}
    playlist[new_album] = new_album
    print(playlist)

print(playlist)
create_album_playlist(artist_name, album_name)