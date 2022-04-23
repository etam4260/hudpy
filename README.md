
# hudpy <img src='logo.png' align="right" width="139"/>


<!-- badges: start -->

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![Codecov test
coverage](https://codecov.io/gh/etam4260/hudr/branch/main/graph/badge.svg)](https://codecov.io/gh/etam4260/hudr?branch=main)
<br/><br/> [![devel
version](https://img.shields.io/badge/devel%20version-0.1.0-yellow)]()

<!-- badges: end -->


## Housing and Urban Development in Python

-   This interface uses the HUD User Data API but is not endorsed or
    certified by HUD User.

The goal of this project is to provide an easy-to-use interface to
access various open-source APIs provided by the U.S Housing and Urban
Development. These include the USPS Crosswalk Files, Fair Markets Rent,
Income Limits, and Comprehensive Housing and Affordability Strategy.
Although HUD does provide datasets for other programs, they are
currently not supported by an API.

HUD has two websites for gaining access to various data sets: HUD User
and Exchange.

According to HUD USER:

All services, which utilize or access the API, should display the
following notice prominently within the application: “This product uses
the HUD User Data API but is not endorsed or certified by HUD User.” You
may use the HUD User name in order to identify the source of API content
subject to these rules. You may not use the HUD User name, or the like
to imply endorsement of any product, service, or entity, not-for-profit,
commercial or otherwise.

## HUD User: <https://www.huduser.gov/portal/datasets>

According to (HUD User Home Page \| HUD USER), HUD User is a U.S.
Department of Housing and Urban Development information source that
includes reports and reference documents. HUD USER was founded in 1978
by the Department of Housing and Urban Development’s Office of Policy
Development and Research.

HUD User maintains an API to gain access to their data. However, their
API system can be confusing and provides their information in JSON
format rather than a data-frame like object. Although there exist file
downloadables, R users may want to be able to extract specific bits of
the data into memory.

## HUD Exchange: <https://www.hudexchange.info/programs/drgr/>

According to (Disaster Recovery Grant Reporting System, 2022), HUD
Exchange is a comprehensive online platform that provides tools,
resources, and contact information for organizations and individuals who
engage with HUD. Nonprofit organizations and state and municipal
governments are frequently included, but borrowers, lenders, and brokers
involved in HUD’s multifamily loan programs are also included.

The DRGR Disaster Recovery Grant Reporting System which HUD Exchange
uses to supply public data does not have an active API for retrieving
information. However, there does exist data sets freely available online
which can be directly downloadable into R. This package provides the
ability to directly get such data.

## Citation

Please cite this package using:

Tam, E., Reilly, A., & Ghaedi, H. (2022). hudpy: A python interface for
accessing HUD <br/>   (US Department of Housing and Urban Development)
APIs (Version 0.1.0). <https://github.com/etam4260/hudpy>

## Available Data

The APIs and datasets which this library interfaces are listed below.
The HUD also provide miscellaneous supplemental APIs under them.

1.  HUD User

    -   USPS Crosswalk
        (<https://www.huduser.gov/portal/dataset/uspszip-api.html>)
    -   Fair Markets Rent
        (<https://www.huduser.gov/portal/dataset/fmr-api.html>)
        -   Small Areas Fair Markets Rent
        -   List States
        -   List Small Areas
    -   Income Limits
        (<https://www.huduser.gov/portal/dataset/fmr-api.html>)
    -   Comprehensive Housing and Affordability Strategy
        (<https://www.huduser.gov/portal/dataset/chas-api.html>)
        -   List Counties in State
        -   List MCDs in State
        -   List All Cities in State

2.  HUD Exchange

    -   Community Development Block Grant - Disaster Recovery
        (<https://drgr.hud.gov/public/index.html>)

## Installation

You can install the development version from
[GitHub](https://github.com/) with:

## Contributors

-   Emmet Tam(<https://github.com/etam4260>)\[<emmet_tam@yahoo.com>\]
-   Allison Reilly()\[<areilly2@umd.edu>\]
-   Hamed Ghaedi()\[<hghaedi@terpmail.umd.edu>\]

## Disclaimers

-   License: GPL2

-   This interface uses the HUD User Data API but is not endorsed or
    certified by HUD User.

-   The limit on the maximum number of API calls is 1200 queries a min.
    Each function call does not correspond to a single API call!

-   This is a WIP so please report any issues or bugs to:
    <https://github.com/etam4260/hudpy/issues>

-   This is open source, so please fork and introduce some pull
    requests!

## References

Disaster Recovery Grant Reporting System. (2022). HUD Exchange.
Retrieved <br />  February 19, 2022, from
<https://www.hudexchange.info/programs/drgr/>

HUD User Home Page: HUD USER. HUD User Home Page \| HUD USER. (n.d.).
Retrieved <br />  February 24, 2022, from
<https://www.huduser.gov/portal/home.html>
