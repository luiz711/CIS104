title = input("Enter the name of your book: ")
author = input("Enter the name of author: ")
publish_year = int(input("Enter year it was published: "))
page_numbers = int(input("Enter the total number of pages: "))
current_year = 2019
book_age = current_year - publish_year

if (book_age < 10):

    print("This book is younger than 10 years old!")

else:

    print("This book is at least 10 years old!")



if (page_numbers < 100):

    print("This book is a short book.")

elif (page_numbers >= 100 and page_numbers <= 300):

    print("This book is an average book.")

else:

    print("This book is a long book.")