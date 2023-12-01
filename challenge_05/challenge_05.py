class Entry:
    def __init__(self, id, username, email, age, location):
        self.id = id
        self.username = username
        self.email = email
        try:
            self.age = int(age)
        except:
            self.age = False
        self.location= location

    def validate(self):
        return (
            self.id is not None
            and self.id.isalnum()
            and self.username.isalnum()
            and (self.username.lower() in self.email or self.username in self.email)
            and '@' in self.email
            and isinstance(self.age, int)
            and (self.location == '' or isinstance(self.location, str))
        )
    

if __name__ == '__main__':
    message = ''
    with open('db.txt', 'r') as file:
         for line in file:
            fields = line.strip().split(',')
            newEntry = Entry(fields[0],fields[1],fields[2],fields[3],fields[4])

            if newEntry.validate() == False:
                message += newEntry.username[0]

    print(message)