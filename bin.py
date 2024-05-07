import csv
from collections import defaultdict

def bin(gfa_file, output_csv):

    contig_bins = defaultdict(str)
    
    with open(gfa_file, 'r') as file:
        for line in file:
            if line.startswith('S'):
                # Parse the contig name and sequence length
                fields = line.strip().split('\t')
                contig_name = fields[1]
                contig_length = int(fields[2])
                
                # length
                if contig_length < 1000:
                    bin_name = 'Bin 1'
                elif contig_length < 5000:
                    bin_name = 'Bin 2'
                elif contig_length < 10000:
                    bin_name = 'Bin 3'
                else:
                    bin_name = 'Bin 4'
                
                contig_bins[contig_name] = bin_name
    
    # csv file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Contig', 'Bin'])
        for contig, bin_name in contig_bins.items():
            writer.writerow([contig, bin_name])


input_gfa = "binniginput.GFA"
output_csv = "bin.csv"
bin(input_gfa, output_csv)
print(f'Results written to {output_csv}')