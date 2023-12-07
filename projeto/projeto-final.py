import argparse
import csv_to_xml
import csv_to_yaml
import csv_to_json

parser = argparse.ArgumentParser("Projeto Final: Gerador de notas fiscais")
parser.add_argument("--formato", dest='formato', help="O formato desejado da nota fiscal. Opções disponíveis: XML, JSON e YAML.", type=str, choices=['xml', 'json', 'yaml'])
args = parser.parse_args()

if args.formato == 'xml':
    csv_to_xml.converterParaXml()
elif args.formato == 'json':
    csv_to_json.converterParaJson()
else:
    csv_to_yaml.converterParaYAML()
