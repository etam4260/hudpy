==============
USPS Crosswalk
==============

According to (US Department of Housing and Urban Development, n.d.), the
difficulty of linking United States Postal Service (USPS) ZIP codes to Census
Bureau regions is one of the many obstacles that social science scholars and
practitioners face. Only at the ZIP code level is there relevant data that, when
paired with demographic data calculated at various Census geographic levels,
could open up new paths of investigation.

Furthermore, the (US Department of Housing and Urban Development, n.d.) believes
that while there are several appropriate approaches for integrating ZIP codes
with Census geographies, they are limited. The HUD-USPS Crosswalk Files were
supplied by PD&R to enable more routes for integrating these data. These
one-of-a-kind files were created using data from the quarterly USPS Vacancy
Data. They come straight from the USPS; they're updated quarterly, so they're
always up to date with changes in ZIP code configurations; and they reflect both
commercial and residential addresses. Because many of the phenomena that housing
researchers study are based on housing unit or address, the latter attribute is
of special interest to them. Analysts can take into account not just the spatial
distribution of population, but also the spatial distribution of residences, by
utilizing an allocation approach based on residential addresses rather than by
area or population. This allows for a more sophisticated approach to data
allocation across different geographies.

These journal articles describe the problem and proposed solution in more detail: 


Wilson, Ron and Din, Alexander, 2018. “Understanding and Enhancing the U.S.
         Department of Housing and Urban Development’s ZIP Code Crosswalk Files,”
         Cityscape: A Journal of Policy Development and Research, Volume 20 Number 2, 277
         https://www.huduser.gov/portal/periodicals/cityscpe/vol20num2/ch16.pdf


Din, Alexander and Wilson, Ron, 2020. "Crosswalking ZIP Codes to Census
         Geographies: Geoprocessing the U.S. Department of Housing & Urban Development’s
         ZIP Code Crosswalk Files," Cityscape: A Journal of Policy Development and
         Research, Volume 22, Number 1,
         https://www.huduser.gov/portal/periodicals/cityscpe/vol22num1/ch12.pdf


Census Geographies
==================

This chart provided by the US Census Bureau gives a good example of the
relationships among different geographies. The crosswalk files only support a
subset of these.


Examples
========

There are 12 main function calls for the crosswalk files:
the package also contains an omni function which encapsulates the 
capabilities of all the main function calls below --
[omni-function] `Using the omni function for querying`_

1) [zip-tract] `Crosswalk zipcode to census tract`_
2) [zip-county] `Crosswalk zipcode to county fip`_
3) [zip-cbsa (Core Base Statistical Areas)] `Crosswalk zipcode to core base statistical area (cbsa)`_
4) [zip-cbsadiv (Available 4th Quarter 2017 onwards)] `Crosswalk zipcode to core based statistical area division (cbsadiv)`_
5) [zip-cd (Congressional District)] `Crosswalk zipcode to congressional district (cd)`_
6) [tract-zip] `Crosswalk census tract to zipcode`_
7) [county-zip] `Crosswalk county fip into zipcode`_
8) [cbsa-zip] `Crosswalk core based statistical areas (cbsa) to zipcode`_
9) [cbsadiv-zip (Available 4th Quarter 2017 onwards)] `Crosswalk core based statistical areas division (cbsadiv) to zipcode`_
10) [cd-zip] `Crosswalk congressional district (cd) to zipcode`_
11) [zip-countysub (Available 2nd Quarter 2018 onwards)] `Crosswalk zipcode to county subdivision (countysub)`_
12) [countysub-zip (Available 2nd Quarter 2018 onwards)] `Crosswalk county subdivision (countysub) to zipcode`_

The first geoid type in the function call is what to query for. For
example in 1) above, 'zip' is the first geoid and 'tract' is the second geoid.

The second geoid in the function call describes the geoid which we want to 
determine 'intersection' with the first geoid where intersection is described
as the % of residential, business, other, and total buildings that overlap. 

For example, in function call #7, we might have a county called 22031 
which has zip codes 71052, 71078, 71049, 71032 ... where the residential 
% (res_ratio) of each zip is 0.38, 0.21, 0.11, 0.05 ... respectively. 
Of all these zipcodes' res_ratios, when added up will equal 1,
signaling these grouping of zip codes make up 100% of residential address in the
county with each zipcode taking up their respective residential percentage.

Disclaimer: Although there exists inverse relationships in the Crosswalk 
Files, the measurements are NOT COMPLETELY inverse -- for reasons stated
within the papers above.

These are basic examples which shows you to query the Crosswalk API. Before
looking at the outputted data I RECOMMEND first taking a look at [the parameters] `Parameters`_
as well as [return data] `Returns`_ located at the bottom of the page.

Crosswalk zipcode to census tract
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_zip_tract(zip = '35213', year = ['2010'], quarter = ['1'])

Crosswalk zipcode to county fip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_zip_county(zip = 35213, year = ['2020'], quarter = ['2'])

Crosswalk zipcode to core base statistical area (cbsa)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python
    
    hud_cw_zip_cbsa(zip = 35213, year = ['2011'], quarter = ['3'])


Crosswalk zipcode to core based statistical area division (cbsadiv)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_zip_cbsadiv(zip = '22031', year = ['2019'], quarter = ['4'])


