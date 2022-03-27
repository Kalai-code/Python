# Learning functions

def display_message():
    print("\nI am learning about functions")
    
def favorite_book(title):
    print(f"\nOne of my favorite books is {title}.")

def make_shirt(text,size='L'):
    print(f"\nThe size of the shirt is '{size}' and the message '{text}' will be printed on the shirt")

def city_country(city,country):
    print(f"\n \"{city.title()}, {country.title()}\"")

def show_messages(short_text_messages):
    for messages in short_text_messages:
        print(f"\n {messages}")
        

   
def send_messages(short_text_messages):
    while short_text_messages:
        list_message = short_text_messages.pop()
        print(f"\n {list_message}")
        sent_messages.append(list_message)
#calling functions  
#display_message()
#favorite_book("Alice in Wonderland")
#make_shirt('Hello','S')
#make_shirt(text = "Have a good day",size='M')
#make_shirt(text = "I Love Python")
#make_shirt("I Love Python",'M')
#make_shirt("Lovely Day",'S')

city_country('santiago','chile')

text_messages = ["Hello There","Nice to meet you","Have a great day"]
#show_messages(text_messages)

#make a copy of list and then print the messages
list_message = ''
sent_messages = []
send_messages(text_messages[:])
print("\n original messages:")
for msg in text_messages:
    print(msg)
print("\n Sent messages:")
for message in sent_messages:
    print(message)
