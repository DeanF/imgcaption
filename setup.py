from setuptools import setup

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(name='imgcaption',
      version='0.1.0',
      description="Library that gets image captions using "
                  "Microsoft's https://www.captionbot.ai/",
      url='https://github.com/DeanF/imgcaption',
      author='DeanF',
      packages=['imgcaption'],
      install_requires=requirements,
      zip_safe=False)
