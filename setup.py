from setuptools import find_packages, setup

setup(
    name="xgboost_ray",
    packages=find_packages(where=".", include="xgboost_ray*"),
    version="0.1.3",
    author="Ray Team",
    description="A Ray backend for distributed XGBoost",
    long_description="A distributed backend for XGBoost built on top of "
    "distributed computing framework Ray.",
    url="https://github.com/ray-project/xgboost_ray",
    install_requires=[
        "xgboost>=0.90", "ray", "numpy>=1.16,<1.20", "pandas", "pyarrow<5.0.0",
        "wrapt>=1.12.1"
    ])
# pyarrow<5.0.0 pinned until petastorm is updated
