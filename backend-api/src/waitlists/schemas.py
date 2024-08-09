from ninja import Schema
from datetime import datetime
from pydantic import EmailStr


class WaitlistCreateEntrySchema(Schema):
    # Create -> Data
    # WailtlistEntryIn
    email: EmailStr


class WaitlistEntryListSchema(Schema):
    # Create -> Data
    # WailtlistEntryIn
    id: int
    email: EmailStr

class WaitlistEntryDetailSchema(Schema):
    # GET -> Data
    # WailtlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime