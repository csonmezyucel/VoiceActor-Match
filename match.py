import urllib.request
import re

print("-----------------------------------------------------------------------")
print("Look up which shows you watched feature an actor of your choosing:")
print("")
print("\t1. Type in how many My Anime List lists you will enter in for search")
print("\t2. Type in the links to those lists")
print("\t3. Type in the My Anime List link to the voice actor of your choosing")
print("-----------------------------------------------------------------------")

# Taking user input the determine the number of lists to search
number = int(input("Number of lists to search: "))
print("-----------------------------------------------------------------------")
watched = set() # Initializing set to put all shows the user watched
finder = re.compile(r"(anime_title&quot;:&quot;)([^;]+)(&quot)") # Regular expression to match names of shows in the url given by user

for i in range(number):
    input_question = "Link to your anime list (" +  str(i + 1) + "): "
    anime_list = input(input_question) # Asking user input for the url to their list
    print("-----------------------------------------------------------------------")
    a = urllib.request.urlopen(anime_list) # Opening url (anime list)
    s = a.read().decode("utf-8") # Decoding it in utf-8 format
    a.close() # Closing url
    for i in re.findall(finder, s): # Adding the watched shows from the url
        watched.add(i[1])

b = urllib.request.urlopen(input("Link to the voice actor's page: ")) # Opening url (voice actor)

z = b.read().decode("utf-8") # Decoing it in utf-8 format
b.close() # Closing url

print("-----------------------------------------------------------------------")
print("Matching Roles: ")
print("----------------")

for i in watched: # Printing out matches
    if z.find("js-people-title\">"+i+"</a></div>") != -1:
        print("\t" + i)

print("-----------------------------------------------------------------------")