import numpy as np
from scipy.integrate import dblquad, nquad
import matplotlib.pyplot as plt

MIN_MAX_COORDS = [-1,1]

def calculate_ber_by_mer(mer, qam_order, correct_point=[0.75, 0.75]):
    sigma = calculate_sigma(mer, qam_order)
    return calculate_ber_integral(sigma, qam_order, correct_point)

def calculate_sigma(mer, qam_order):
    qam_power = get_qam_power(qam_order)
    return qam_power / 10 ** (mer/10)

def calculate_ber_integral(sigma, qam_order, correct_point):
    mx,my = correct_point
    x0,x1,y0,y1 = get_boundary(correct_point,qam_order)
    opts = {'epsabs': 0, 'epsrel': 1e-13, 'limit': 100}
    inner_area = nquad(lambda x,y: gauss2d_pdf(x,y,mx,my,sigma), [[x0,x1], [y0,y1]], opts=opts)
    error = inner_area[1]
    ber = 1- inner_area[0]
    # print(f'Error: {error}')
    # if error > ber:
    #     print('Uwaga: Błąd większy niż BER')

    return ber, error

def plot_all():
    mers = np.linspace(1,20)
    bers_for_qam = []
    qam_orders = [4,16,64]
    for qam_order in qam_orders:
        bers = []
        for mer in mers:
            ber = calculate_ber_by_mer(mer, qam_order)[0]
            bers.append(ber)
        bers_for_qam.append(bers)

    epsilon_line = 1e-13 *np.ones(len(mers))

    plt.plot(mers, bers_for_qam[0], 'yo', label='QAM-4')
    plt.plot(mers, bers_for_qam[1], 'bo', label='QAM-16')
    plt.plot(mers, bers_for_qam[2], 'go', label='QAM-64')
    plt.plot(mers, epsilon_line, 'r--', label='Minimalna dokładność (błąd bezwzględny)')
    plt.xlabel('MER [dB]')
    plt.ylabel('BER')
    plt.yscale('log')
    plt.legend(loc='upper right')
    plt.show()

def gauss2d_pdf(x, y, mx, my, sigma):
    return np.exp(- ((x-mx)**2 + (y-my)**2) / (2*sigma**2)) / (2 * np.pi * sigma**2)

def get_boundary(point, qam_order):
    N = int(np.sqrt(qam_order)) # 16 -> 4
    square_len_per_bit = (MIN_MAX_COORDS[1] - MIN_MAX_COORDS[0]) / N
    indent = square_len_per_bit / 2

    return point[0]-indent, point[0]+indent, point[1]-indent, point[1]+indent

def get_qam_power(qam_order):
    points = get_qam_points(qam_order)
    return np.sum(np.array(points)**2) / len(points)

def get_qam_points(qam_order):
    if not qam_order in [4,16,64,128]:
        print('qam_order is not a power of 2!')
        return -1
    N = int(np.sqrt(qam_order)) # 16 -> 4
    square_len_per_bit = (MIN_MAX_COORDS[1] - MIN_MAX_COORDS[0]) / N
    indent_from_boundary = square_len_per_bit / 2
    xy_min = MIN_MAX_COORDS[0] + indent_from_boundary
    xy_max = MIN_MAX_COORDS[1] - indent_from_boundary
    centrals_xy = np.linspace(xy_min, xy_max, N)
    points = []
    [points.append([x,y]) for y in centrals_xy for x in centrals_xy]
    return points
