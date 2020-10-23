from setuptools import setup, find_packages
version = '3.3'

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(
    name='wutongchain-cts',
    version=version,
    packages=find_packages(),
    author=u'Wally Yu',
    install_requires=['requests>=2.10'],
    url='https://github.com/wally-yu/py-wutongchain-cts',
    include_package_data=True,
    license='MIT License',
    description='CTS是梧桐链（同济区块链）的轻量级独立服务，主要应用场景为存证，可以说是为存证领域而特制的，便于使用的API和服务，此为其Python SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
      )

# build: python3 setup.py sdist bdist_wheel