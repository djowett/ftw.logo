from ftw.logo.interfaces import IIconConfig
from ftw.logo.interfaces import ILogo
from ftw.logo.interfaces import ILogoConfig
from hashlib import sha256
from plone.app.caching.interfaces import IETagValue
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.interface import implementer
from zope.interface import Interface


@implementer(ILogo)
@adapter(IPloneSiteRoot, Interface)
class Logo(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_config(self, config_type):
        return getMultiAdapter((self.context, self.request), config_type)

    def get_logo_config(self):
        return getMultiAdapter((self.context, self.request), ILogoConfig)

    def get_icon_config(self):
        return getMultiAdapter((self.context, self.request), IIconConfig)


@implementer(IETagValue)
@adapter(Interface, Interface)
class LogoViewletETagValue(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        cachekey = sha256()
        cachekey.update(getMultiAdapter(
                (self.context, self.request), ILogo).get_logo_config().cachekey)
        cachekey.update(getMultiAdapter(
                (self.context, self.request), ILogo).get_icon_config().cachekey)
        return cachekey.hexdigest()
