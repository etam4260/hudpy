import os

def hud_set_cache_dir(path):
    """
    Set the caching directory to store data retrieved using the
    rhud API calls. By default, rhud uses a non-persistent temporary directory
    given for an R session. However, it is possible that a user might want
    to save their queried data in a custom location which is persistent.
    This function allows users to set the cache directory. The user can also
    store the preferred path in the .RProfile so that rhud will remember the set
    preference directory throughout sessions. Make sure the path is valid and
    and is not in a sensitive location.

    Windows users: please note that you'll need to use double-backslashes or
    forward slashes when specifying your cache directory's path in R.

    * This will create a folder called rhud_cache in specified path

    * If setting a new directory, the previous cache will not be cleaned. In
    a future update there will be a garbage collection option.

    Parameters
    ----------
    path : The full path to the desired cache directory. Only one can be
        set at a time. If no path is specified, it will use the temp directory
        for R. The temp directory is not persistent.
    
    in_wkdir : Store the path as environment variable in the working directory
        .Rprofile so rhud will cache to this specified path.
    
    in_home : Store the path as environment variable in the HOME directory
        .Rprofile so rhud will cache to this specified path.
    
    See Also
    --------

    * hud_get_cache_dir()
    * hud_set_cache_dir()
    * hud_clear_cache()
     
    Examples
    --------

    >>> hud_set_cache_dir("./an/example/path", in_wkdir = TRUE, in_home = TRUE)

    """

    # Set for the rhud cache path in the current session.

    # TODO: First check for valid path formatting by regex

def hud_get_cache_dir():
    """
    @name hud_get_cache_dir
    @title hud_get_cache_dir
    @description Get the path rhud is using to store cached files.
    @returns A character vector with path to cached files. If none is set,
    will default to R temp session directory
    @export
    @seealso
    * [rhud::hud_get_cache_dir()]
    * [rhud::hud_set_cache_dir()]
    * [rhud::hud_clear_cache()]
    @examples
    \dontrun{
    library(rhud)

    hud_get_cache_dir()

    }
    """
        
    return(os.getenv("RHUD_CACHE_DIR"))



def hud_clear_cache():
    """
    Remove cached data from the caching directory that is used to
    store data retrieved using the rhud API calls. By default, rhud uses a
    non-persistent temporary directory given for an R session, but a user might
    have set another directory to use.

    See Also
    --------

    * hud_get_cache_dir()
    * hud_set_cache_dir()
    * hud_clear_cache()
    
    Examples
    --------
    >>>  hud_clear_cache()

    """
    if (os.getenv("RHUD_CACHE_DIR") == "" or \
        os.getenv("RHUD_CACHE_DIR") == None):

        # Clear the cache directory of python temp... 
        # tempdir() +  "//" + "rhud_cache"
    else:
        # os.getenv("RHUD_CACHE_DIR")
    