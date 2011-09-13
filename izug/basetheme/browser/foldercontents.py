from plone.app.content.browser.foldercontents import FolderContentsView
from plone.app.content.browser.foldercontents import FolderContentsTable
from plone.app.content.browser.tableview import Table, TableKSSView
from Acquisition import aq_inner
from OFS.interfaces import IOrderedContainer
from zope.app.pagetemplate import ViewPageTemplateFile


class IzugFolderContentsView(FolderContentsView):
    """Customized izug folder_contents
    Check https://extranet.4teamwork.ch/support/zug/maintlog/1583
    Behaviour:
    * Default sort-order is alphabetical (sortable_title)
    * Use sortAttribute and sortOrder, if available
    * Plone-root is using plone-default folder_contents
      (Registred on IBaseObject)
    * Columntitle is clickable and triggers js-sort
    * The sortable row is only available if sortAttribute is manuall
      (getObjPositionInParent), on plone root or on some explicit configuered
      types (Default: Folder)
    * Batchsize is 50
    * Column type: show title not the icon.
    """

    def contents_table(self):
        table = IzugFolderContentsTable(aq_inner(self.context), self.request)
        return table.render()


class IzugFolderContentsTable(FolderContentsTable):
    """
    The foldercontents table renders the table and its actions.
    """

    def __init__(self, context, request, contentFilter={}):
        self.context = context
        self.request = request
        self.contentFilter = contentFilter
        self.update_filter()

        url = context.absolute_url()
        view_url = url + '/@@folder_contents'
        self.table = IzugTable(request, url, view_url, self.items,
                           show_sort_column=self.show_sort_column,
                           buttons=self.buttons)

    def update_filter(self):
        content_filter = {}

        # Huck for js sort on table
        if 'sort_on' in self.contentFilter:
            return

        # Default is sortable_title
        content_filter['sort_on'] = 'sortable_title'
        # Look for available sort attr.
        sort_on = self.context.aq_explicit.get('sortAttribute', None)
        sort_order = self.context.aq_explicit.get('sortOrder', None)
        if sort_on:
            content_filter['sort_on'] = sort_on
        if sort_order:
            content_filter['sort_order'] = sort_order
        self.contentFilter.update(content_filter)
        # Fix for kss update_table - THIS SHOULD BE DONE BY PLONE!!
        if sort_on:
            self.request.set('sort_on', sort_on)

    @property
    def orderable(self):
        """
        """
        iface = IOrderedContainer.providedBy(aq_inner(self.context))
        attr = self.context.aq_explicit\
            .get('sortAttribute', '') == 'getObjPositionInParent'
        if self.contentFilter.get('sort_on', '') != 'getObjPositionInParent':
            return False
        return iface and attr


class FolderContentsKSSView(TableKSSView):
    table = IzugFolderContentsTable


class IzugTable(Table):
    render = ViewPageTemplateFile("table.pt")
