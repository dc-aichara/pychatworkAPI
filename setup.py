import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setuptools.setup(
  name='pychatworkAPI',
  packages=['pychatworkAPI'],
  version='1.12',
  license='MIT',
  description='pychatworkAPI is a python package to access chatwork offline.',
  author='Dayal Chand Aichara',
  author_email='dc.aichara@gmail.com',
  url='https://github.com/dc-aichara/pyChatwork',
  download_url='https://github.com/dc-aichara/pychatworkAPI/archive/V-1.12.tar.gz',
  keywords=['chatwork', 'chatwork-api'],
  install_requires=['requests',],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Operating System :: OS Independent'
  ],
  long_description=long_description,
  long_description_content_type='text/markdown'
)
