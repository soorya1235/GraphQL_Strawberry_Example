import strawberry

@strawberry.type
class User:
    name: str

@strawberry.type
class Shobha:
    name: str

def get_shobha(self) -> Shobha:
    return User(name="Shobha")   


def get_lastuser(self) -> User:
    return User(name="soorya")   

@strawberry.type
class Query:
    last_user: User = strawberry.field(resolver=get_lastuser)
    first_user : Shobha = strawberry.field(resolver=get_shobha)

schema = strawberry.Schema(query=Query)    
