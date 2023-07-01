from typing import Any
from tabulate import tabulate


class Otable:
    def __init__(self, objects):
        # Ensure that all objects are of the same type
        first_type = type(objects[0])
        for obj in objects:
            assert isinstance(obj, first_type), "All objects must be of the same type"

        # Get the properties (i.e., attributes) of the objects
        self.columns = [attr for attr in dir(objects[0]) if not callable(getattr(objects[0], attr)) and not attr.startswith("__")]
        print(self.columns)
        
    
        # Create the table (a list of lists)
        self.table = []
        for obj in objects:
            row = []
            for column in self.columns:
                if isinstance(getattr(obj, column), (list, tuple)):  # Check if attribute is a list or tuple
                    flattened_value = ", ".join(str(item) for item in getattr(obj, column))
                    row.append(flattened_value)
                elif hasattr(getattr(obj, column), "__dict__"):  # Check if attribute is an object with its own attributes
                    attributes = getattr(obj, column).__dict__
                    flattened_value = ", ".join(f"{attr}: {value}" for attr, value in attributes.items())
                    row.append(flattened_value)
                else:
                    row.append(getattr(obj, column))
            self.table.append(row)



        # Initialize the list of hidden columns
        self.hidden_columns = []


    def update_cell(self, column, row_index, new_value):
        # Accept either a column index or a column name
        if isinstance(column, int):
            column = self.columns[column]

        # Get the column index
        column_index = self.columns.index(column)

        # Update the value of the cell
        self.table[row_index][column_index] = new_value


    def to_markdown(self):
        # Get a list of indices corresponding to visible columns
        visible_column_indices = [i for i, col in enumerate(self.columns) if col not in self.hidden_columns]

        # Exclude the hidden columns
        table = [[row[i] for i in visible_column_indices] for row in self.table]
        headers = [self.columns[i] for i in visible_column_indices]

        return tabulate(table, headers=headers, tablefmt="pipe")

    def to_html(self):
        # Get a list of indices corresponding to visible columns
        visible_column_indices = [i for i, col in enumerate(self.columns) if col not in self.hidden_columns]

        # Exclude the hidden columns
        table = [[row[i] for i in visible_column_indices] for row in self.table]
        headers = [self.columns[i] for i in visible_column_indices]

        return tabulate(table, headers=headers, tablefmt="html")

    def get_table(self):
        table = []
        visible_column_indices = [i for i, col in enumerate(self.columns) if col not in self.hidden_columns]
        for row in self.table:
            visible_row = [row[i] for i in visible_column_indices]
            table.append(visible_row)
        return table
    
    def get_headers(self):
        headers = [col for col in self.columns if col not in self.hidden_columns]
        return headers

    def add_column(self, column_name, column_values, location):
        # Ensure that the number of values matches the number of rows in the table
        assert len(column_values) == len(self.table), "The number of values must match the number of rows in the table"

        # Insert the new column name at the specified location
        self.columns.insert(location, column_name)

        # Add the values to the corresponding rows
        for i in range(len(self.table)):
            self.table[i].insert(location, column_values[i])

    def add_column_with_default_value(self, column_name, default_value, location):
        # Create a list of default values with the same length as the number of rows in the table
        default_values = [default_value] * len(self.table)

        # Use the add_column function to add the new column
        self.add_column(column_name, default_values, location)

    def hide_column(self, column):
        # Accept either a column index or a column name
        if isinstance(column, int):
            column = self.columns[column]

        # Add the column to the list of hidden columns
        if column not in self.hidden_columns:
            self.hidden_columns.append(column)
            

    def show_column(self, column):
        # Accept either a column index or a column name
        if isinstance(column, int):
            column = self.columns[column]

        # Remove the column from the list of hidden columns if it's present
        if column in self.hidden_columns:
            self.hidden_columns.remove(column)


    def move_column(self, column, direction):
        # Get the current index of the column
        if isinstance(column, str):
            index = self.columns.index(column)
        else:
            index = column

        # Determine the new index based on the direction
        if direction == "left" and index > 0:
            new_index = index - 1
        elif direction == "right" and index < len(self.columns) - 1:
            new_index = index + 1
        else:
            return  # Do nothing if moving the column is not possible

        # Remove the column from its current position and insert it at the new position
        self.columns.remove(column)
        self.columns.insert(new_index, column)

        # Do the same for the rows
        for row in self.table:
            row.insert(new_index, row.pop(index))