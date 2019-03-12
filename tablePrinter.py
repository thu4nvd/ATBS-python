# tableData = [['apples', 'oranges', 'cherries', 'banana'],
# ['Alice', 'Bob', 'Carol', 'David'],
# ['dogs', 'cats', 'moose', 'goose']]
# Your printTable() function would print the following:
# apples Alice dogs
# oranges
# Bob cats
# cherries Carol moose
# banana David goose

def tprint(tableData):
    # Tim so lon nhat max_row cua cac list con
    max_row = len(max(tableData, key=lambda row: len(row)))
    # print(max_row)
        
    # Tinh max_len cua moi row
    max_len = [ int(len(max(row, key=lambda i: len(i) ))) for row in tableData]
    # print(max_len)

    # In ra tung hang, hang thu i la phan tu thu i cua cac list con
    for i in range(max_row):
        for row in range(len(tableData)):
            if i < len(tableData[row]):
                # print(str(row[i].rjust(max_len[row] + 2)), end=" ")
                str = tableData[row][i].rjust(max_len[row] + 2)
                print(str, end=" ")
            else:
                print(" "*(max_len[row] + 2), end=" ")
        print("\n")
    