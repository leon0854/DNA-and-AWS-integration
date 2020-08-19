import json
import re
from get_site_list import get_site_list

def get_site_id(event, context):
    str_site_list = str(get_site_list(event, context))
    find_site_id = re.findall(r"'id': '(.*?)', 'siteHierarchy'", str_site_list, re.S)
    return find_site_id