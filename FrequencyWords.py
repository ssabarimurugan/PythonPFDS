import os
import re

def FindFrequency(path):
    freq = {}   
    file = open(path)
    data = file.read()
    data = data.replace('\n', ' ')
    data = re.sub(r'[^a-zA-Z0-9\s\’]+', '', data)
    data_list = data.split(' ')

    for word in data_list:
        if freq.get(word) is not None:
            freq[word] += 1
        else:
            freq[word] = 1

    for x in freq :
        print('{} is occurs {} times'.format(x, freq[x]))

    top3 = sorted(freq, key=freq.get, reverse=True)[:3]

    print("Top 3 frequent words: ")
    print(top3)

def main():
    while True:
        rel_path = input("Enter a valid input file path (relative):")
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, rel_path)
        if os.path.isfile(abs_file_path) :
            break
    
    FindFrequency(abs_file_path)
        
if __name__ == "__main__":  
    main()
    

