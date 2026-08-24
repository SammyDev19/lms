class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, admin_username, admin_password):
        if admin_username == self.username and admin_password == self.password:
            return True
        else:
            return False


