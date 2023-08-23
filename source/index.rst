Introduction
============

.. include:: introduction.rst

Quickstart
==========

REDi can be run as a Python package (PyREDi) or as a script through the command line.

Install through PyPi
********************

1. Install PyRedi through PyPi

   ``pip install pyredi`` or ``python -m pip install pyredi``

You should now be able to use REDi in your Python code, as shown below in the Usage section.

Install and run from source
***************************

1. Download the source code from the `REDi GitHub repository <https://github.com/arup-group/REDi>`_ by running the following in your command line interface:

   ``git clone https://github.com/arup-group/REDi.git``

2. Navigate into the folder where REDi was cloned:

   ``cd REDi``

3. Install the required Python packages:

   ``pip install -r requirements.txt``

You should now be able to use REDi in your Python environment, as shown below in the Usage section.

Usage
=====

The REDi engine can be run via the PyREDi Python package or through a command line interface. Both methods require installation as outlined above.

PyREDi Python Package
*********************

To run the REDi engine from the PyREDi package, you need to import the PyREDi package into your Python script and run the ``go_redi`` function with the ``building_dict`` as input, as shown below:

.. code-block:: python
   
   import json 
   
   from REDi.go_redi import go_redi
   
   building_dict = json.load(open('./examples/example_building.json'))
   
   res = go_redi(building_dict=building_dict, seed=2023)
   
   print('Total downtime :',res['building_total_downtime'],'\n')

You should see the following output:

.. code-block:: text

		******* Running REDi™ for building example_building *******
		
		Analysis done!
		
		Time to full recovery [days] 496.56187582116473
		Time to functional recovery [days]  475.5133725965221
		Time to immediate occupancy [days]  231.80657475175408
		
		Total downtime : [496.56187582 475.5133726  231.80657475] 

Note that if you omit the seed value (``seed=2023``) from the input parameters to ``go_redi``, your results will be different.

The ``building_dict`` object is a dictionary that should contain all inputs required by REDi. The inputs are explained below in the :ref:`inputs-label` section. An example ``building_dict`` is also provided in the ``examples/example_building.json`` file. If importing the ``examples/example_building.json`` file as shown above, you must provide the absolute path to the ``examples/example_building.json`` file. The ``res`` object from the code-block above is a dictionary containing the outputs described below.

.. important::

    If you do not provide the seed and/or burn-in options, the output will vary every run, i.e., the output will be non-deterministic.
    REDi is tested on Python version **3.11**. It may or may not work in other versions of Python.

Command line interface
**********************

The REDi engine can be executed from the command line using the following syntax:

.. code-block:: text

	python main.py [-h] [-a A] [-c C] [-r R] [-s S] [-b B]

where:

.. code-block:: text

	- h, help - show the help message 
	- a A - Path to the asset JSON file [str] (required)
	- r R - Path of the results file (include the .json suffix in path) [str] (required)
	- c C - Path to the components JSON file [str] (optional - REDi will use built-in FEMA P-58 component library if blank)
	- s S - Seed for the random number generator, for deterministic output [int] (optional - leave blank for stochastic output)
	- b B - Burn-in number, i.e., how many times to generate and discard random numbers at random number generator initialization [int] (optional - mainly for testing purposes)

To run the example building, execute the following in command line:

``python main.py -a "examples/example_building.json" -r "REDi_output.json" -s 2023``

You should see the following output:

.. code-block:: text

		******* Running REDi™ for building example_building *******
		
		Analysis done!
		
		Time to full recovery [days] 496.56187582116473
		Time to functional recovery [days]  475.5133725965221
		Time to immediate occupancy [days]  231.80657475175408
		
		Total downtime : [496.56187582 475.5133726  231.80657475] 

Note that if you omit the seed value (``-s 2023``) from the input parameters, your results will be different.

.. important::

    If you do not provide the seed and/or burn-in options, the output will vary every run, i.e., the output will be non-deterministic.
    REDi is tested on Python version **3.11**. It may or may not work in other versions of Python.

Background
**********

REDi is underpinned by the performance-based engineering methodology introduced by FEMA. Namely, the component-based FEMA P-58 methodology: `Development of Next Generation Performance-Based Seismic Design Procedures for New and Existing Buildings <https://femap58.atcouncil.org/2-uncategorised/1-home>`_. REDi uses a modified version of the component library from the FEMA P-58 PACT tool. A prepackaged component library is provided as a json file in the repository: ``data\component_library.json``. REDi's version of the FEMA P-58 component library employs the same naming convention as FEMA, e.g., ``B1031.001``.  The main difference between the two libraries is that each component in REDi's library contains additional **seq**, **long_lead**, and **rds** parameters that are desribed below.

- **seq** - list that defines the repair sequence for that component. The length of the **seq** list is always 2. 
- **long_lead** - list that specifies the long-lead times for repair materials for the component. The length of the **long_lead** list is always 3. 
- **rds** - list that provides the repair class for each damage state. The length of the **rds** list should be the same as the number of damage states. 

There are 3 repair goals in REDi: 1) full recovery; 2) functional recovery; and 3) re-occupancy. Moreover, there are 8 repair sequences; 7 that are non-structural and 1 that is structural. 

Inputs and outputs
******************

The following sections outline the necessary inputs for the REDi engine and its corresponding outputs.
 
.. _inputs-label:

Inputs
++++++

.. include:: inputs.rst

.. _outputs-label:

Outputs
+++++++

.. include:: outputs.rst

Contribution guidelines
=======================

.. include:: contribution_guidelines.rst

License
=======

REDi is licensed under the Apache License, Version 2.0. The full license text can be found in the ``LICENSE.txt`` file found `here <https://github.com/arup-group/REDi/blob/main/LICENSE.txt>`_ in the GitHub repository. 

Contact
=======

REDi represents the collaborative result of more than a decade of implementation and research into building recovery at Arup's Risk + Resilience team (formerly Advanced Technology + Research) in San Francisco.

PyREDi Code Contribution team
*****************************

.. include:: contribution_team.rst

REDi Technical background team
******************************

.. include:: technical_team.rst

Contact Us
**********

This documentation is a continuous work in progress. To report any errors or omissions, please contact Dr. Stevan Gavrilovic, Arup, Risk + Resilience Team, San Francisco.

`Stevan Gavrilovic <mailto:stevan.gavrilovic@arup.com>`_

.. toctree::
   :maxdepth: 3
   :caption: Contents:
   
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
