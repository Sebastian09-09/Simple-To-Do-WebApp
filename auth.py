import json 

class Auth:
    def __init__(self, username):
        self.username = username
    
    @staticmethod
    def getAuth():
        '''Function to read data from auth.json'''
        with open("auth.json", "r") as f:
            return json.load(f)
        
    @staticmethod
    def setAuth(data):
        '''Function to write data at auth.json'''
        with open("auth.json", "w") as f:
            json.dump(data,f)

        
    def getPassword(self):
        '''Function to read password of the user'''
        data=Auth.getAuth()
        if self.username in data:
            return data[self.username]
        return None 
    
    def setPassword(self, password):
        '''Function to set new username and password'''
        data=Auth.getAuth()
        if self.username not in data:
            data[self.username] = password 
            Auth.setAuth(data)
            return True
        return None 

