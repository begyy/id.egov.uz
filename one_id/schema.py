from dataclasses import dataclass
from typing import List, Optional


@dataclass
class LegalInfo:
    is_basic: bool
    tin: str
    acron_UZ: str
    le_tin: str
    le_name: str


@dataclass
class User:
    user_id: str
    user_type: str
    email: str
    first_name: str
    sur_name: str
    mid_name: str
    full_name: str
    mob_phone_no: str
    birth_date: str
    tem_adr: str
    gd: str
    per_adr: str
    birth_place: str
    birth_cntry: str
    natn: str
    ctzn: str
    pport_issue_place: str
    pport_issue_date: str
    pport_expr_date: str
    ret_cd: str
    valid: bool
    pin: str
    tin: str
    pport_no: str
    sess_id: str
    legal_info: Optional[List[LegalInfo]]
