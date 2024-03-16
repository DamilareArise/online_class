class UBA:
    def __init__(self):
        self.name = 'UBA'
        self.Branch = 'HQrts'

      
    def home(self):
        print(f'''
                Welcome to {self.name} {self.Branch}
        
        1. Sign in 
        2. Sign up

        ''')
    def landing_page(self):

        print(f'''
                Welcome to {self.name} {self.Branch}
        
        1. Deposit
        2. WIthdraw

        ''')

    def deposit(self):
        pass

# print(__name__)

# headbranch = UBA()
# headbranch.home()
    
if __name__ == '__main__':
    headbranch = UBA()
    headbranch.home()