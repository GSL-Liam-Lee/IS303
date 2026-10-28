from class.connecting.FortniteBot import FortniteBot

bot1 = FortniteBot("Chat",89)
bot2 = FortniteBot("R2-D2",22)
bot3 = FortniteBot("spencer_hilton", 111111)

bot1.take_damage(5)
bot2.take_damage(20)

print(bot1.health)
print(bot2.health)


bot3.__init__