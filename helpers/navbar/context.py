from gallery.models import Gallery
from section.models import Section
import pandas
import json


def navigation_sections():
    active_sections = Section.objects.values('name').filter(is_active=True).order_by('id')
    sections = [i['name'] for i in active_sections]
    active_galeries = Gallery.objects.values('name', 'section__name').filter(is_active=True).order_by('id')
    df = pandas.DataFrame(active_galeries)
    df = df.groupby('section__name')['name'].agg(','.join).to_json()
    res = json.loads(df)
    result = {k: v.split(',') for k, v in res.items()}
    per_section = {}
    for section in sections:
        for section_name, gallery in result.items():
            if section_name == section:
                per_section.update({section: gallery})
                break
            else:
                per_section.update({section: []})
    return per_section
