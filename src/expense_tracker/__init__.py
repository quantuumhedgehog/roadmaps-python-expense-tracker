# __init__.py  (Empty or package-level code)
"""
Tracker CLI - A Command Line Expenses Tracker Tool.

This package provides a command-line interface for managing expenses.

Main Features:
    - Add expenses with description and amount
    - Update an expense
    - Delete an expense
    - View all expenses
    - View summary of all expenses
    - View summary of expenses for a specific month (of current year)

For command-line usage, see README.md
"""

# __version__ = "0.1.0"
__author__ = "@quantuumhedgehog"
__email__ = "lutso.mykhailo@gmail.com"

from .expenses import get_parser, parse_arguments
__all__ = ["get_parser", "parse_arguments"]
