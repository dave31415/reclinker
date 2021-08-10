import os

data_sources_dir = os.path.realpath(os.path.dirname(__file__))
resource_data_dir = os.path.realpath(os.path.join(data_sources_dir, 'resource_data'))
nick_name_data_dir = os.path.realpath(os.path.join(resource_data_dir, 'nick_names'))

_file_names = {
    'nick_names_1': f'{nick_name_data_dir}/nicknames_1.txt',
    'us_census_nicknames': f'{nick_name_data_dir}/us_census_nicknames.txt',
    'nicknames_domin': f'{nick_name_data_dir}/domin.txt',
    'nicknames_variations': f'{nick_name_data_dir}/variations.txt',
}


def get_file_names():
    return _file_names.copy()
