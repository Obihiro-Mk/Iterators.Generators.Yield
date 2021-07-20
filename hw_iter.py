import json


class CountriesIterate:
    wiki_link = 'https://en.wikipedia.org/wiki/'

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        with open(input_file, 'r', encoding='utf-8') as f:
            self.countries_info = json.load(f)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.countries_info:
            raise StopIteration
        country_info = self.countries_info.pop(0)
        country = country_info['name']['common']
        country_link = self.wiki_link + country.replace(' ', '_')
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write(f'{country} - {country_link}\n')
        return f'{country} - {country_link}\n'


iter_countries = CountriesIterate('countries.json', 'country_link.txt')
for i in iter_countries:
    print(i)

