# -*- coding: utf-8 -*-


from misitio.utilities.contenttype import *


def create_site_structure(site):
    """Crea la estructura del sitio de Misitio.
    """
    createFolder(site, u'Acerca de',
                 allowed_types=['Document', 'Folder'],
                 exclude_from_nav=False)
    createFolder(site, u'contactos',
                 allowed_types=['Document', 'Folder', 'image'],
                 exclude_from_nav=False)
    createFolder(site, u'servicios',
                 allowed_types=['Document', 'Folder', 'image', 'file'],
                 exclude_from_nav=False)
    createFolder(site['servicios'], u'capacitacion',
                 allowed_types=['Document', 'Folder', 'image'],
                 exclude_from_nav=False)
    createLink(site, u'Twitter','http://twitter.com/#!/VTVcanal8')
    createLink(site, u'Facebook','http://twitter.com/#!/VTVcanal8')
    createDocument(site['acerca-de'],u'La Compania')
    createDocument(site['acerca-de'],u'Ubicacion')
    createDocument(site['servicios'],u'Consultoria')
    createDocument(site['servicios']['capacitacion'], u'Python')
    createDocument(site['servicios']['capacitacion'], u'Plone')

def remove_default_content(site):
    """Borra el contenido creado en la instalacion de Plone.
    """
    removable = ['Members', 'news', 'events', 'front-page']
    for item in removable:
        if hasattr(site, item):
            site.manage_delObjects([item])

def setupVarious(context):
    if context.readDataFile ('misitio.policy-default.txt') is None:
        return
    portal = context.getSite()
    remove_default_content(portal)
    create_site_structure(portal)
