#### To Count the Kmers From a DNA Sequence in a FASTA File ####

from compiler.ast import flatten
import sys

def percentage_frequency(x, k, sequence): #the frequency from the dictionary, the k value, the sequence
    length = float(len(sequence))
    multiply = x * k 
    fraction = multiply / length
    percent = fraction * 100
    return percent

def count_kmers(filename, k):
    with open(filename) as TEXT:
        content = TEXT.readlines()[1:]
        sequence = "".join(content).replace("\r","").replace("\n","").replace("N","")
        TEXT.close()
        #empty dictionary
        counts = {}
        #calculate how many kmers of length k that there are:
        num_kmers = len(sequence) - k + 1
        for i in range(num_kmers):
            #slice the string to get the kmer:
            kmer = sequence[i:i+k]
            #add the kmer to the dictionary if its not there:
            if kmer not in counts:
                counts[kmer] = 0 
            #increment the count for this kmer
            counts[kmer] += 1
        #To get percentage frequency of the kmers in the sequence:
        frequency = counts.values()
        percent = [percentage_frequency(i, k, sequence) for i in frequency]
        
        ###To Create a Data Frame of the Results###
        #To extract all the informtion from the dictionary:
        kmer_vals = []
        for kmer, frequency in counts.iteritems():
            pattern = [kmer, frequency]
            kmer_vals.append(pattern)
        #To create a tuple of all the information from the dictionary plus the percentage frequency of the kmers:
        info_tuple = zip(kmer_vals, percent)
        #To flatten the list:
        info_list = flatten(info_tuple)
        #To create a list of list:
        i = 0
        info_list_of_list = []
        while i < len(info_list):
            info_list_of_list.append(info_list[i:i+3])
            i+=3
        #To comvert to a string:
        string_info =  repr(info_list_of_list)
        #To edit the string:
        info_format = string_info.replace("],","\n").replace("]","").replace("['","").replace("["," ").replace("'","").replace(",","\t")
        #To add the titles:
        info_format = ("kmer\tfrequency\tpercent\n" + info_format)
        info_format = ("\n%s\n" % (sys.argv[1]) + info_format)
        print info_format
    with open("kmer_freq.txt","w") as OUTPUT:
        for x in info_format:
            OUTPUT.write(x)
    return info_format

#want to be able to create an output file and attach each run of the function to that file
#also format in the file with a new line so which displays the name of the genome under each kmer and frequency and percent heading perhaps using 3 tabs per genome name.
count_kmers(sys.argv[1], int(sys.argv[2]))

