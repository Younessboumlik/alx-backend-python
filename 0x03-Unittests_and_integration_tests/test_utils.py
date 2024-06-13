#!/usr/bin/env python3
""" This is a unittest for the function access_nested_map(nested_map: Mapping, path: Sequence) -> Any """
import unittest
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Tests the access_nested_map function """
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        Test the access_nested_map method.
        Args:
            nested_map (Mapping): A dictionary that may have nested dictionaries
            path (Sequence): Keys to get to the required value in the nested dictionary
            expected (Any): The expected value at the end of the path
        """
        answer = access_nested_map(nested_map, path)
        self.assertEqual(answer, expected)

