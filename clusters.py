class Bill:
    def __init__(self, litur, tegund, hradi):
        self.litur = litur
        self.tegund = tegund
        self.hamarkshradi = hradi

    def afram(self):
        print(f"{self.tegund} fer áfram! brúmm brúmm")


car1 = Bill("rauður","tezla",250)
car2 = Bill("blár","benz",250)
car3 = Bill("bozolitur","bozo car",250)
car4 = Bill("chrome","volkswagen minibus",250)


bilar = [car1,car2,car3]
bilar.append(car4)
for b in bilar:
    b.afram()
# print(t2.tegund)
# t2.afram()
class Batur:
    def __init__(self, litur, tegund, hradi, fiskibatur):
        self.litur = litur
        self.tegund = tegund
        self.hamarkshradi = hradi
        self.fiskibatur = fisk


        
