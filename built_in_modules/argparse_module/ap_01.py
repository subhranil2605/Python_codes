import argparse

'''
parser = argparse.ArgumentParser(description="Calculate volume of a cylinder")
parser.add_argument('-r', '--radius', type=int, help='Radius of the cylinder')
parser.add_argument('-H', '--height', type=int, help='Height of the cylinder')
args = parser.parse_args()


def cylinder_volume(radius: int, height: int) -> float: 
    return np.pi * np.power(radius, 2) * height


if __name__ == "__main__":
    print(cylinder_volume(args.radius, args.height))
'''


parser = argparse.ArgumentParser(prog='ap_01',
                                 usage='%(prog)s [options] -f -l -m',
                                 description="Get the full name of yours",
                                 epilog="End of the help.")

parser.add_argument('-f', '--first_name', type=str, required=True , help='First Name')
parser.add_argument('-m', '--middle_name', type=str, metavar='', help='Middle Name')
parser.add_argument('-l', '--last_name', type=str, required=True, help='Last Name')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')

args = parser.parse_args()


def full_name(first, last, middle=None):
    return f"{first.title()} {middle.title()} {last.title()}" if middle else f"{first.title()} {last.title()}"


if __name__ == "__main__":
    fn = full_name((f := args.first_name), (l := args.last_name), (m := args.middle_name))
    if args.quiet:
        print(fn)
    elif args.verbose:
        print(f"Full name of {f}-{m or ''}-{l} is {fn}")
    else:
        print(fn)
