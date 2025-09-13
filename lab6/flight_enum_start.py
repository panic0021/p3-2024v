from enum import Enum

class UslugaNaLetu(Enum):

    IZBOR_SEDISTA='izbor sedista'
    OBROK='obrok'
    WIFI='wifi'
    OSIGURANJE_LETA='osiguranje leta'
    PRIORITETNO_UKRCAVANJE='prioritetno ukrcavanje'

    @staticmethod
    def valid_service_str(param_str):
        for service in UslugaNaLetu:
            if service.value.lower()==param_str.lower():
                return True
        return False
    @staticmethod
    def get_service_from_str(param_str):
        for service in UslugaNaLetu:
            if service.value.lower()==param_str.lower():
                return service
        return None


if __name__=='__main__':
    print(UslugaNaLetu.valid_service_str('wifi'))
    print(UslugaNaLetu.get_service_from_str('izbor sedista'))