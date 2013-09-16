from logging import getLogger
log = getLogger('izug.basetheme')

from Products.CMFCore.utils import getToolByName

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('izug.basetheme_various.txt') is None:
        return

    # Add additional setup code here

def seantis_uninstall(context):
    
    if context.readDataFile('is_seantis_uninstall_profile') is None:
        return

    portal = context.getSite()

    # remove all izug specific stuff from different seantis modules
    css_registry = getToolByName(portal, 'portal_css')
    stylesheets = css_registry.getResourcesDict()
    ids = [
        i for i in stylesheets 
        if 'resource++seantis.dir' in i 
        and 'css' in i
        and 'izug' in i
    ]

    for id in ids:
        log.info('removing {}'.format(id))
        css_registry.unregisterResource(id)

    return "Ran all uninstall steps."
