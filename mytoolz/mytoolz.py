# mytoolz
# version 0.1
# Last update: 2017-11-01 by Myrousz
#
# Various useful functions for working with files, CSVs and tables.


import io, os, json, csv
import pyaml as yaml
import datetime
import unicodedata

# Methods in version 0.1

def hello():
    return "Hello, mytoolz!!"


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


def reformat_date(datestr, fromformat, toformat):
    dt = datetime.datetime.strptime(datestr, fromformat)
    dt2 = datetime.datetime.strftime(dt, toformat)
    return dt2


def load_json_data(path):
    with open(path, "r") as infile:
        data = json.load(infile)
        return data


def save_json_data(data, path):
    with open(path, 'w') as handle:
        json.dump(data, handle, indent=4)


# Write YAML file
def save_yaml_data(data, path):
    with io.open(path, 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)


# Read YAML file
def load_yaml_data(path):
    with open(path, 'r') as stream:
        data_loaded = yaml.load(stream)
        return data_loaded


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]


def load_file_as_lines(path):
    with open(path, "r") as f:
        lines = [line.rstrip('\n') for line in f]
        return lines


def write_lines_as_file(data, path):
    dd = "\n".join(data)
    with open(path, "w") as outfile:
        outfile.write(dd)


def write_array_as_csv(data, path, delimiter=",", quotechar='"'):
    with open(path, "wb") as f:
        writer = csv.writer(f, delimiter=delimiter, quotechar=quotechar)
        writer.writerows(data)


def load_csv_as_array(path, delimiter=",", quotechar='"'):
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        rows = []
        for row in reader:
            rows.append(row)
        return rows


def load_csv_as_dict_array(input_file, delimiter=","):
    with open(input_file) as f:
        a = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True, delimiter=delimiter)]
        return a


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def copy_as_new(dictionary, fields):
    """
    Copies the dictionary to a new one. Copies only the fields specified.
    :param dictionary:
    :param fields:
    :return:
    """
    out = {}
    for f in fields:
        out[f] = dictionary[f]
    return out

# Methods in version 0.2


