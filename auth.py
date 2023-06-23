import json 

class Auth:
    def __init__(self, username):
        self.username = username
    
    @staticmethod
    def getAuth():
        with open("auth.json", "r") as f:
            return json.load(f)
        
    @staticmethod
    def setAuth(data):
        with open("auth.json", "w") as f:
            json.dump(data,f)

        
    def getPassword(self):
        data=Auth.getAuth()
        if self.username in data:
            return data[self.username]
        return None 
    
    def setPassword(self, password):
        data=Auth.getAuth()
        if self.username not in data:
            data[self.username] = password 
            Auth.setAuth(data)
            return True
        return None 

