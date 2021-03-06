try:
    import argparse
except ImportError:
    argparse = None
import sys
    
import las


def main():
    if argparse:
        args = get_parser().parse_args(sys.argv[1:])
        lasfn = args.las_filename
        xlsfn = args.xls_filename
    else:
        if len(sys.argv >= 3):
            lasfn = sys.argv[1]
            xlsfn = sys.argv[2]
        else:
            print('Convert LAS file to Excel.\n\n'
                  'Usage:\n\n'
                  'las2excel.py example.las output.xls')
            sys.exit(1)
        
    l = las.Las(lasfn)
    converter = core.ExcelConverter(l)
    converter.write_excel(xlsfn)

    
def get_parser():
    parser = argparse.ArgumentParser('Convert LAS file to Excel')
    parser.add_argument('las_filename')
    parser.add_argument('xls_filename')
    return parser
    
    
if __name__ == '__main__':
    main()