Crosswalk zipcode to congressional district (cd)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_zip_cd(zip = '35213', year = [2011]), quarter = [1]))

Crosswalk census tract to zipcode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_tract_zip(tract = 48201223100, year = ['2017'], quarter = ['1'])

Crosswalk county fip into zipcode 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_county_zip(county = '22031', year = ['2010'], quarter = ['1'])

Crosswalk core based statistical areas (cbsa) to zipcode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_cbsa_zip(cbsa = '10140', year = ['2017'], quarter = ['2'])


Crosswalk core based statistical areas division (cbsadiv) to zipcode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python
    
    hud_cw_cbsadiv_zip(cbsadiv = 10380, year = ['2017'], quarter = ['4'])


Crosswalk congressional district (cd) to zipcode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_cd_zip(cd = '2202', year = ['2010'], quarter = ['4'])


Crosswalk zipcode to county subdivision (countysub)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python
    
    hud_cw_zip_countysub(zip = '35213', year = ['2019'], quarter = ['2'])


Crosswalk county subdivision (countysub) to zipcode 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Python

    hud_cw_countysub_zip(countysub = '4606720300 ', year = ['2019', '2019', '2019'], quarter = ['4','4'])

Querying for only the crosswalked geoids
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you just want the crosswalked geoids, you can set the **minimal** argument 
to TRUE. This will return a vector containing the crosswalked geoids
without the extra metadata.

.. code-block:: Python
    
    hud_cw_county_zip(county = '22031', year = ['2010'], quarter = ['1'], minimal = TRUE)

Using the omni function for querying
====================================

The omni function is a redundant implementation of the functions shown above
that requires specifying the type which can be from 1-12. The type argument
follows the number scheme described at within the [input arguments][Input Arguments]. You also 
must use the 'query' argument (i.e query = 22031) for inputting geoids instead 
of the specific geoid names (i.e county = 22031, cd = 7200) used by the 
above functions.

.. code-block:: Python
    
    hud_cw(type = 7, query = '22031', year = ['2010'], quarter = ['1'])

Crosswalking a dataset
======================

For those who need to apply an allocation method (residential, business, other,
total) to individual items in a data set, the **crosswalk()** function is available. 
Lets say we wanted to know the population at a zip code level (there is likely 
already a data set for this) for the counties of Washington, Wicomico, 
and Worchester in Maryland in the year 2019. 

NOTE: The use of the crosswalk() function is likely best suited for datasets 
that are not described in the geographic identifier we want to crosswalk to. In
this case population might not be the best example for this.

.. code-block:: Python

    sample = data.frame(pop = [151049, 103609, 52276),
                        county = ["24043", "24045", "24047"))

    head(sample)

In the crosswalked data set below each zip code associated with a county 
is assigned the same population value.

.. code-block:: Python

    crosswalk(data = sample, geoid = "county", geoid_col = "county",
              cw_geoid = "zip", cw_geoid_col = NA, method = NA,
              year = 2019, quarter = 1)

To utilize an allocation method provided by the crosswalk files and apply it
to columns of the data set, specify the method and cw_geoid_col arguments.
In this case we want to allocate the county population levels to a zip code
level using the method based on the ratio of residential addresses.

.. code-block:: Python

    crosswalk(data = sample, geoid = "county", geoid_col = "county",
              cw_geoid = "zip", cw_geoid_col = "pop", method = "res",
              year = 2019, quarter = 1)

Geo-in-geo functions: does one geography overlap another?
=========================================================

This library also allows the user to determine if one geography overlaps
another.

Disclaimer: Overlap is not determined by whether the boundaries intersect, but
rather if any addresses lie in both. 

This allows you to specify the year, quarter, and key arguments.

.. code-block:: Python

    z_in_cbsa(zip = 71052, cbsa = 43340, year = 2019, quarter = 2)

Most recent USPS Crosswalk files
================================

To get the most recent crosswalk files by year and quarter:

.. code-block:: Python
    
    hud_rec_cw_yr()

Parameters
==========


Returns
=======

References
==========

Din, Alexander and Wilson, Ron, 2020. "Crosswalking ZIP Codes to Census 
       Geographies: Geoprocessing the U.S. Department of Housing & Urban Development’s
       ZIP Code Crosswalk Files," Cityscape: A Journal of Policy Development and
       Research, Volume 22, Number 1, https://www.huduser.gov/portal/periodicals/cityscpe/vol22num1/ch12.pdf
   
Katy Rossiter, K. R. (2014, July 31). Standard Hierarchy of Census Bereau
       Geographies [Photograph]. Understanding Geographic Relationships: Counties,
       Places, Tracts and More.
       https://www.census.gov/newsroom/blogs/random-samplings/2014/07/understanding-geographic-relation
       ships-counties-places-tracts-and-more.html

U.S Department of Housing and Urban Development. (n.d.). HUD USPS ZIP
       Code Crosswalk Files | HUD USER. HUD  USPS ZIP CODE CROSSWALK FILES.
       Retrieved February 17, 2022, from 
       https://www.huduser.gov/portal/datasets/usps_crosswalk.html

Wilson, Ron and Din, Alexander, 2018. “Understanding and Enhancing the U.S.
       Department of Housing and Urban Development’s ZIP Code Crosswalk Files,”
       Cityscape: A Journal of Policy Development and Research, Volume 20 Number 2, 277
       – 294.
