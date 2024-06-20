import sys

def print_header(header_title):
    # Define the characters for the box
    top_bottom_border = '+' + '-' * (len(header_title) + 10) + '+'
    middle_row = '|' + ' '* 5 + header_title +  ' '* 5  + '|'

    # Print the box
    print(top_bottom_border)
    print(middle_row)
    print(top_bottom_border)



def print_complex_header(title, columns):
    # Define the top and bottom border based on the length of the longest column name
    max_col_length = max(len(col) for col in columns)
    table_width = max_col_length + 4
    top_bottom_border = '+' + '-' * table_width + '+'

    # Print the title
    title_row = '| ' + title.center(table_width - 2) + ' |'
    print(top_bottom_border)
    print(title_row)
    print(top_bottom_border)

    # Print each column name within the table
    for col in columns:
        col_row = '| ' + col.ljust(table_width - 2) + ' |'
        print(col_row)

    print(top_bottom_border)


