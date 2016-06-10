import os
from setuptools import setup

here = os.path.dirname(os.path.abspath(__file__))

setup(name='imgcaption',
      version='0.1.2',
      description="Library that gets image captions using "
                  "Microsoft's https://www.captionbot.ai/",
      url='https://github.com/DeanF/imgcaption',
      author='DeanF',
      packages=['imgcaption'],
      install_requires=['requests', 'six'],
      zip_safe=False)
