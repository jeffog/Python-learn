
import urllib

def read_text():
    quotes = open("thequickbrown.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("No profanities found")
    else:
        print("Error")

read_text()


