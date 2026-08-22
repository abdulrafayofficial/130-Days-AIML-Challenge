class DatabaseConnection:
    def __init__(self,db_name:str):
        self.db_name = db_name

    def __enter__(self):
        print(f'Connecting to user db....{self.db_name}')
        return self

    def __exit__(self, exc_type, exc_val, tb):
        if exc_val:
            print(f"Error occurred: {exc_val}")
                  
        print(f'Connection to user db Closed! {self.db_name}')
        return True # says to the compiler that the error is handled 😎


with DatabaseConnection('my_db_exclusive'):
    print('AHHHHHH')
    # result = 1/0
    print('I AM INSIDE... AHHHHH')




class HTMLTag:
    def __init__(self,tag):
        self.tag = tag


    def __enter__(self):
        print(f"Opening Tag of {self.tag} is <{self.tag}>")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"Closing Tag of {self.tag} is </{self.tag}>")


with HTMLTag('p'):
    print("AHHHHHH")