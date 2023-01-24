import setuptools


with open('readme.md', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='psr.container',
    version='1.1.0',
    description='Common Container Interface (PHP FIG PSR-11)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='License :: OSI Approved :: MIT License',
    package_dir={'psr': 'lib/psr'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    py_modules=['psr.container'],
    python_requires='>=3.6',
)
