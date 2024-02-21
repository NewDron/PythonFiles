def is_year_leap(aasta:int)->bool:
    """True kui aasta on liigaasta ja False kui on tavaline aasta.
       param int aasta: Kasutaja sisestab aasta ja järjekorranumbri
       rtype:bool
    """
    if aasta%4==0:
        tüüp=True
    else:
        tüüp=False
    return tüüp
