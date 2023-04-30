import strawberry  # new
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter  # new


# new
@strawberry.type
class Query:
  @strawberry.field
  def hello(self) -> str:
    return "Hello World"
  @strawberry.field
  def getname(self) -> str:
      return "hello soorya"

schema = strawberry.Schema(Query)  # new
graphql_app = GraphQLRouter(schema)  # new
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")  # new


@app.get("/")
def ping():
    return {"ping": "pong"}