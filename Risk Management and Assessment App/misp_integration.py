from pymisp import PyMISP
import os
from dotenv import load_dotenv

load_dotenv()

MISP_URL = os.getenv('MISP_URL')
MISP_KEY = os.getenv('MISP_KEY')

def fetch_misp_events():
    misp = PyMISP(MISP_URL, MISP_KEY, ssl=False)
    events = misp.search(controller='events', limit=10)
    return events.get('response', [])