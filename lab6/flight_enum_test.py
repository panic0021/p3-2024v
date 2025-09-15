from enum import Enum


class UslugaNaLetu(Enum):

    IZBOR_SEDISTA='izbor sedista'
    OBROK='obrok'
    WIFI='wifi'
    OSIGURANJE_LETA='osiguranje leta'
    PRIORITETNO_UKRCAVANJE='prioritetno ukrcavanje'

    @staticmethod
    def valid_service_str(s):
        for item in UslugaNaLetu:
            if item.value==s.lower():
                return True
        return False
    
    @staticmethod
    def get_service_from_str(s):
        for item in UslugaNaLetu:
            if item.value==s.lower() or item.name.lower()==s.lower():
                print(item.name)
                return item
        return None



if __name__=='__main__':
    s='IZBOR_SEDISTA'
    print(UslugaNaLetu.valid_service_str(s))
    print(UslugaNaLetu.get_service_from_str(s))