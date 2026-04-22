import src.classes as c

# Init Classes

class_barbarian = c.CharacterClass("Barbarian","Fights their way through with brute force. Can't use magic.",200,0,15,5)
class_mage = c.CharacterClass("Mage","Uses various spells to blast enemies away.",110,15,4,0)
class_knight = c.CharacterClass("Knight","A skilled fighter who uses both magic and weapons, the most balanced.",150,7,10,3)

classes = {
      class_barbarian.name: class_barbarian,
      class_mage.name: class_mage,
      class_knight.name: class_knight
}