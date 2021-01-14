from utils import plot_all, calculate_ber_by_mer
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mer', help='MER value in dB', type=float)
    parser.add_argument('-o, --qam-order', help='QAM order (m-value)',type=int, dest='qam_order')
    parser.add_argument('action', help='Action to execute: calc_ber lub plot_all')

    args = parser.parse_args()

    if args.action == 'calc_ber':
        if not (args.mer or args.qam_order):
            raise Exception('No argument for mer lub qam-order')

        if not args.qam_order in [4,16,64,128]:
            raise Exception('qam-order must be a power of 2')
        
        ber, error = calculate_ber_by_mer(args.mer, args.qam_order)
        output = {'mer': args.mer, 'ber': ber, 'error': error}
        print(output)

    if args.action == 'plot_all':
        plot_all()


