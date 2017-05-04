from setuptools import setup

setup(name='trename',
      version='0.1',
      license='MIT',
      packages=['trename'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
                'trename=trename.cli:main',
          ]
      }
)