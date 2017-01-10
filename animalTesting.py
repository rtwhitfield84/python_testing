import unittest
from animals import *

class TestAnimal(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.animal = Animal("bear")
		self.dog = Dog("roger")


	def test_AnimalHasCorrectNameProperty(self):
		self.assertEqual("bear", self.animal.get_name())

	def test_SpeciesHasCorrectPropertyValue(self):
		self.animal.set_species("ErroneusMaximus")
		self.assertEqual("ErroneusMaximus",self.animal.get_species())

	def test_AnimalObjectHasCorrectWalkSpeed(self):
		self.animal.set_legs(4)
		self.animal.walk()
		self.assertEqual(self.animal.speed, 0.1 * self.animal.legs)

	def test_DogObjectHasCorrectWalkSpeed(self):
		self.dog.set_legs(4)
		self.dog.walk()
		self.assertEqual(self.dog.speed, 0.2 * self.dog.legs)

	def test_AnimalObjectIsInstanceOfAnimal(self):
		self.assertIsInstance(self.animal, Animal)

	def test_DogObjectIsInstanceOfDog(self):
		self.assertIsInstance(self.dog, Dog)


if __name__ == '__main__':
	unittest.main()
