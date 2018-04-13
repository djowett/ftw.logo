from ftw.logo.tests import FunctionalTestCase
from ftw.testbrowser import browsing
from unittest import skip


class TestIconViewlet(FunctionalTestCase):

    @skip("TODO: Remove defualt viewport from sunburst default template")
    @browsing
    def test_viewport_metatag(self, browser):
        browser.login().visit(self.portal)

        self.assertEqual(
            ['width=device-width, initial-scale=1'],
            map(lambda x: x.attrib['content'], browser.css(
                'meta[name="viewport"]'))
        )

    @browsing
    def test_logo_viewlet_displays_relevant_metadata_in_header(self, browser):
        browser.login().visit(self.portal)

        self.assertEqual(
            [{'href': 'http://nohost/plone/@@logo/icon/APPLE_TOUCH_ICON', 'sizes': '180x180'}],
            map(lambda x: {
                'href': x.attrib['href'],
                'sizes': x.attrib['sizes'],
            }, browser.css('link[rel="apple-touch-icon"]'))
        )

        self.assertEqual(
            [
                {
                    'type': 'image/png',
                    'sizes': '32x32',
                    'href': 'http://nohost/plone/@@logo/icon/FAVICON_32X32',
                },
                {
                    'type': 'image/png',
                    'sizes': '16x16',
                    'href': 'http://nohost/plone/@@logo/icon/FAVICON_16X16',
                },
                {
                    'type': '',
                    'sizes': '',
                    'href': 'http://nohost/plone/@@logo/icon/FAVICON',
                },
            ],
            map(lambda x: {
                'type': x.attrib.get('type', ''),
                'sizes': x.attrib.get('sizes', ''),
                'href': x.attrib['href'],
            }, browser.css('link[rel="icon"]'))
        )

        self.assertEqual(
            ['http://nohost/plone/manifest.json'],
            map(lambda x: x.attrib['href'], browser.css(
                'link[rel="manifest"]'))
        )

        self.assertEqual(
            ['http://nohost/plone/browserconfig.xml'],
            map(lambda x: x.attrib['content'], browser.css(
                'meta[name="msapplication-config"]'))
        )

        self.assertEqual(
            ['#ffffff'],
            map(lambda x: x.attrib['content'], browser.css(
                'meta[name="theme-color"]'))
        )
