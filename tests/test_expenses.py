# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pytest",
#     "expense_tracker",
# ]
#
# [tool.uv.sources]
# expense_tracker = { path = "../" }
# ///

import expense_tracker

def test_hello_default(capfd):
    expense_tracker.hello()
    captured = capfd.readouterr()
    assert captured.out == "Hello, world!\n"


def test_hello_with_name(capfd):
    expense_tracker.hello("Mykhailo")
    captured = capfd.readouterr()
    assert captured.out == "Hello, Mykhailo!\n"
