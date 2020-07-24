import sys

if __name__ == "__main__":
    conf = open(f"{sys.argv[1]}", 'r')
    data = conf.readlines()    
    
    def clean_newlines(data):
        data_list = []
        for line in data:
            data_list.append(line.strip())
        return data_list

    def remove_whitespace(input):
        return "".join(input.split())

    def convert_list(input):
        conv_d = {input[i] : input[i +1] for i in range(0, len(input),2)}
        return conv_d
        
    try:
        replacement_pos = {'on','true', 'yes'}
        replacement_neg = {'off', 'no', 'false'}
        list_corrected = []
        removed_new_lines = clean_newlines(data)

        for line in removed_new_lines:
            if not line.startswith('#'):
                splitline = line.split('=')
                for value in splitline:
                    no_whitespace = remove_whitespace(value)
                    try: 
                        no_whitespace = int(no_whitespace)
                    except:
                        pass
                    if no_whitespace in replacement_pos:
                        no_whitespace = True
                    if no_whitespace in replacement_neg:
                        no_whitespace = False

                    list_corrected.append(no_whitespace)
                    
        ans=(convert_list(list_corrected))
        print(ans)
        print(ans['host'])
        print(ans['user'])
        print(ans['debug_mode'])

    finally:
        conf.close()


## This will run any config file. To run: "python3 main.py [configFile]"
