=============
Income Limits
=============


According to (Income Limits | HUD USER), HUD establishes income restrictions for
assisted housing programs such as Public Housing, Section 8 project-based,
Section 8 Housing Choice Voucher, Section 202 housing for the elderly, and
Section 811 housing for persons with disabilities. For each metropolitan region,
parts of some metropolitan areas, and non-metropolitan county, HUD creates
income limitations based on Median Family Income estimates and Fair Market Rent
area criteria.


Examples
========

This page contains basic examples of how to query the HUD Income Limits API.
Before looking at the examples I reccomend first taking a look at
[the parameters] `Parameters`_ as well as [output data] `Returns`_ located at
the bottom of the page.

**Disclaimer:** The output tables are too large to be displayed here so we
choose to leave them out.

* Querying a state will return a single row containing the Income Limits for that state. 
* Querying for a county will return the IL measurement for that county.
* Querying for a cbsa will return the IL measurement for that cbsa.

State Level Income Limits
=========================

These are examples which show you how to query the Income Limits on a state
level basis. You can use the state abbreviation, state name, or state fipscode.
It will return a single row indicating the income limits for that particular
state.


.. code-block:: Python

    # These function calls gets income limits data for 
    # the state of Virginia in 2021.
    hud_il(query = 'VA', year = '2021')

    hud_il(query= "Virginia", year = '2021')

    hud_il(query= "51", year = '2021')

    # You can also choose to query for multiple
    # states or multiple years.
    hud_il(query = ['VA', 'MD'], year = ['2021', '2019'])


County Level Income Limits
==========================
These are examples that show you how to query the Income Limits on a 
county-level basis: counties are defined with a 2 digit state fipscode + 3 digit county fipscode. You also need a 99999 code added to the end. We currently 
don't know why the extra 99999 is included and have not found any cases where it's different. I recommend looking at `US Counties`_ to determine what counties 
are available for particular states.

.. code-block:: Python

    # Getting a county requires a 2 digit state fip + 3 digit county fip + 99999
    # This queries for Income Limits in 2017.
    hud_il(query = '0100199999', year = '2017')

Small Areas Income Limits
=========================

These are examples that show you how to query the Small Areas Income Limits.
Small Areas are defined as metropolitan and micropolitan areas specified using
CBSA codes. Currently, we know how to query for metropolitan small areas, but
are not sure for micropolitan yet. I recommend looking at 
`US Metropolitan Areas`_ to determine what counties are available.

.. code-block:: Python

    # Gets il data for METRO area.
    hud_il(query = "METRO47900M47900", year = [2018])


Most recent Income Limits files
===============================

To get the most recent Income Limits files by year:


.. code-block:: Python
    
    hud_rec_il_yr()


Querying for Geographic Identifers
==================================

US States
---------
This is an example to show you how to query for all states and territories
in the US.

.. code-block:: Python

    hud_nation_states_territories()



US Counties 
-----------
This is an example to show you how to query for all counties in MD,
Virginia, and California, respectively.

.. code-block:: Python

    hud_state_counties("MD")

    hud_state_counties("Virginia")

    hud_state_counties("6")


US Metropolitan Areas
---------------------

This is an example to show you how to query for metropolitan areas for a state.

.. code-block:: Python

    # Get all metropolitan areas in Maryland and Virginia.
    hud_state_metropolitan(["MD", "VA"])


Parameters
==========


Returns
=======


References
==========

"Income Limits | HUD USER." Huduser.gov, 2015,
         www.huduser.gov/portal/datasets/il.html.
