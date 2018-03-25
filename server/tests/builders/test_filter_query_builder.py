""" Tests for filter query builder """
import unittest
from werkzeug.datastructures import ImmutableMultiDict
from app.builders.filter_query_builder import FilterQueryBuilder

class FilterQueryBuilderTestCase(unittest.TestCase):

    def test_build_with_null_arguments_return_empty_filters(self):
        # arrange
        expected_filters_length = 0
        builder = FilterQueryBuilder(None)

        # act
        result = builder.build()

        # assert
        self.assertEqual(expected_filters_length, len(result.filters))

    def test_build_with_one_filter_argument_almost_like_return_empty_filters(self):
        # arrange
        expected_filters_length = 0
        args = ImmutableMultiDict(
            [
                ("filtering[date]", 1521417600)
            ])

        builder = FilterQueryBuilder(args)

        # act
        result = builder.build()

        # assert
        self.assertEqual(expected_filters_length, len(result.filters))

    def test_build_with_one_filter_argument_incorrect_return_empty_filters(self):
        # arrange
        expected_filters_length = 0
        args = ImmutableMultiDict(
            [
                ("abcde[date]", 1521417600)
            ])

        builder = FilterQueryBuilder(args)

        # act
        result = builder.build()

        # assert
        self.assertEqual(expected_filters_length, len(result.filters))

    def test_build_with_one_filter_argument_but_empty_attr_return_empty_filters(self):
        # arrange
        expected_filters_length = 0
        args = ImmutableMultiDict(
            [
                ("filter[]", 1521417600)
            ])

        builder = FilterQueryBuilder(args)

        # act
        result = builder.build()

        # assert
        self.assertEqual(expected_filters_length, len(result.filters))

    def test_build_with_one_filter_argument_correct_return_correct_filters(self):
        # arrange
        expected_filters_length = 1
        args = ImmutableMultiDict(
            [
                ("filter[date]", 1521417600)
            ])

        builder = FilterQueryBuilder(args)

        # act
        result = builder.build()

        # assert
        self.assertEqual(expected_filters_length, len(result.filters))
        self.assertIsNotNone(result.filters.get("date"))
        self.assertEqual(result.filters.get("date"), 1521417600)

    def test_build_with_one_filter_argument_with_two_attrs_return_the_first(self):
        # arrange
        expected_filters_length = 1
        args = ImmutableMultiDict(
            [
                ("filter[date][test]", 1521417600)
            ])

        builder = FilterQueryBuilder(args)

        # act
        result = builder.build()

        # assert
        self.assertEqual(expected_filters_length, len(result.filters))
        self.assertIsNotNone(result.filters.get("date"))
        self.assertEqual(result.filters.get("date"), 1521417600)
        self.assertIsNone(result.filters.get("test"))

    def test_build_with_two_filter_argument_correct_return_correct_filters(self):
        # arrange
        expected_filters_length = 2
        args = ImmutableMultiDict(
            [
                ("filter[date]", 1521417600),
                ("filter[user_id]", 10)
            ])

        builder = FilterQueryBuilder(args)

        # act
        result = builder.build()

        # assert
        self.assertEqual(expected_filters_length, len(result.filters))
        self.assertIsNotNone(result.filters.get("date"))
        self.assertEqual(result.filters.get("date"), 1521417600)
        self.assertIsNotNone(result.filters.get("user_id"))
        self.assertEqual(result.filters.get("user_id"), 10)
