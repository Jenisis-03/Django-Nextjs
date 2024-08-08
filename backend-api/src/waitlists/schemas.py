from ninja import Schema
from datetime import datetime
from pydantic import EmailStr


class WaitlistCreateEntrySchema(Schema):
    # Create -> Data
    # WailtlistEntryIn
    email: EmailStr

class WaitlistEntryDetailSchema(Schema):
    # GET -> Data
    # WailtlistEntryOut
    email: EmailStr
    timestamp: datetime