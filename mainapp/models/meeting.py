from django.db import models

from .committee import Committee
from .default_fields import DefaultFields
from .file import File
from .location import Location
from .meeting_series import MeetingSeries
from .person import Person


class Meeting(DefaultFields):
    name = models.CharField(max_length=1000)
    cancelled = models.BooleanField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    locations = models.ForeignKey(Location, null=True, blank=True)
    # There are cases where mutliple committes have a joined official meeting
    committees = models.ManyToManyField(Committee, blank=True)
    # Only applicable when there are participants without an organization
    persons = models.ManyToManyField(Person, blank=True)
    invitation = models.ForeignKey(File, null=True, blank=True, related_name="meeting_invitation")
    results_protocol = models.ForeignKey(File, null=True, blank=True, related_name="meeting_results_protocol")
    verbatim_protocol = models.ForeignKey(File, null=True, blank=True, related_name="meeting_verbatim_protocol")
    # Sometimes there are additional files atttached to a meeting
    auxiliary_files = models.ManyToManyField(File, blank=True, related_name="meeting_auxiliary_files")
    meeting_series = models.ForeignKey(MeetingSeries, null=True, blank=True)
