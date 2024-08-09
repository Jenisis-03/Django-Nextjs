from ninja import NinjaAPI, Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
from waitlists.api import router as waitlist_router

# Create an instance of NinjaExtraAPI
api = NinjaExtraAPI()

# Register the default JWT controller
api.register_controllers(NinjaJWTDefaultController)

# Add the router to the API
api.add_router("/waitlists", waitlist_router)

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None

@api.get("/hello")
def hello(request):
    print(request)
    return {"message": "Hello World"}

@api.get("/me", response=UserSchema, auth=JWTAuth())
def me(request):
    return request.user
