================================================
Comprehensive Housing and Affordability Strategy
================================================


According to (Consolidated Planning/CHAS Data | HUD USER), the United States
Department of Housing and Urban Development (HUD) gets custom tabulations of
American Community Survey (ACS) data from the United States Census Bureau every
year. These figures, dubbed "CHAS" (Comprehensive Housing Affordability
Strategy), show the scope of housing issues and needs, particularly among
low-income households. Local governments utilize the CHAS data to plan how they
will spend HUD monies, and HUD may use the data to distribute grant funds.
  
Examples
========

These are basic examples showing you how to query the Comprehensive Housing and
Affordability (CHAS) API.

Each geoid query represents a CHAS measurement for that particular 
geographic resolution. Before looking at the examples I RECOMMEND first
looking at [the parameters] `Parameters`_
as well as [return data] `Returns`_ located at the bottom of the page.

The functions below are the main functions for querying the CHAS API at
different geographic resolutions. The package also contains an omni function 
which encapsulates thecapabilities of all the main function calls below --
[omni-function] `Using the omni function for querying`_

1) [nation] `Comprehensive Housing and Affordability Strategy for Nation`_
2) [state] `Comprehensive Housing and Affordability Strategy for States`_
3) [county] `Comprehensive Housing and Affordability Strategy for County`_
4) [mcd] `Comprehensive Housing and Affordability Strategy for MCD`_
5) [place] `Comprehensive Housing and Affordability Strategy for Place`_

Comprehensive Housing and Affordability Strategy for Nation
===========================================================

.. code-block:: Python

    hud_chas_nation(year = ["2014-2018"])


Comprehensive Housing and Affordability Strategy for States
===========================================================

.. code-block:: Python

    # Queries for CHAS in a state
    hud_chas_state("Maryland", year = ["2012-2016"])


Comprehensive Housing and Affordability Strategy for County
===========================================================

.. code-block:: Python

    # Queries a county in Virginia
    hud_chas_county("51999", year = ["2014-2018"])


Comprehensive Housing and Affordability Strategy for MCD
========================================================

.. code-block:: Python

    # Queries for CHAS for all mcds in Virginia
    hud_chas_state_mcd("VA", year = ["2014-2018"])


Comprehensive Housing and Affordability Strategy for Place
==========================================================

.. code-block:: Python

    # Queries for CHAS for all places in state fips code 51.
    hud_chas_state_place("51", year = ["2014-2018"])



Using the omni function for querying
====================================
The omni function requires specifying the type which can be from 1-12. The type
argument follows the number scheme described at [Input Arguments][]. You also 
must use the 'query' argument for inputting geoids instead of the specific 
geoid names (i.e county = 22031, cd = 7200) used by the other functions.

The input arguments for the omni function closely follow the API arguments
provided by HUD USER. Please type in '?hud_chas' into your terminal to get more
details on how to use this.

.. code-block:: Python
  
    hud_chas(type = 1)

    hud_chas(type = 2, 51)




Querying for Geographic Identifers
==================================

US Counties 
-----------

This is an example to show you how to query for all counties in MD,
Virginia, and California, respectively.

.. code-block:: Python

    hud_state_counties("MD")

    hud_state_counties("Virginia")

    hud_state_counties("6")



US Minor Civil Divisions
------------------------

This is an example to show you how to query for minor civil divisions in
Virginia and California.

.. code-block:: Python

    hud_state_minor_civil_divisions(["VA", "CA"])



US Places
---------

This is an example to show you how to query for places in Wyoming and Michigan

.. code-block:: Python

    hud_state_places(["VA", "CA"])

Parameters
==========


Returns
=======


References
===========

"Consolidated Planning/CHAS Data | HUD USER." Www.huduser.gov,
      www.huduser.gov/portal/datasets/cp.html.
