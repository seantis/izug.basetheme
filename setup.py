from setuptools import setup, find_packages
import os

version = open('izug/basetheme/version.txt').read().strip()
maintainer = 'Mathias Leimgruber'

extras_require = {
    'plone4': ['ftw.upgrade'],
    }

setup(name='izug.basetheme',
      version=version,
      description="An installable theme for Plone 4.0",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],

      keywords='web zope plone theme',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='https://github.com/4teamwork/izug.basetheme',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['izug'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        'plonetheme.classic',
        'collective.js.jqueryui',
        'ftw.contentmenu',
        'z3c.jbot',
        'collective.mtrsetup',
        'plone.browserlayer',
        'zope.app.pagetemplate'
        ],
      extras_require=extras_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
