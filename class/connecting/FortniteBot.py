class FortniteBot:

    max_health = 100

    def __int__(self, bot_name, start_position):#constructor
        self.anme = bot_name
        self.health = 100

    def take_damage(self, amount): #method
        self.health -= amount