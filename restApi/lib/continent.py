""" Continent lib """

from countrycode import countrycode

def _error(msg):
    """ Utility to handle custom errors (see response mapping) """
    raise Exception("[BadRequest] %s" % msg)

def continent_by_country_name(event):
    """ Get continent name (e.g. "Europe"), given a country name (e.g. "Italy") """
    country_name = event.get('country')

    if not country_name:
        return _error("Invalid event (required country)")

    continent = countrycode(codes=[country_name], origin="country_name", target='continent')

    if not continent:
        return _error("Invalid country: %s" % country_name)

    return {
        "continent": next(iter(continent)),
    }
