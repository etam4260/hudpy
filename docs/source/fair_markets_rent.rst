=================
Fair Markets Rent
=================

According to (Fair Market Rents | HUD USER), Fair Market Rents (FMRs) are used
to calculate payment standard amounts for the Housing Choice Voucher program,
initial renewal rents for some expiring project-based Section 8 contracts,
initial rents for housing assistance payment (HAP) contracts in the Moderate
Rehabilitation Single Room Occupancy program (Mod Rehab), rent ceilings for
rental units in both the HOME Investment Partnerships program and the Emergency
Solution Grants program, and rent ceilings for rental units in both the HOME
Investment Partnerships program and the Emergency Solution Grant.

Furthermore, the United States Department of Housing and Urban Development (HUD)
calculates FMRs for metropolitan areas defined by the Office of Management and
Budget (OMB), some HUD-designated subdivisions of OMB metropolitan areas, and
each non-metropolitan county on an annual basis. FMRs must be posted at least 30
days before they go into effect, and they must go into force at the beginning of
the federal fiscal year (usually October 1). Fair Market Rentals are estimates
of the 40th percentile gross rents for standard quality units within a
metropolitan region or non-metropolitan county, as described in 24 CFR 888.113.


Examples
========

These are basic examples to show you how to query the Fair Markets Rent API. Before
looking at the examples I RECOMMEND first looking at [the parameters] `Parameters`_
as well as [return data] `Returns`_ located at the bottom of the page.

**Disclaimer:** The output tables are too large to be displayed here so we
choose to leave them out.

Querying a county or cbsa code that are considered small areas will 
return data at a zip code level. If they are not small areas, then it will 
give a singular measurement for that entire county or cbsa. 

Lets say we are working with county level data -- when mixing them together 
(counties that are small areas and not small areas) those counties that are
not small areas will have an NA in the zip_code, 
meaning this measurement is defined at a county level. Those counties that 
are small areas will return zip code data in the zip_code field.

State Level Fair Markets Rent
=============================

This is an example which shows you how to query the Fair Markets Rent API for a
state. You can use the state abbreviation, state name, or state fips code. It
will return all counties in the state and their Fair Markets Rents as well
as all metroareas in the state and their Fair Markets Rent.


.. code-block:: Python
   
    # These functions gets FMR data for the state of Virginia in 2021.
    hud_fmr(query = 'VA', year = '2021')

    hud_fmr(query= "Virginia", year = '2021')

    hud_fmr(query= "51", year = '2021')



If you only need the county level data, then this might work better...

.. code-block:: Python

    # These functions gets FMR data for the state 
    # of Virginia in 2021 for counties.
    hud_fmr_state_counties(state = 'VA', year = '2021')

    hud_fmr_state_counties(state = "Virginia", year = '2021')

    hud_fmr_state_counties(state = "51", year = '2021')


If you need just metro data...

.. code-block:: Python

    # These functions gets FMR data for the state 
    # of Virginia in 2021 for metroareas.
    hud_fmr_state_metroareas(state = 'VA', year = '2021')

    hud_fmr_state_metroareas(state = "Virginia", year = '2021')

    hud_fmr_state_metroareas(state = "51", year = '2021')



County Level Fair Markets Rent
===============================

This is an example which shows you how to query the Fair Markets Rent on a
county level basis. These are defined with a 2 digit state code + 3 digit county
code. You also need a 99999 code added onto the end. I recommend taking a 
look at `US Counties`_ to determine what counties are available.

.. code-block:: Python

    # Getting a county requires a 2 digit state
    # fipscode + 3 digit county fipscode + 99999
    hud_fmr(query = '0100199999', year = '2017')



You can also choose to use:

.. code-block:: Python

    # Getting a county requires a 2 digit state 
    # fipscode + 3 digit county fipscode + 99999
    hud_fmr_county_zip(county = '0100199999', year = '2017')



Small Areas Fair Markets Rent
====================================

.. code-block:: Python

    # Gets FMR data for METRO area.
    hud_fmr(query = "METRO47900M47900", year=[2018])



You can also choose to use:
.. code-block:: Python

    # Getting a county requires a 2 digit state 
    # fipscode + 3 digit county fipscode + 99999
    hud_fmr_metroarea_zip(metroarea = 'METRO47900M47900', year = '2017')



Most recent Fair Markets Rent files
====================================

To get the most recent Fair Markets Rent files by year:

.. code-block:: Python

    hud_rec_fmr_yr()


Querying for Geographic Identifers
====================================

US States
---------
This is an example to show you how to query for all states in the US.

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

This is an example to show you how to query for metropolitan areas in Wyoming
and New York.

