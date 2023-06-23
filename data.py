import json 
class Data:
    def __init__(self,username):
        self.username = username 

    @staticmethod
    def getData():
        with open("data.json","r") as f:
            return json.load(f)
    
    @staticmethod
    def setData(data):
        with open("data.json","w") as f:
            json.dump(data,f)

    def getUserData(self):
        data=Data.getData()
        return data[self.username] if self.username in data else {}
    
    def setUserData(self, task):
        data=Data.getData()
        if self.username not in data:
            data[self.username] = {}
        data[self.username][task] = "pending"
        Data.setData(data)
    
    def delUserData(self,task):
        data = Data.getData()
        del data[self.username][task]
        Data.setData(data)
    
    def updUserData(self,task,update):
        print(task , update)
        data=Data.getData()
        data[self.username][task] = update
        Data.setData(data)