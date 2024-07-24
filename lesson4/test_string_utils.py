    # lesson_4/test_string_utils.py
import pytest
from string_utils import StringUtils

su = StringUtils()

def test_capitilize():
        assert su.capitilize("skypro") == "Skypro"
        assert su.capitilize("SkyPro") == "Skypro"
        assert su.capitilize("123skypro") == "123skypro"
print ("test")
def test_trim():
        assert su.trim("   skypro") == "skypro"
        assert su.trim("skypro") == "skypro"
        assert su.trim("   skypro   ") == "skypro   "

def test_to_list():
        assert su.to_list("a,b,c,d") == ["a", "b", "c", "d"]
        assert su.to_list("1:2:3", ":") == ["1", "2", "3"]
        assert su.to_list("") == []
        assert su.to_list("   ", " ") == ["", "", "", ""]

def test_contains():
        assert su.contains("SkyPro", "S") is True
        assert su.contains("SkyPro", "U") is False
        assert su.contains("SkyPro", "k") is True
        assert su.contains("", "S") is False

def test_delete_symbol():
        assert su.delete_symbol("SkyPro", "k") == "SyPro"
        assert su.delete_symbol("SkyPro", "Pro") == "Sky"
        assert su.delete_symbol("SkyPro", " ") == "SkyPro"
        assert su.delete_symbol("", "S") == ""

def test_starts_with():
        assert su.starts_with("SkyPro", "S") is True
        assert su.starts_with("SkyPro", "P") is False
        assert su.starts_with("", "S") is False

def test_end_with():
        assert su.end_with("SkyPro", "o") is True
        assert su.end_with("SkyPro", "y") is False
        assert su.end_with("", "o") is False

def test_is_empty():
        assert su.is_empty("") is True
        assert su.is_empty(" ") is True
        assert su.is_empty("SkyPro") is False

def test_list_to_string():
        assert su.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert su.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert su.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
        assert su.list_to_string([]) == ""
