#ETHAN SPENCER CSE111

import pytest
from caloriefinal import es_convert_height_to_cm, es_convert_weight_to_kg

def test_convert_height_to_cm():
    assert es_convert_height_to_cm(60, 'United States') == 152.4
    assert es_convert_height_to_cm(170, 'Canada') == 170
    assert es_convert_height_to_cm(170, 'Mexico') == 170
    assert es_convert_height_to_cm(170, 'Germany') == 170

def test_convert_weight_to_kg():
    assert es_convert_weight_to_kg(120, 'United States') == pytest.approx(54.4311, rel=1e-3)
    assert es_convert_weight_to_kg(70, 'Canada') == 70
    assert es_convert_weight_to_kg(70, 'Mexico') == 70
    assert es_convert_weight_to_kg(70, 'Germany') == 70

pytest.main(["-v", "--tb=line", "-rN", __file__])