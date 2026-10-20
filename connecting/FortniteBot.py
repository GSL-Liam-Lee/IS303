class FortniteBot:

    def __int__(self, bot_name):
        self.anme = bot_name
        self.health = 100

    def take_damage(self, amount): #method
        self.health -= amount