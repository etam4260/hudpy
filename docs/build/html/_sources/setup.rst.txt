Setup
=====

Are you a R developer? Check out [rhud](https://github.com/etam4260/rhud) instead.


To install from pypi use:

.. code-block:: Bash

    pip install hudpy


You can install the development version by cloning the repository

.. code-block:: Bash

    git clone https://github.com/etam4260/hudpy.git


and then running...

.. code-block:: Bash

    pip install hudpy


The US Department of Housing and Urban Development HUD USER requires users 
to gain an access key before querying their systems. You must go to 
https://www.huduser.gov/hudapi/public/register?comingfrom=1 and follow the 
instructions for making an account.

From the website, you need to make a new token. Make sure to save the token
somewhere as you will only be able to view it once. However, you can use it as
many times as you want. You can now supply the 'key' argument to the function
calls.


Setting the Key
-----------------

.. code-block:: Python

    hud_set_key("2yeuduhq72ueajk", in_home = TRUE)


You can also tell RStudio to remember the key by setting `in_wkdir` and
`in_home` parameter to `TRUE` which will write Sys.setenv("your-key") to your
.Rprofile.


To check whether rhud can gain access to this environment variable...

.. code-block:: Python

    hud_get_key()

It is now set up for the rest of the R session.

Setting a user agent
--------------------


It is recommended to set a user agent before querying. This tells the HUD
servers a bit more about the querying application or user.

.. code-block:: Python

    hud_set_user_agent("This Application")


If no user agent is set, it will return an empty string.

.. code-block:: Python

    hud_get_user_agent()    


Understanding the Syntax
------------------------

A noticeable issue with querying geographic data is determining what resolution
the data is returned in. Therefore, understanding the syntax of 
these function calls should easily help you determine what you are querying 
and what data is returned.

The general syntax for these functions within the package follow this pattern
where {1},{2}, and {3} are placeholders:

hud\_{1}\_{2}\_{3}


{1}: This symbol represents the dataset to query for. So for example if you want
fair markets rent data, this will be 'fmr'. If you want data from the crosswalk
files, this will be 'cw'.

{2}: This symbol represents the geographic resolution to query for. 
For example, if the function requires that you input state(s), then this 
will be named as 'state.' If the function requires that you input
county(s) then this will be 'county'.

{3}: This symbol represented the output geographic resolution. So for example,
if we want data at a zip code level, then this will have 'zip'.

For those that do not have the {2} and {3}, these are omni functions which 
are capable of performing all queries under {1}, but these functions are
harder to understand.

For those that do not have the {3}, it inherits the {2}. This means that 
if {2} is a state input, then the data described by the output data is also
a state.

A quick example:

.. code-block:: Python

    hud_cw_county_zip(county = 22031, year = c('2017'), quarter = c('1'))


The first part of the function begins with 'hud'.

The second part is 'cw' meaning we are querying the crosswalk files.

The third part is 'county' meaning we need to input county(s)

The fourth part is the 'zip' meaning the data will be returned 
at a zip code resolution.



Additional Help
---------------

If you ever get confused or need help you can easily revisit this website 
where you can check the all the function definitions in the
***Reference*** tab.


.. code-block:: Python

    rhud_website()  


This will quickly open up this website on your web browser
as well as the github repository where you can submit issues.

