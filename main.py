from helper.google import SheetsHelper


def main():
    # Initialize the SheetsHelper object
    helper = SheetsHelper()

    # Read data from the sheet
    sheet_id = '1N241PKX1ljVapIDu15EW_E_Y6q2O7TZmoKODv7X88Rs'
    sheet_range = 'Panel!B5:Z'
    print(f"Reading data from range {sheet_range} of the Spreadsheet {sheet_id}\n")
    data = helper.get_sheet_data(sheet_id, sheet_range)
    print(data)

    new_input = input("Do you want to add a new value as an example? (y/n):")
    if new_input == "y":
        # Append new values to the sheet
        new_values = [
            ['LTC', '89.95'],
        ]
        range_name = sheet_range
        value_input_option = 'USER_ENTERED'
        helper.append_values(sheet_id, range_name, value_input_option, new_values)

    elif new_input == "n":
        print("Okay bye")
        return
    else:
        print("Invalid argument")
        return


if __name__ == '__main__':
    main()
