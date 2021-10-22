import json

class FILE():
    """
    File module allows us to store data on json format.\n
    This can be easily accessibe for the users.\n
    (It uses a dictionary to store which is converted to json object)\n
    """
    def __init__(self,name:str="data") -> None:
        """
        Create a new json file to store data\n
        \n
        Parameters:\n
        :name(str): the name of the file, Eg. data -> data.json\n
        """
        self.name = name
        pass

    def save(self,key,value):
        """
        Save the required data with its key\n
        \n
        Parameters:\n
        :key: the key holds the value\n
        :value: the actual data to be stored\n
        """
        try:
            with open(f"{self.name}.json","r") as f:
                data = json.load(f)

            data[key] = value
        except:
            data = {f"{self.name}'s data":f"{self.name}"}
        
        with open(f"{self.name}.json", 'w') as f:
            json.dump(data, f,indent=4, sort_keys=True)

    def get(self,key):
        """
        Get a previously stored value from the file\n
        \n
        :Parameters\n
        :key: the key which holds the required data\n
        \n
        :Returns\n
        :value: the data contained by the key\n
        """
        try:
            with open(f"{self.name}.json", 'r') as f:
                data = json.load(f)
                value = data[key]
                return value

        except Exception as e:
            print("[Missing] the key supplied is missing",e)
    
    def delete(self,key):
        """
        Delete the data after use\n
        \n
        :Parameters\n
        :key: the key and value you want to delete.\n
        """
        with open(f"{self.name}.json", 'r') as f:
            data = json.load(f)
        try:
            del data[key]
            with open(f"{self.name}.json", 'w') as f:
                json.dump(data, f,indent=4, sort_keys=True)
        except KeyError as e:
            print(e)

