from pets_world import __version__
import pytest

from pets_world.pets_classes import Pet, Cat, Dog

def test_version():
    assert __version__ == '0.1.0'
    
def test_pets_counter(data):
    assert Pet.get_pets_count() == 4

def test_cat_has_hair(data):
    assert data[0].has_hair == True
    assert data[1].has_hair == False

def test_dog_age(data):
    assert data[2].age == 12
    assert data[3].age == 17

@pytest.fixture
def data():
    cat1 = Cat('Cat1', 5, True)
    cat2 = Cat('Cat2', 6, False)
    dog1 = Dog('Dog1', 12)
    dog2 = Dog('Dog2', 17)
    return [cat1, cat2, dog1, dog2]