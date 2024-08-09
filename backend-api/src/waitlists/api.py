from ninja import Router
from typing import List
from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema , WaitlistEntryDetailSchema
from django.shortcuts import get_object_or_404

router = Router()

@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

@router.get("{entry_id}/", response=WaitlistEntryDetailSchema)
def list_waitlist_entry(request, entry_id:str):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return obj