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
looking at the examples I RECOMMEND first looking at [the parameters][Parameters]
as well as [return data][Returns] located at the bottom of the page.

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
```{r, eval=FALSE}
# These functions gets FMR data for the state of Virginia in 2021.
hud_fmr(query = 'VA', year = '2021')

hud_fmr(query= "Virginia", year = '2021')

hud_fmr(query= "51", year = '2021')
```


If you only need the county level data, then this might work better...

```{r, eval=FALSE}
# These functions gets FMR data for the state of Virginia in 2021 for counties.
hud_fmr_state_counties(state = 'VA', year = '2021')

hud_fmr_state_counties(state = "Virginia", year = '2021')

hud_fmr_state_counties(state = "51", year = '2021')
```


If you need just metro data...

```{r, eval=FALSE}
# These functions gets FMR data for the state of Virginia in 2021 for metroareas.
hud_fmr_state_metroareas(state = 'VA', year = '2021')

hud_fmr_state_metroareas(state = "Virginia", year = '2021')

hud_fmr_state_metroareas(state = "51", year = '2021')
```


County Level Fair Markets Rent
===============================

This is an example which shows you how to query the Fair Markets Rent on a
county level basis. These are defined with a 2 digit state code + 3 digit county
code. You also need a 99999 code added onto the end. I recommend taking a 
look at [US Counties][] to determine what counties are available.

```{r, eval=FALSE}
# Getting a county requires a 2 digit state fipscode + 3 digit county fipscode + 99999
hud_fmr(query = '0100199999', year = '2017')
```


You can also choose to use:
```{r, eval=FALSE}
# Getting a county requires a 2 digit state fipscode + 3 digit county fipscode + 99999
hud_fmr_county_zip(county = '0100199999', year = '2017')
```


Small Areas Fair Markets Rent
====================================

```{r, eval=FALSE}
# Gets FMR data for METRO area.
hud_fmr(query = "METRO47900M47900", year=c(2018))
```


You can also choose to use:
```{r, eval=FALSE}
# Getting a county requires a 2 digit state fipscode + 3 digit county fipscode + 99999
hud_fmr_metroarea_zip(metroarea = 'METRO47900M47900', year = '2017')
```


Most recent Fair Markets Rent files
====================================

To get the most recent Fair Markets Rent files by year:

```{r, eval = if(Sys.getenv("HUD_KEY") == "") FALSE else TRUE }
rhud::hud_rec_fmr_yr()

```


Querying for Geographic Identifers
====================================

US States
---------
This is an example to show you how to query for all states in the US.

```{r, eval=FALSE}
library(rhud)
hud_nation_states_territories()
```


US Counties 
-----------
This is an example to show you how to query for all counties in MD,
Virginia, and California, respectively.

```{r, eval=FALSE}
hud_state_counties("MD")

hud_state_counties("Virginia")

hud_state_counties("6")
```


US Metropolitan Areas
---------------------

This is an example to show you how to query for metropolitan areas in Wyoming
and New York.
```{r, eval=FALSE}
hud_state_metropolitan(c("WY", "NY"))
```


Parameters
==========

Returns
==========



References
==========

"What Is Fair Market Rent? | RentData.org." Www.rentdata.org,
        www.rentdata.org/articles/what-is-fair-market-rent. Accessed 18 Feb. 2022.

"Fair Market Rents | HUD USER." Huduser.gov, U.S Department of Housing and Urban
        Development, 2017, www.huduser.gov/portal/datasets/fmr.html.
