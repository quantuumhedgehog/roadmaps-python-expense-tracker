# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "expense_tracker",
# ]
#
# [tool.uv.sources]
# expense_tracker = { path = "." }
# ///
import expense_tracker

def main() -> None:
    expense_tracker.hello("Thing Check")


if __name__ == "__main__":
    main()
