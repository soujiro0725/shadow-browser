from setuptools import setup


setup(
    name = 'shadow_browser',
    version = '0.1.0',
    url = 'https://github.com/soujiro0725/shadow-browser',
    license = 'MIT',
    author = 'soujiro0725',
    author_email = 'soujiro0725@gmail.com',
    description = '',
    install_requires = ['setuptools', 'selenium'],
    packages = ['browser'],
    package_data={
        'drivers': ['browser/driver/chromedriver_mac', 'browser/driver/chromedriver_linux']
    },
    entry_points = {
    }
)
