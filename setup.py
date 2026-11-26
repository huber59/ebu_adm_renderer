from setuptools import setup, find_packages

setup(
    name='ear',
    description='EBU ADM Renderer',
    version='2.0.0',

    url='https://github.com/ebu/ebu_adm_renderer',

    author='EBU',
    author_email='ear-admin@list.ebu.ch',
    license='BSD-3-Clause-Clear',

    long_description=open('README.md').read() + '\n' + open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',

    python_requires='>=3.9',
    install_requires=[
        'numpy>=1.22',
        'scipy>=1.8',
        'attrs>=21.3',
        'ruamel.yaml>=0.17.22',
        'lxml>=4.9',
        'multipledispatch>=0.6',
    ],

    extras_require={
        'test': [
            'pytest>=7',
            'pytest-datafiles>=2.0',
            'pytest-cov>=4',
            'soundfile>=0.12',
        ],
        'dev': [
            'flake8>=6',
            'flake8-print>=5',
        ],
    },

    packages=find_packages(),

    package_data={
        "ear.test": ["data/*.yaml", "data/*.wav"],
        "ear.core": ["data/*.yaml", "data/*.dat"],
        "ear.core.test": ["data/psp_pvs/*.npz"],
        "ear.core.objectbased.test": ["data/gain_calc_pvs/*"],
        "ear.fileio.adm": ["data/*.xml"],
        "ear.fileio.adm.test": ["test_adm_files/*.xml"],
        "ear.fileio.bw64.test": ["test_wav_files/*.wav"],
    },

    entry_points={
        'console_scripts': [
            'ear-render = ear.cmdline.render_file:main',
            'ear-utils = ear.cmdline.utils:main'
        ]
    },
)
