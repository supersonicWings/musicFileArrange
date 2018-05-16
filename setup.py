from setuptools import setup
import py2exe

setup(name='FileToDir',
      description='It moves the file in the same folder as the file name',
      version='1.0',
      windows=[{'script': 'fileArrange.py'}],
      options={
          'py2exe': {
              'bundle_files': 1,
              'dll_excludes': ['w9xpopen.exe']
          },
      },
      zipfile=None
      )
