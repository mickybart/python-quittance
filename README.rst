Quittance (Rent receipt)
========================

Permit to create receipt without effort.

quittance module
----------------

Installation
^^^^^^^^^^^^

This package is available for Python 3.5+.

install the development version from github:

.. code:: bash

    pip3 install git+https://github.com/mickybart/python-quittance.git

Prerequisite
^^^^^^^^^^^^

Examples in this README are using the rent.json and paid.json files. 

.. code:: python
    
    # rent structure
    # (rent.json)
    {
        "address" : "Street<br>Town<br>Country<br>...<br>",
        "owner" : "John Doe",
        "tenant" : "Another John Doe",
        "currency" : " euros",
        "rent_price" : 500.00,
        "rent_charge_price" : 100.00,
        "town" : "Receipt town",
        "signature" : "signature.png"
    }
    
    # paid structure
    # (paid.json)
    {
        "date" : "20/01/2018"
    }

Quick start
^^^^^^^^^^^

.. code:: bash

    # edit paid.json to set the paid date
    # rent.json should be ok
    
    python run.py


Error Types
-----------

Internal Notes
--------------

Bugs or Issues
--------------

Please report bugs, issues or feature requests to `Github
Issues <https://github.com/mickybart/python-quittance/issues>`__
