.. hudpy documentation master file, created by
   sphinx-quickstart on Tue May 17 16:45:51 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to hudpy!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   setup
   usps_crosswalk
   fair_markets_rent
   income_limits
   comprehensive_housing_and_affordability
   changelog
   authors
   modules


Getting Started
===============
-   This interface uses the HUD User Data API but is not endorsed or
    certified by HUD User.

To install from pypi use:

.. code-block:: Bash
    
    pip install hudpy


You can install the development version by cloning the repository:

.. code-block:: Bash
    
    git clone https://github.com/etam4260/hudpy.git


now run:

.. code-block:: Bash
    
    pip install ./hudpy



Key Access
----------

To use functions provided by this package, you need to get access HUD
USER via token. Go to <https://www.huduser.gov/hudapi/public/login> to
register for an account and then create a token with access to all
datasets provided by HUD. This will include selecting USPS Crosswalk,
Fair Markets Rent, Income Limits, and Comprehensive Housing
Affordability Strategy.

Now copy and paste that key into the hud_set_key() function.


.. code-block:: Python

   hud_set_key("sample-key")

Simplistic Example
------------------

This sample provided below shows how to query the USPS Crosswalk API


.. code-block:: Python

   hud_cw_zip_tract(zip = '35213', year = ['2010'], quarter = ['1'])


What is hudpy?
==============

The goal of this project is to provide an easy-to-use interface to
access various open-source APIs provided by the U.S Housing and Urban
Development. These include the USPS Crosswalk Files, Fair Markets Rent,
Income Limits, and Comprehensive Housing and Affordability Strategy.
Although HUD does provide datasets for other programs, they are
currently not supported by an API.

Please read
<https://www.huduser.gov/portal/dataset/api-terms-of-service.html> for
all terms of service.

According to HUD USER:

All services, which utilize or access the API, should display the
following notice prominently within the application: ???This product uses
the HUD User Data API but is not endorsed or certified by HUD User.??? You
may use the HUD User name in order to identify the source of API content
subject to these rules. You may not use the HUD User name, or the like
to imply endorsement of any product, service, or entity, not-for-profit,
commercial or otherwise.


Citation
========

Please cite this package using:

Tam E, Reilly A, Ghaedi H, Jin S (2022). rhud: A Python Interface to the
HUD (US Department of Housing and Urban Development) APIs. 0.1.0.9000,  
<https://github.com/etam4260/hudpy/>.

Available Data
--------------

The APIs and datasets which this library interfaces are listed below.
The HUD also provide miscellaneous supplemental APIs under them.

1.  HUD User

