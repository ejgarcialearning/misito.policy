import unittest2 as unittest
from Products.CMFCore.utils import getToolByName
from misitio.policy.testing import MISITIO_POLICY_INTEGRATION_TESTING


class TestSiteStructure(unittest.TestCase):

    layer = MISITIO_POLICY_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
            
    def test_default_content_is_removed(self):
        existing = self.portal.objectIds()
        self.assertTrue('events' not in existing)
        self.assertTrue('front-page' not in existing)
        self.assertTrue('news' not in existing)
        self.assertTrue('Member' not in existing)
            
    def test_misitio_content_is_created(self):
        existing = self.portal.objectIds()
        self.assertTrue('acerca-de' in existing)
        self.assertTrue('contactos' in existing)
        self.assertTrue('servicios' in existing)
        self.assertTrue('twitter' in existing)
        self.assertTrue('facebook' in existing)
