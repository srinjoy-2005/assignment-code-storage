class UsernameAlreadyExist(Exception):
    def __init__(self, username) -> None:
        super().__init__(f"{username} already exists")

class InvalidEmail(Exception):
    def __init__(self, email) -> None:
        super().__init__(f"{email} is invalid")

class InvalidAge(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Invalid Age")

class UnderAge(InvalidAge):
    def __init__(self, age) -> None:
        super().__init__(f"Your age is below the min age req.")


def Validmail(email: str):
    if '@' in email:
        parts = email.split('@')
        if len(parts) == 2 and parts[0] and parts[1]:
            return True
    return False

def get_valid_users(users):
    valid_users = {}
    for username,email,age in users:
        try:
            if username in valid_users.keys():
                raise UsernameAlreadyExist(username)
            if not Validmail(email):
                raise InvalidEmail(email)
            if age <= 0:
                raise InvalidAge(age)
            if age < 16:
                raise UnderAge(age)
            valid_users[username] = {"email":email,"age":age}
        except (UsernameAlreadyExist,InvalidEmail,InvalidAge,UnderAge) as e:
            print(e)
        
    return valid_users

if __name__ == "__main__":
    num = int(input())
    users = []
    for _ in range(num):
        username = input()
        email = input()
        age = int(input())
        users.append((username,email,age))

    valid_users = get_valid_users(users=users)
    print(f"Valid users are: {valid_users}")