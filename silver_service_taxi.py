from prac8.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def _int_(self,name="",fuel=0,fancifulness=1.0):
        super()._init_(name,fuel)
        self.fancifulness = fancifulness
        self.price_per_km = Taxi.price_per_km * self.fancifulness

    def get_fare(self):
        return( super().get_fare()+self.flagfall )

    def _str_(self):
        pass


if SilverServiceTaxi == '_main_':
        silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
        silver_taxi.drive(50)
        print("Current fare: $(:.2f)".format(silver_taxi.get_fare()))