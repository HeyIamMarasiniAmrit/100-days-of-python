class vault:
    def __init__(self, galleons=0, sickles=0, knuts=0 ):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


def __str__(self):
    return f"{self.galleons} Galleons, {self.sickles} sickles, {self.knuts} knuts"


potter = vault(100, 50, 25)
print(potter)


weasley =vault(25, 50, 100)
print(weasley)
