import os
from setuptools import setup, find_namespace_packages
from typing import (
    List,
    Optional,
)


# Environ variables
PANDOS_CODEBASE_PATH = os.environ.get(
    "PANDOS_CODEBASE_PATH",
    default=os.path.join("src", "main")
)
PANDOS_DISABLE_MYPYC = int(os.environ.get(
    "PANDOS_DISABLE_MYPYC",
    default="0",
))


if not PANDOS_DISABLE_MYPYC:
    from mypyc.build import mypycify


with open("README.md", "r") as file:
    readme = file.read()


with open("requirements.txt", "r") as file:
    requirements = [req for req in file.read().splitlines() if req and not req.startswith("#")]


version_filename = "toolbox_version"
version_filepath = os.path.join(
    PANDOS_CODEBASE_PATH,
    "pandos",
    "system",
    "toolbox",
    version_filename
)
with open(version_filepath, "r") as file:
    version = file.read().strip()


with open("LICENSE", "r") as file:
    license_content = file.read()


def get_source_files(
        ignore_mark: Optional[str] = None,
        skip_dirs: Optional[List[str]] = None,
        skip_files: Optional[List[str]] = None,
) -> List[str]:
    skip_dirs = skip_dirs or []
    skip_files = skip_files or []

    def traverse(path: str):
        for _, dirs, files in os.walk(path):
            node_files = [
                os.path.join(path, file)
                for file in files
                if file.endswith(".py") and file not in skip_files
            ]
            return node_files + [
                file
                for directory in dirs
                for file in traverse(os.path.join(path, directory))
                if directory not in skip_dirs
            ]
    return [
        source_file_handler.close() or source_file
        for source_file in traverse(PANDOS_CODEBASE_PATH)
        for source_file_handler in [open(source_file, "r")]
        if ignore_mark is None or ignore_mark not in source_file_handler.read()
    ]


def get_packages(here: str = ".", pandos_prefix: str = "pandos") -> List[str]:
    return [
        package
        for package in find_namespace_packages(where=here)
        if package.startswith(pandos_prefix)
    ]


mypyc_configs = [
    # "--disallow-untyped-defs",  # TODO: Enable this option eventually for better performance
    "--ignore-missing-imports",
]

mypyc_target_files = get_source_files(
    ignore_mark="# pandos-mypyc-ignore-file",
    skip_dirs=[
        "__pycache__",
    ],
    skip_files=[
        "__init__.py"
    ],
)


packages = get_packages(here=PANDOS_CODEBASE_PATH)


setup(
    name="pandos_toolbox",
    version=version,
    description=(
        "Pandos System Extension: toolbox"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="rhdzmota",
    author_email="info@rhdzmota.com",
    url="https://github.com/pando-systems/pando-systems-extensions",
    # https://pypi.org/classifiers/
    classifiers=[
        "Typing :: Typed",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Distributed Computing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
    ],
    package_dir={
        "": PANDOS_CODEBASE_PATH,
    },
    package_data={
        "": [
            os.path.join(
                "system",
                "toolbox",
                "toolbox_version",
            ),
        ]
    },
    include_package_data=True,
    packages=packages,
    install_requires=requirements,
    python_requires=">=3.10, <4",
    license=license_content,
    zip_safe=False,
    **({} if PANDOS_DISABLE_MYPYC else dict(ext_modules=mypycify(mypyc_configs + mypyc_target_files))),
)
