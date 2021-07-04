# Read information from the configuration.txt
class readConfigure:
    def __init__(self):

        # Initialize a blank dictionary
        self.readfile = {}

        # Open and read the file
        f = open("configuration.txt", 'r')
        for line in f:
            line = line.split(", ")
            self.readfile[line[0]] = line[1].splitlines()[0]
    
    # Check if username and password in the configuration file
    def checkUserPass(self, username, password):
        if self.readfile['username'] == username and self.readfile['password'] == password:
            return True
        return False

    # return mathpix api key and id 
    def retMathpixKeys(self):
        return (self.readfile['mathpix_app_id'], self.readfile['mathpix_app_key'])

    # return wolfram aplha api id
    def retWolfAppID(self):
        return self.readfile['wolf_app_id']


