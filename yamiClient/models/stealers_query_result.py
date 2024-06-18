from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.credit_card import CreditCard
    from ..models.ftp_credential import FTPCredential
    from ..models.password import Password
    from ..models.rdp_credential import RDPCredential
    from ..models.stolen_file import StolenFile
    from ..models.token import Token
    from ..models.user_log import UserLog


T = TypeVar('T', bound='StealersQueryResult')


@_attrs_define
class StealersQueryResult:
    """
    Attributes:
        user (UserLog):
        passwords (List['Password']):
        rdp_credentials (List['RDPCredential']):
        ftp_credentials (List['FTPCredential']):
        tokens (List['Token']):
        credit_cards (List['CreditCard']):
        stolen_files (List['StolenFile']):
    """

    user: 'UserLog'
    passwords: List['Password']
    rdp_credentials: List['RDPCredential']
    ftp_credentials: List['FTPCredential']
    tokens: List['Token']
    credit_cards: List['CreditCard']
    stolen_files: List['StolenFile']
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user.to_dict()

        passwords = []
        for passwords_item_data in self.passwords:
            passwords_item = passwords_item_data.to_dict()
            passwords.append(passwords_item)

        rdp_credentials = []
        for rdp_credentials_item_data in self.rdp_credentials:
            rdp_credentials_item = rdp_credentials_item_data.to_dict()
            rdp_credentials.append(rdp_credentials_item)

        ftp_credentials = []
        for ftp_credentials_item_data in self.ftp_credentials:
            ftp_credentials_item = ftp_credentials_item_data.to_dict()
            ftp_credentials.append(ftp_credentials_item)

        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data.to_dict()
            tokens.append(tokens_item)

        credit_cards = []
        for credit_cards_item_data in self.credit_cards:
            credit_cards_item = credit_cards_item_data.to_dict()
            credit_cards.append(credit_cards_item)

        stolen_files = []
        for stolen_files_item_data in self.stolen_files:
            stolen_files_item = stolen_files_item_data.to_dict()
            stolen_files.append(stolen_files_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'user': user,
                'passwords': passwords,
                'rdp_credentials': rdp_credentials,
                'ftp_credentials': ftp_credentials,
                'tokens': tokens,
                'credit_cards': credit_cards,
                'stolen_files': stolen_files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credit_card import CreditCard
        from ..models.ftp_credential import FTPCredential
        from ..models.password import Password
        from ..models.rdp_credential import RDPCredential
        from ..models.stolen_file import StolenFile
        from ..models.token import Token
        from ..models.user_log import UserLog

        d = src_dict.copy()
        user = UserLog.from_dict(d.pop('user'))

        passwords = []
        _passwords = d.pop('passwords')
        for passwords_item_data in _passwords:
            passwords_item = Password.from_dict(passwords_item_data)

            passwords.append(passwords_item)

        rdp_credentials = []
        _rdp_credentials = d.pop('rdp_credentials')
        for rdp_credentials_item_data in _rdp_credentials:
            rdp_credentials_item = RDPCredential.from_dict(rdp_credentials_item_data)

            rdp_credentials.append(rdp_credentials_item)

        ftp_credentials = []
        _ftp_credentials = d.pop('ftp_credentials')
        for ftp_credentials_item_data in _ftp_credentials:
            ftp_credentials_item = FTPCredential.from_dict(ftp_credentials_item_data)

            ftp_credentials.append(ftp_credentials_item)

        tokens = []
        _tokens = d.pop('tokens')
        for tokens_item_data in _tokens:
            tokens_item = Token.from_dict(tokens_item_data)

            tokens.append(tokens_item)

        credit_cards = []
        _credit_cards = d.pop('credit_cards')
        for credit_cards_item_data in _credit_cards:
            credit_cards_item = CreditCard.from_dict(credit_cards_item_data)

            credit_cards.append(credit_cards_item)

        stolen_files = []
        _stolen_files = d.pop('stolen_files')
        for stolen_files_item_data in _stolen_files:
            stolen_files_item = StolenFile.from_dict(stolen_files_item_data)

            stolen_files.append(stolen_files_item)

        stealers_query_result = cls(
            user=user,
            passwords=passwords,
            rdp_credentials=rdp_credentials,
            ftp_credentials=ftp_credentials,
            tokens=tokens,
            credit_cards=credit_cards,
            stolen_files=stolen_files,
        )

        stealers_query_result.additional_properties = d
        return stealers_query_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
