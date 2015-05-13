def state_distribution():
    infile = open('sample_data.txt', 'r')
    line = infile.read()
    name_list = line.split()
    print len(name_list)
    
    state_numbers = {'AL':0,'AK':0,'AZ':0}
    print state_numbers


    counter = 0
    another_dict = {}
    for keys in state_numbers.keys():
        if state_numbers[keys] == 'AL':
            counter +=1
            another_dict[keys] = 'AL_' + str(counter)

    print(another_dict)
