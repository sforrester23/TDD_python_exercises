from exercise_101 import *

def test_hello_human1():
    assert hello_human('Jefferson') == 'Hello Jefferson, you are a human'

def test_hello_human2():
    assert hello_human('Joana') == 'Hello Joana, you are a human'

def test_area_square():
    assert area_square(10) == 100

def test_area_square1():
    assert area_square(13) == 169

def test_area_triangle():
    assert area_triangle(10, 10) == 50

def test_area_triangle2():
    assert area_triangle(10, 13) == 65

def test_area_circle():
    assert round(area_circle(10), 3) == 314.159

def test_area_circle2():
    assert round(area_circle("9"), 3) == 254.469

def test_volume_sphere():
    assert round(volume_sphere(10), 3) == 4188.790

def test_volume_sphere2():
    assert round(volume_sphere("9"), 3) == 3053.628


