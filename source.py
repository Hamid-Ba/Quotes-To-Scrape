from secrets import choice
from bs4 import BeautifulSoup

from Blog import Blog

quotes_List = []
page_index = 1

def again(answer = 'n') :
     if answer.lower().strip() == 'y' :
        return True
     else : return False

# Fill Quotes List
while True :
    page = Blog(f"https://quotes.toscrape.com/page/{page_index}/")
    page_content  = page.get_content_page()

    page_html = BeautifulSoup(page_content , "html.parser")

    quotes = page_html.find_all(class_ = 'quote')

    for quote in quotes :
        quotes_info = {
            'text' : quote.find(class_ = 'text').string,
            'author' : quote.find(class_ = 'author').string.lower(),
            'author_link' : f"https://quotes.toscrape.com/{quote.a.get('href')}"
        }
        quotes_List.append(quotes_info)

    # If Next Page Exists 
    if page_html.nav.li['class'][0] == 'next':
        page_index += 1
    else : break

# Game Logic
willingToPlay = True

while willingToPlay :
    willingToPlay = False
    the_quote = choice(quotes_List)

    author_page = Blog(the_quote['author_link'])
    page_content = author_page.get_content_page()

    page_html = BeautifulSoup(page_content,"html.parser")

    born_date = page_html.find(class_ = "author-born-date").string
    born_place = page_html.find(class_ = "author-born-location").string

    the_quote['born_place'] = f"{born_date} in {born_place}"
    chances = 3

    while chances >= 0 :
        print("*" * 10)
        print(f"Here's The Quote:\n{the_quote['text']}")
        answer = input("Whose Above Quote Belong To ? ")

        chances -= 1
        # User Won
        if answer.lower().strip() == the_quote['author'] :
            want_to_continue =  input("Well Done ;) , Do You Want To Continue ?(press y)")
            if again(want_to_continue) :
                willingToPlay = True
            else : 
                willingToPlay = False
            break
        
        elif chances == 2 :
            print(f'HELP : The author born info is {the_quote["born_place"]}')

        elif chances == 1 :
            print(f'HELP : The Name Starts With {the_quote["author"][0]}')
        
        elif chances == 0 :
            print(f'HELP : The LastName Starts With {the_quote["author"].split(" ")[1][0]}')

        else :
            print(f"You Lose , The Author Is : {the_quote['author']}")
            want_to_continue =  input("Do You Want To Continue ?(press y)")
            if again(want_to_continue) :
                willingToPlay = True
            else : 
                willingToPlay = False
            break