.. code-block:: Python

    hud_state_metropolitan(["WY", "NY"])



Parameters
==========

+-----------+-------------------------------------------------------------------------------------+
|Parameters | Description                                                                         |
+===========+=====================================================================================+
| query     |   Can provide either a 10 digit FIPS code which is almost always                    |
|           |   state fips + county fips + 99999, or state abbreviation.                          |
|           |   Can also provide a CBSA code. You are only allowed to query for metropolitan      |
|           |   areas.                                                                            |
|           |                                                                                     |
|           |   Run hud_states() to get a list of counties.                                       |
|           |                                                                                     |
|           |   Run hud_metropolitan("MD") to get a list of metropolitan areas in MD.             |
|           |                                                                                     |
|           |   Run hud_counties("MD") to get list of counties in MD.                             |
|           |                                                                                     |
|           |   * query = 'METRO12700M12700'                                                      |
|           |   * query = 'MD'                                                                    |
|           |   * query = '5100199999'                                                            |
|           |                                                                                     |   
+-----------+-------------------------------------------------------------------------------------+ 		                             
| year      |    Years of the data to retrieve: defaults to the current year.                     |
|           |                                                                                     |
|           |    * year = c(2019, 2018, 2021)                                                     |
|           |    * year = c(2016)                                                                 |
|           |    * year = 2021                                                                    |      
|           |                                                                                     |  
+-----------+-------------------------------------------------------------------------------------+ 
| key       |   The API key provided by HUD USER.                                                 |
|           |                                                                                     |         
|           |   * key = "a-sample-key"                                                            |                                         
+-----------+-------------------------------------------------------------------------------------+


Returns
=======
+------------+-------------------------------------------------------------------------------------+
|Data        | Description                                                                         |
+============+=====================================================================================+
| query      |   Identifier for county, state, or cbsadiv depending on function                    |
|            |                                                                                     |
+------------+-------------------------------------------------------------------------------------+ 		                             
| year       |   Year when measurement was taken.                                                  |
|            |                                                                                     |
|            |   * year = c(2019, 2018, 2021)                                                      |
|            |   * year = c(2016)                                                                  |
|            |   * year = 2021                                                                     |      
|            |                                                                                     |  
+------------+-------------------------------------------------------------------------------------+ 
|county_name |   Name of the county if it is a county.                                             |
|            |                                                                                     |         
|            |                                                                                     |                                         
+------------+-------------------------------------------------------------------------------------+
|counties_msa|   Names of all counties belonging to the Metro Area if it is a Metro Area(MSA).     |    
|            |                                                                                     |                                                
+------------+-------------------------------------------------------------------------------------+
| town_name  |   Town name - applicable for North East region                                      |
|            |                                                                                     |                                                 
+------------+-------------------------------------------------------------------------------------+
|metro_status|   value will be "1" if it is a metropolitan county. Otherwise value will be "0".    |                                           
|            |                                                                                     |                                                 
+------------+-------------------------------------------------------------------------------------+
|metro_name  |   Metro area name if metro_status is "1"                                            |
|            |                                                                                     |                                           
+------------+-------------------------------------------------------------------------------------+
|smallarea   |                                                                                     |
|_status     |   value will be "1" if it is a small area. Otherwise value will be "0".             |
|            |                                                                                     |                                              
+------------+-------------------------------------------------------------------------------------+
| Efficiency |                                                                                     |
| (A studio  |                                                                                     |
| apartment) |   Efficiency FMR in US Dollars                                                      |
|            |                                                                                     |                                              
+------------+-------------------------------------------------------------------------------------+    
| One-Bedroom|   1-bedroom FMR in US Dollars                                                       |
|            |                                                                                     |                                     
+------------+-------------------------------------------------------------------------------------+ 
| Two-Bedroom|   2-bedroom FMR in US Dollars                                                       |
|            |                                                                                     |                                              
+------------+-------------------------------------------------------------------------------------+ 
| Three-     |                                                                                     |
| Bedroom    |  3-bedroom FMR in US Dollars                                                        |
|            |                                                                                     |                                                                            
+------------+-------------------------------------------------------------------------------------+ 
| Four-      |                                                                                     |
| Bedroom    |   4-bedroom FMR in US Dollars                                                       |
|            |                                                                                     |                                             
+------------+-------------------------------------------------------------------------------------+ 


References
==========

"What Is Fair Market Rent? | RentData.org." Www.rentdata.org,
        www.rentdata.org/articles/what-is-fair-market-rent. Accessed 18 Feb. 2022.

"Fair Market Rents | HUD USER." Huduser.gov, U.S Department
        of Housing and Urban Development, 2017, 
        www.huduser.gov/portal/datasets/fmr.html.
