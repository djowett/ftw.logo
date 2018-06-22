from plone.supermodel import model
from zope import schema

from ftw.logo import _

class IManualOverrides(model.Schema):

    title = schema.TextLine(
        title=_(u'Test name'),
    )
