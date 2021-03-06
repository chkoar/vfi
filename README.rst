|Travis|_ |Codecov|_ |ReadTheDocs|_

.. |Travis| image:: https://travis-ci.org/chkoar/vfi.svg?branch=master
.. _Travis: https://travis-ci.org/chkoar/vfi

.. |Codecov| image:: https://codecov.io/gh/chkoar/vfi/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/chkoar/vfi

.. |ReadTheDocs| image:: https://readthedocs.org/projects/vfi/badge/?version=latest
.. _ReadTheDocs: https://vfi.readthedocs.io/en/latest/?badge=latest

===
VFI
===

VFI - Voting Feature Intervals is a supervised classification model similar to Naive Bayes. Constructs intervals around each class for each feature. Class counts are recorded for each interval on each feature and the classification is performed using a voting scheme.

Based on the paper: G. Demiroz, A. Guvenir: Classification by voting feature intervals. In: 9th European Conference on Machine Learning, 85-92, 1997.01.

Documentation is available on ReadTheDocs at http://vfi.readthedocs.io/en/latest/


------------------
How to use VFI
------------------

The vfi package inherits from sklearn classes, and thus drops in neatly
next to other sklearn classifiers with an identical calling API. Similarly it
supports input in a variety of formats: an array (or pandas dataframe) of shape ``(num_samples x num_features)``.

.. code:: python

    import vfi
    from sklearn.datasets import load_iris
    
    data, target = load_iris(return_X_y=True)
    
    model = vfi.VFI()
    model.fit(data, target)


----------
Installing
----------

PyPI install, presuming you have an up to date pip:

.. code:: bash

    pip install vfi


If pip is having difficulties pulling the dependencies then we'd suggest to first upgrade
pip to at least version 10 and try again:

.. code:: bash

    pip install --upgrade pip
    pip install vfi

Otherwise install the dependencies manually using anaconda followed by pulling vfi from pip:

.. code:: bash

    conda install numpy scipy
    conda install scikit-learn
    pip install vfi


For a manual install of the latest code directly from GitHub:

.. code:: bash

    pip install --upgrade git+https://github.com/chkoar/vfi.git#egg=vfi


Alternatively download the package, install requirements, and manually run the installer:

.. code:: bash

    wget https://github.com/chkoar/vfi/archive/master.zip
    unzip master.zip
    rm master.zip
    cd vfi-master
    
    pip install -r requirements.txt
    
    python setup.py install

-----------------
Running the Tests
-----------------

The package tests can be run after installation using the command:

.. code:: bash

    pytest vfi --cov

--------------
Python Version
--------------

The vfi package supports only Python 3.
    
------------
Contributing
------------

We welcome contributions in any form! Assistance with documentation, particularly expanding tutorials,
is always welcome. To contribute please `fork the project <https://github.com/chkoar/vfi/issues#fork-destination-box>`_ make your changes and submit a pull request. We will do our best to work through any issues with
you and get your code merged into the main branch.


---------
Licensing
---------

The vfi package is MIT licensed. Enjoy.