-   USPS Crosswalk
    (<https://www.huduser.gov/portal/dataset/uspszip-api.html>)

.. list-table:: 
   :widths: 100 100
   :header-rows: 1

   * - USPS Crosswalk Files 
     - Years   

   * - `hud_cw_zip_tract()` 
     - 2010-2021 
   
   * - `hud_cw_zip_county()` 
     - 2010-2021

   * - `hud_cw_zip_cbsa()` 
     - 2010-2021
   
   * - `hud_cw_zip_cbsadiv()` 
     - 2017-2021

   * - `hud_cw_zip_countysub()` 
     - 2018-2021
   
   * - `hud_cw_zip_cd()` 
     - 2010-2021

   * - `hud_cw_tract_zip()` 
     - 2010-2021

   * - `hud_cw_county_zip()` 
     - 2010-2021

   * - `hud_cw_cbsa_zip()` 
     - 2010-2021

   * - `hud_cw_cbsadiv_zip()` 
     - 2017-2021

   * - `hud_cw_cd_zip()` 
     - 2010-2021

   * - `hud_cw_countysub_zip()` 
     - 2018-2021

   * - `hud_cw()` 
     - 2010-2021

   * -
     -

   * - `crosswalk()` 
     - 2010-2021

   * -
     -

   * - `z_in_trt()`  
     - 2010-2021

   * - `z_in_cty()`  
     - 2010-2021

   * - `z_in_cbsa()`  
     - 2010-2021

   * - `z_in_cbsadiv()`  
     - 2017-2021

   * - `z_in_ctysb()`  
     - 2018-2021

   * - `z_in_cd()`  
     - 2010-2021

   * - `trt_in_z()`  
     - 2010-2021

   * - `cty_in_z()`  
     - 2010-2021

   * - `cbsa_in_z()`  
     - 2010-2021

   * - `cbsadiv_in_z()`  
     - 2017-2021

   * - `ctysb_in_z()`  
     - 2018-2021

   * - `cd_in_z()`  
     - 2010-2021

-   Fair Markets Rent
    (<https://www.huduser.gov/portal/dataset/fmr-api.html>)
    -   Small Areas Fair Markets Rent

.. list-table:: 
   :widths: 100 100
   :header-rows: 1

   * - Fair Markets Rent
     - Years   

   * - `hud_fmr_state_counties()`
     - 2017-2022 

   * - `hud_fmr_state_metroareas()`
     - 2017-2022 

   * - `hud_fmr_county_zip()` 
     - 2017-2022 

   * - `hud_fmr_metroarea_zip()` 
     - 2017-2022 

   * - `hud_fmr()`
     - 2017-2022 
 

-   Income Limits
    (<https://www.huduser.gov/portal/dataset/fmr-api.html>)

.. list-table:: 
   :widths: 100 100
   :header-rows: 1

   * - Income Limits
     - Years

   * - `hud_il()`
     - 2017-2022

-   Comprehensive Housing and Affordability Strategy
    (<https://www.huduser.gov/portal/dataset/chas-api.html>)

.. list-table:: 
   :widths: 100 100
   :header-rows: 1

   * - Comprehensive Housing and Affordability Strategy
     - Years

   * - `hud_chas_nation()` 
     - 2014-2018 , 2013-2017, 2012-2016, 2011-2015, 2010-2014, 2009-2013, 2008-2012, 2007-2011, 2006-2010

   * - `hud_chas_state()`   
     - 2014-2018 , 2013-2017, 2012-2016, 2011-2015, 2010-2014, 2009-2013, 2008-2012, 2007-2011, 2006-2010

   * - `hud_chas_county()`
     - 2014-2018 , 2013-2017, 2012-2016, 2011-2015, 2010-2014, 2009-2013, 2008-2012, 2007-2011, 2006-2010

   * - `hud_chas_state_mcd()`   
     - 2014-2018 , 2013-2017, 2012-2016, 2011-2015, 2010-2014, 2009-2013, 2008-2012, 2007-2011, 2006-2010

   * - `hud_chas_state_place()` 
     - 2014-2018 , 2013-2017, 2012-2016, 2011-2015, 2010-2014, 2009-2013, 2008-2012, 2007-2011, 2006-2010

   * - `hud_chas()`
     - 2014-2018 , 2013-2017, 2012-2016, 2011-2015, 2010-2014, 2009-2013, 2008-2012, 2007-2011, 2006-2010

-   US Geographic Entities

.. list-table:: 
   :widths: 100 
   :header-rows: 1

   * - US Geographic Entities

   * - `hud_nation_states_territories()`

   * - `hud_state_metropolitan()`

   * - `hud_state_counties()`

   * - `hud_state_places()`

   * - `hud_state_minor_civil_divisions()`

-   Key access

.. list-table:: 
   :widths: 100 
   :header-rows: 1

   * - Key Access

   * - `hud_set_key()`  

   * - `hud_get_key()`

   * - `hud_set_user_agent()`

   * - `hud_get_user_agent()`

-   Caching

.. list-table:: 
   :widths: 100
   :header-rows: 1

   * - Caching

   * - `hud_set_cache_dir()`
     
   * - `hud_get_cache_dir()`
     
   * - `hud_clear_cache()`


- Utilities

.. list-table:: 
   :widths: 100
   :header-rows: 1

   * - Utilities

   * - `rhud_website()`
     
   * - `hud_rec_cw_yr()`
     
   * - `hud_rec_fmr_yr()`
   
   * - `hud_rec_il_yr()`
   


Contributors
============

-   Emmet Tam(<https://github.com/etam4260>)\[<emmet_tam@yahoo.com>\]
-   Allison Reilly()\[<areilly2@umd.edu>\]
-   Hamed Ghaedi()\[<hghaedi@terpmail.umd.edu>\]
-   Shuyu Jin(<https://github.com/geojsy>)\[<geojsy@umd.edu>\]

Disclaimers
===========

-   License: GPL >= 2

-   This interface uses the HUD User Data API but is not endorsed or
    certified by HUD User.

-   The limit on the maximum number of API calls is 1200 queries a min.
    Each function call does not correspond to a single API call!

-   This is a WIP so please report any issues or bugs to:
    <https://github.com/etam4260/hudpy/issues>

-   This is open source, so please fork and introduce some pull
    requests!

References
==========

HUD User Home Page: HUD USER. HUD User Home Page \| HUD USER. (n.d.).
Retrieved February 24, 2022, from <https://www.huduser.gov/portal/home.html>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
