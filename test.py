from craigslist_headless import CraigslistHousing

if __name__ == "__main__":
    cl_h = CraigslistHousing(site='portland', area='mlt', category='apa',
                             filters={'max_price': 1400, 'private_room': True,
                                      'search_distance': 3, 'zip_code': 97211, 'dogs_ok': True, 'query': 'yard'
                                      })
    results = cl_h.get_results(sort_by='newest', geotagged=True, include_details=True)
    for result in results:
        print(result)
    cl_h.quit()
