import os
import sys

path = os.getcwd()
parent_directory = os.path.abspath(os.path.join(path, os.pardir))
sys.path.append(parent_directory)

import unittest

import pandas as pd

from community_website.modules.utils import translate_excel


class TestTranslateExcel(unittest.TestCase):
    def test_nonexistent_excel_file(self):
        excel_file_path = "tests/nonexistent_file.xlsx"
        to_language = "en"
        result = translate_excel(excel_file_path, to_language)
        self.assertIsNone(
            result, "Expected None for a non-existent Excel file"
        )

    def test_empty_excel_file(self):
        excel_file_path = "tests/test_excels/empty_file.xlsx"
        to_language = "en"
        result = translate_excel(excel_file_path, to_language)
        self.assertIsNone(result, "Expected None for an empty Excel file")

    def test_translation_without_export(self):
        expected_df = pd.DataFrame(["Turkish"], columns=["table"])
        excel_file_path = "tests/test_excels/sample.xlsx"
        to_language = "en"
        result = translate_excel(excel_file_path, to_language)
        print(result)
        self.assertIsInstance(result, pd.DataFrame, "Expected a DataFrame")
        self.assertFalse(result.empty, "Expected non-empty DataFrame")
        self.assertEqual(
            result.columns, expected_df.columns, "Columns translated correctly"
        )
        self.assertEqual(
            result.values, expected_df.values, "Rows translated correctly"
        )

    def test_translation_with_export(self):
        excel_file_path = "tests/test_excels/sample.xlsx"
        to_language = "en"
        result = translate_excel(excel_file_path, to_language, export=True)
        self.assertIsNone(result, "Expected None when exporting")
        self.assertTrue(
            os.path.isfile("tests/test_excels/sample_translated.xlsx"),
            "File created successfully",
        )


if __name__ == "__main__":
    unittest.main()
