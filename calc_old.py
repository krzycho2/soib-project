import numpy as np
import scipy
from scipy.stats import norm
from scipy.integrate import dblquad
import random
import matplotlib.pyplot as plt

QAM_M_VALUE = 16
MAX_POINT = (1,1)

def calculate_mer_single(points, correct_point):
    diff_points = points - correct_point
    return np.log10(calculate_power(points) / calculate_power(diff_points))


def calculate_power(points):
    points = np.array(points)
    return np.sum(points**2) / len(points)

def calculate_constellation_power():
    qam_points = np.array(get_all_qam_points())
    N = np.sqrt(QAM_M_VALUE)
    return np.sum(qam_points**2) / N

def generate_gauss2d_points(central_point, sigma, n_points):
    """
    Return 2 arrays: xs and ys.
    """
    mean = list(central_point)
    cov = [[sigma**2,0], [0,sigma**2]]
    return np.random.multivariate_normal(mean, cov, n_points)

def calculate_ber_single(points, correct_point):
    x0,x1,y0,y1 = get_boundary(correct_point)

    xx_in_boundary = np.logical_and(points[:,0] >= x0, points[:,0] <= x1)
    yy_in_boundary = np.logical_and(points[:,1] >= y0,points[:,0] <= y1)
    points_in_boundary = np.sum(np.logical_and(xx_in_boundary, yy_in_boundary))

    n_points = len(points)
    return (n_points - points_in_boundary) / n_points

def get_all_qam_points():
    N = int(np.sqrt(QAM_M_VALUE)) # 4
    boundary_len = 1 / N
    x0 = boundary_len / 2
    y0 = x0
    points = []
    
    for j in range(N):
        for i in range(N):
            x = x0 + i*boundary_len
            y = y0 + j*boundary_len
            points.append((x,y))

    return points


def get_boundary(point):
    N = np.sqrt(QAM_M_VALUE)
    max_a = 1
    a = max_a / N / 2
    return point[0]-a, point[0]+a, point[1]-a, point[1]+a
    # return (point[0]-a, point[1]-a), (point[0]+a, point[1]-a), (point[0]-a, point[1]+a), (point[0]+a, point[1]+a)


def gauss_pdf(x, loc, scale):
    return norm.pdf(x, loc, scale)

# def plot_sig_mer():
mers = []
bers = []
sigmas = np.logspace(-5,-1,100)
for i in range(len(sigmas)):
    sigma = sigmas[i]
    if i % 10 == 0:
        print('Sigma nr ',i)

    correct = (0.5,0.5)
    points = generate_gauss2d_points(correct, sigma, int(1e6))
    # ber = calculate_ber_single(points, correct)
    mer = calculate_mer_single(points, correct)
    mers.append(mer)
    # bers.append(ber)

plt.plot(sigmas, mers, 'ro')
# plt.yscale('log')
plt.show()
    # print(sig,mer)