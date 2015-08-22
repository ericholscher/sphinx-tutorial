from setuptools import setup, find_packages

setup(
    name='crawler',
    version='1.0.0',
    author='Eric Holscher',
    author_email='eric@ericholscher.com',
    license='BSD',
    description='A simple web crawler',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    install_requires=['requests', 'beautifulsoup4'],
    entry_points={
        'console_scripts': [
            'crawler=crawler.main:run_main',
        ]
    },
)
