from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Physics',
    version='1.4.1',
    author='Sayad Uddin Tahsin',
    author_email='mr.pluto012@gmail.com',
    description='A Python Library for Performing Physics Calculations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sayad-Uddin-Tahsin/PhysicsKit',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.7',
    project_urls={
        'Bug Tracker': 'https://github.com/Sayad-Uddin-Tahsin/PhysicsKit/issues',
    },
    keywords=['physics', 'physicskit', 'tahsin-project']
)