# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:32:09 2019

@author: DELL
"""

class User(object):
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        return self.email
    def change_email(self, new):
        self.email = new
    def __repr__(self):
        return 'User {}, email: {}, books read : {}'.format(self.name, self.email, len(self.books))
    def __eq__(self, other):
        return (self.name ==other) and (self.email == other)
    def read_book(self, book, rating = None):
        if (rating!=None):
            self.books[book] = rating
    def get_average_rating(self):
        total = 0
        count = 0 
        for i in self.books.values():
            if (i!=None):
                total +=i
                count +=1
        return total/count
    
                

class Book(object):
    def __init__(self, title, isbn, price = 0):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = price
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, new):
        self.isbn = new
        print('Isbn has been updated')
    def add_rating(self, rating):
        a = rating
        if (a!=None):
            
            if (a<=4) and (a>=0): 
                self.ratings.append(rating)
            else :
                print ('Invalid rating')
    def __eq__(self, other):
        return (self.title == other) and (self.isbn == other)
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __repr__(self):
        return self.title
    
    def get_average_rating(self):
        total = 0
        count = 0
        for i in self.ratings:
            if(i!=None):
                total+=i
                count+=1
        return total/count
    

class Fiction(Book):
    def __init__(self, title, author, isbn, price = 0):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price = 0):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        p = self.level
        a = p[0]
        if (a=='a') or (a=='o') or (a=='i') or (a=='u') or (a=='e'):
            p= 'an ' + p
        else:
            p = 'a ' + p
        return '{}, {} manual on {}'.format(self.title, p, self.subject)
    
class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
    def create_book(self, title, isbn):
        return Book(title, isbn)
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    def add_book_to_user(self, book, email, rating = None ):
        if email in self.users :
            book.add_rating(rating)
            self.users[email].read_book(book, rating)
            self.books[book]= self.books.get(book,0) +1
        else:
            print('User with email {} does not exist'.format(email))
    def add_user(self, name, email, user_books = None):
        if email in self.users:
            print('This email has been used')
        else: 
            i = User(name, email)
            self.users[email]=i
        if (user_books!=None):
            for i in user_books:
                self.add_book_to_user(i, email)
   
    def print_catalog(self):
        print('Catalog:')
        for i in self.books:
            print ('{} with rating {}'.format(i, i.ratings))
    def print_users(self):
        print('List of users:')
        for i in self.users.values():
            print(i)
    def most_read_book(self):
        a = -1
        b = None
        for i in self.books:
            if(self.books[i]>a):
                a = self.books[i]
                b = i
        return 'The most read book is {} with number of readers is {}'.format(b,a)
    def highest_rated_book(self):
        a=-1
        b = None
        for i in self.books:
            if(a<i.get_average_rating()):
                a = i.get_average_rating()
                b = i
        return 'The highest rated book is {} with the average rating {}'.format(b, a)
    
    def most_positive_user(self):
        b = -1
        a = None
        for i in self.users.values():
            if (b<i.get_average_rating()):
                b = i.get_average_rating()
                a = i
        return 'The most positive user is {} with average rating of {}'.format(a,b)
    
    def __repr__(self):
        print('Welcome this TomeRater:')
        self.print_users()
        self.print_catalog()
        return('Have a nice day')
    def __eq__(self, other):
        return (self.users==other) and (self.books == other)
       
        
        



            
    