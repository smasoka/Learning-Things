from unittest import mock, TestCase

from project import something

# Manual start/stop
class TestExamples(TestCase):
    def setUp(self):
        self.patcher = mock.patch('project.something.check_output', return_value=b'foo\nbar\n')
        self.patcher.start()

    def test_print_contents_of_cwd_success(self):
        actual_result = something.print_content_of_cwd()

        expected_directory = b'foo'
        self.assertIn(expected_directory, actual_result)

    def tearDown(self):
        self.patcher.stop()

# # Context Manager
# class TestExamples(TestCase):
#     def test_print_contents_of_cwd_success(self):
#         with mock.patch('project.something.check_output', return_value=b'foo\nbar\n'):
#             actual_result = something.print_content_of_cwd()
#
#         expected_directory = b'foo'
#         self.assertIn(expected_directory, actual_result)
#
# # Decorator Patch
# class TestExamples(TestCase):
#     @mock.patch('project.something.check_output', return_value=b'foo\nbar\n')
#     def test_print_contents_of_cwd_success(self, mock_check_output):
#         actual_result = something.print_content_of_cwd()
#
#         expected_directory = b'foo'
#         self.assertIn(expected_directory, actual_result)
#
# # Original Testing
# class TestExamples(TestCase):
#     def test_print_contents_of_cwd_success(self):
#         # running the actual fucntion
#         actual_result = something.print_content_of_cwd()
#
#         expected_directory = b'tests'
#         self.assertIn(expected_directory, actual_result)
