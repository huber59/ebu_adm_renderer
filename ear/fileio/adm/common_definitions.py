from ...compatibility import open_resource
from .xml import parse_adm_elements
import lxml.etree


def load_common_definitions(adm):
    fname = "data/2094_common_definitions.xml"
    with open_resource(__name__, fname) as stream:
        element = lxml.etree.parse(stream)
        parse_adm_elements(adm, element, common_definitions=True)
        adm.lazy_lookup_references()
