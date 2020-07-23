from Personality import Personality
from Normal import Normal
import unittest

class Test(unittest.TestCase):
    def test_personality(self):
        personality = Personality(50, 50, 50)
        Personality.type_name = "Happy-Go-Lucky"
        Personality.pop_percent = 0.1
        print(personality.type_name)
        fear = personality._getFear_()
        print(fear)
        print(personality)
        personality._setFear_(30)
        fear2 = personality._getFear_()
        print(fear2)
        print(personality._getFear_())
        personality._setMorale_(100)
        print(personality._getMorale_())


    def test_normal(self):
        normal = Normal(40, 40, 40)
        #Personality.type_name = "Yoda"
        #Personality.pop_percent = 0.9
        print(normal)
        print(normal._getTrust_())
        normal._setMorale_(60)
        print(normal._getMorale_())


if __name__ == '__main__':
    unittest.main()
