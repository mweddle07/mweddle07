class Employee:
    #define class
    def __init__(self, name, number):
            self.__name = name
            self.__number = number
            
     #set attributes      
    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number
        
    #return attributes
    def get_name(self, name):
        return self.__name
    def get_number(self, number):
        return self.number