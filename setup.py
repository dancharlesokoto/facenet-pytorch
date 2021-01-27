import setuptools, os

PACKAGE_NAME = 'facenet-pytorch'
VERSION = '1.0'
AUTHOR = 'Dancharles Okoto'
EMAIL = 'dancharles.okoto@gmail.com'
DESCRIPTION = 'Improved Pretrained Pytorch face detection and recognition models'
GITHUB_URL = 'https://github.com/dancharlesokoto/facenet-pytorch'

parent_dir = os.path.dirname(os.path.realpath(__file__))
import_name = os.path.basename(parent_dir)

with open('{}/README.md'.format(parent_dir), 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=GITHUB_URL,
    packages=[
        'facenet_pytorch',
        'facenet_pytorch.models',
        'facenet_pytorch.models.utils',
        'facenet_pytorch.data',
    ],
    package_dir={'facenet_pytorch':'.'},
    package_data={'': ['*net.pt']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'requests',
        'torchvision',
        'pillow',
    ],
)
