def read_data(filename):
    with open(filename, "r") as file:
        data = [list(map(float, line.split())) for line in file]
    return(data)
def write_averages(data):
    total_sum=sum(sum(row) for row in data)
    total_count=sum(len(row) for row in data)
    overall_average = total_sum/total_count
    row_averages= [sum(row) / len(row) for row in data]
    with open("averages.txt", "w") as output_file:
        output_file.write(f"Overall Average: {overall_average:.2f}\n")
        for i, avg in enumerate(row_averages, start=1):
            output_file.write(f"Row {i} Average: {avg:.2f}\n")
def write_reversed(data):
    with open("reversed.txt", "w") as rev_file:
        for row in data:
            reversed_row= row[::-1]
            rev_file.write(" ".join(map(str, reversed_row)) + "\n")
def write_flipped(data):
    with open("flipped.txt", "w") as flipped_file:
        for row in reversed(data):
            flipped_file.write(" ".join(map(str, row)) + "\n")
def write_diagonal(data):
    if len(data)==len(data[0]):
        mirrored = [[data[j][i] for j in range(len(data))] for i in range(len(data))]
        with open("diagonal.txt", "w") as diagonal_file:
            for row in mirrored:
                diagonal_file.write(" ".join(map(str,row)) + "\n")
def main():
    filename = input("Enter the name of the data file(including the extension .txt): ")
    data = read_data(filename)
    write_averages(data)
    write_reversed(data)
    write_flipped(data)
    if len(data)==len(data[0]):
        write_diagonal(data)
if __name__=="__main__":
    main()
