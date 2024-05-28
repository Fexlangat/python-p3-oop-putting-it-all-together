#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def page_count(self, value):
         if value != int:
            print ("page_count must be an integer\n")
         else:
             self.page_count = value

    def page_count(self):
        return self._page_count
      
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    
    

    
    

  
  
  
  
  
  
  
  
  
  
  
  
    # def requires_int(self,  page_count):
    #     if page_count != int():
    #         print ("page_count must be an integer")
       