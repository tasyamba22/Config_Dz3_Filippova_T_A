import unittest
from config_to_yaml import generate_config, compute_expression

class TestConfigGenerator(unittest.TestCase):
    def test_simple_string(self):
        yaml_input = {"key" : "value"}
        expected = "key = \"value\"\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_simple_number(self):
        yaml_input = {"number": 42}
        expected = "number = 42\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_dictionary(self):
        yaml_input = {"settings": {"color": "blue", "size": 10}}
        expected = "settings = '[ color : \"blue\"; size : 10; ]\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_list(self):
        yaml_input = {"values": [1, 2, 3]}
        expected = "values = '( 1 2 3 )\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_comment(self):
        yaml_input = {"comment": "Это комментарий"}
        expected = "*> Это комментарий\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_multiline_comment(self):
        yaml_input = {"multicomment": "Это\nмногострочный\nкомментарий"}
        expected = "--[[\nЭто\nмногострочный\nкомментарий\n]]\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_constant_expression(self):
        yaml_input = {"result": "^{+ 2 3}"}
        expected = "result = 5.0\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_nested_structures(self):
        yaml_input = {"settings": {"window": {"width": 800, "height": 600}, "theme": "dark"}}
        expected = "settings = '[ window : '[ width : 800; height : 600; ]; theme : \"dark\"; ]\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_invalid_key_name(self):
        yaml_input = {"Invalid-Key": "value"}
        with self.assertRaises(ValueError) as context:
            generate_config(yaml_input)
        self.assertIn("Некорректное имя ключа", str(context.exception))

    def test_valid_key_name(self):
        yaml_input = {"valid_key123": "value"}
        expected = "valid_key123 = \"value\"\n"
        self.assertEqual(generate_config(yaml_input), expected)

    def test_compute_expression(self):
        self.assertEqual(compute_expression("+ 2 3"), "5.0")
        self.assertEqual(compute_expression("- 10 3"), "7.0")
        self.assertEqual(compute_expression("* 2 5"), "10.0")
        self.assertEqual(compute_expression("/ 10 2"), "5.0")
        self.assertEqual(compute_expression("concat hello world"), "helloworld")

if __name__ == "__main__":
    unittest.main()

