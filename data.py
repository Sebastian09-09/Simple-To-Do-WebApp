import json 
class Data:
    def __init__(self,username):
        self.username = username 

    @staticmethod
    def getData():
        '''Function to read data from data.json'''
        with open("data.json","r") as f:
            return json.load(f)
    
    @staticmethod
    def setData(data):
        '''Function to write data in data.json'''
        with open("data.json","w") as f:
            json.dump(data,f)

    def getUserData(self):
        '''Returns users tasks'''
        data=Data.getData()
        return data[self.username] if self.username in data else {}
    
    def setUserData(self, task):
        '''ads new user task'''
        data=Data.getData()
        if self.username not in data:
            data[self.username] = {}
        data[self.username][task] = "pending"
        Data.setData(data)
    
    def delUserData(self,task):
        '''deletes users task'''
        data = Data.getData()
        del data[self.username][task]
        Data.setData(data)
    
    def updUserData(self,task,update):
        '''updates users task'''
        print(task , update)
        data=Data.getData()
        data[self.username][task] = update
        Data.setData(data)