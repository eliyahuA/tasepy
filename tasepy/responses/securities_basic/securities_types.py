from ..responses import ResponseComponent, Root


class SecurityTypeItem(ResponseComponent):
    """Individual security type classification information.
    
    Represents a security type with hierarchical classification codes
    and descriptive names for main categories and specific subtypes.
    """
    security_main_type_code: str
    security_main_type_desc: str
    security_full_type_code: str
    security_type_desc: str


class SecuritiesTypes(ResponseComponent):
    """Complete securities types response from TASE securities API.
    
    Contains the full classification system for securities types traded
    on the Tel Aviv Stock Exchange with hierarchical type codes and descriptions.
    """
    securities_types: Root[SecurityTypeItem]