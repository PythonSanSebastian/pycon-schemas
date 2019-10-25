import json
import os

from .reader import get_schema


sponsor_schema = get_schema('sponsor')
sponsorships_schema = get_schema('sponsorships')
talk_schema = get_schema('talk')
submission_schema = get_schema('submission')
