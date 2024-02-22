class AuthenticationService:
    def is_authenticated_old(self, id):
        return self.is_authenticated("", id)

    def is_authenticated(self, role, id):
        return id == 12345


class AuthenticationClient:
    def __init__(self, authenticationService):
        self.authenticationService = authenticationService

    def run(self):
        authenticated = self.authenticationService.is_authenticated("", 33)
        print("is authenticated: ", str(authenticated))


class YetAnotherClient:
    def run(self):
        AuthenticationService().is_authenticated_old(100)


if __name__ == "__main__":
    client = AuthenticationClient(AuthenticationService())
    client.run()
