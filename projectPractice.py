booklist=[]
record=int(input("Enter limit: "))
for i in range(record):
    bookname=input("Enter Book Title: ")
    bookauthor=input("Enter Author Name: ")
    bookprice=int(input("Enter Price of the Book: "))
    booklist.append(
    {
        'BookTitle':bookname,
        'BookAuthor':bookauthor,
        'BookPrice':bookprice,
    }
)
    header=f"{'Booktitle':<20}{'BookAuthor':<20}{'BookPrice':<20}"
    print(header)
    for data in booklist:
        row = f"{data['BookTitle']:<20} {data['BookAuthor']:<20} {data['BookPrice']:<20}"
        print(row)