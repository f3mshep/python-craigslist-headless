import logging
from craigslist.craigslist import CraigslistHousing

cl_h = CraigslistHousing(site='sfbay', area='sfc', category='roo',
                         filters={'max_price': 1200, 'private_room': True}, log_level=logging.INFO)

# You can get an approximate amount of results with the following call:


for result in cl_h.get_results(sort_by='newest', geotagged=True):
    print(result)