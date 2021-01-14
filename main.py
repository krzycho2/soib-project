from utils import plot_all, calculate_ber_by_mer
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mer', help='MER value in dB', type=float)
    parser.add_argument('-o, --qam_order', help='QAM order (m-value)',type=int)
    parser.add_argument('action', help='Akcja do wykonania: calc_ber lub plot_all')

    args = parser.parse_args()
    print(args)

    if args.action == 'calc_ber':
        if not (args.mer or args.qam_order:
            print( 'Brak argumentu mer lub qam-order')
            return
        
        ber, error = calculate_ber_by_mer(args.mer, args.qam_order)
        output = {'mer': args.mer, 'ber': ber, 'error': error}
        print(output)

    if args.action == 'plot_all':
        plot_all()


