import datetime as dt
import decimal

class PowerMeter:
    
    def __init__(self):
        charges: dict[dt.date, decimal.Decimal] = {}
        tariff1: numbers.Number = 5.18 # за кВт/ч дневной тариф
        tariff2: numbers.Number = 3.59 # за кВт/ч ночной тариф
        tariff2_starts: datetime.time = dt.time(7, 0, 0) # начало дневного тарифа
        tariff2_ends: datetime.time = dt.time(23, 0, 0) # конец дневного тарифа
        
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.tariff1 = tariff1
        self.tariff2 = tariff2
        self.charges = charges
        self.all_power = 0
        
    def __repr__(self):
        return f'<PowerMeter: {self.all_power} кВт/ч>' # машиночитаемый
    
    def __str__(self):
        current_month = dt.datetime.now().strftime('%B')[:3]
        return f'({current_month}) {self.charges[current_month]}' # человекочитаемый
        
    def meter(self, power):
        power: numbers.Number = power
        self.all_power += power
        current_month = dt.datetime.now().strftime('%B')[:3]
        current_time = dt.datetime.now().time()
        
        if current_month not in self.charges:
            self.charges[current_month] = 0
        
        if self.tariff2_starts <= current_time <= self.tariff2_ends:
            price = decimal.Decimal(power*self.tariff1).quantize(decimal.Decimal("1.00"))    
        else:
            price = decimal.Decimal(power*self.tariff2).quantize(decimal.Decimal("1.00"))
        
        self.charges[current_month] += price
        return price

# >>> pm1 = PowerMeter()
# >>>
# >>> pm1.meter(3)
# Decimal('15.54')
# >>> pm1.meter(2.6)
# Decimal('13.47')
# >>>
# >>> pm1
# <PowerMeter: 5.6 кВт/ч>
# >>> print(pm1)
# (Mar) 29.01