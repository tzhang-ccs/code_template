import argparse


def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)


parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--name', '-n', help='name')
parser.add_argument('--year', '-y', help='year', default=2017, type=int)
parser.add_argument('--body', '-b', help='body', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        test_for_sys(args.year, args.name, args.body)
    except Exception as e:
        print(e)
