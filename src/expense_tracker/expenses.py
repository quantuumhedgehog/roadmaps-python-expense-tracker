def get_parser():
    parser = argparse.ArgumentParser(
            description="Exspense Tracker", argument_default=argparse.SUPPRESS
    )
    # Positional argument (required)
    parser.add_argument(
            "command",
            choices=["list", "add", "summary", "update", "delete"],
            help="Tasker command",
    )

    # Conditional arguments
    list_group = parser.add_mutually_exclusive_group(required=False)
    list_group.add_argument("--ascend", action="store_true")
    list_group.add_argument("--descend", action="store_true")

    add_group = parser.add_argument_group("ADD", "Add a new exspense")
    add_group.add_argument(
            "--description", type=str, help="Description of the exspense", required=False
    )
    add_group.add_argument(
            "--amount", type=str, help="Amount of the exspense", required=False
    )

    summary_group = parser.add_argument_group("SUMMARY", "Show summary of exspenses")
    summary_group.add_argument("--year", type=int, help="Year for summary", required=False)
    summary_group.add_argument(
            "--month", type=int, help="Month for summary", required=False
    )

    update_delete_group = parser.add_argument_group("UPDATE", "Update/delete an exspense")
    update_delete_group.add_argument(
            "--id", type=int, help="ID of expense to edit", required=False
    )

    return parser


def parse_arguments(parser: argparse.ArgumentParser, tracker: Tracker):
    args: argparse.Namespace = parser.parse_args()
    match args.command:
        case "list":
            if args.ascend:
                print("ascend")
            elif args.descend:
                print("descend")
            else:
                ticket_print(tracker.exspenses)
        case _:
            sys.exit(1)
    if args.command == "add":
        # Check if required arguments for 'process' mode are present
        if not args.description and not args.amount:
            parser.error("For 'add' command, --desription and --amount are required.")
        print(f"Input: {args.description}, Output: {args.amount}")

    else:
        exit(1)
