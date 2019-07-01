import numpy as np
import math


def not_prime(n):
    if n == 2:
        return False
    if n % 2 == 0 or n <= 1:
        return True

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return True
    return False


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


"""
def compute_route_length(cities_coordinates, santas_route):
    
    Compute the length of the specified santas_route according to the coordinates specified in cities_coordinates AFTER
    adding North Pole (CityID = 0) at the beginning and at the end of the Path.
    :param cities_coordinates: df that contains the cities' X and Y coordinates
    :param santas_route: Path that DO NOT contain North Pole at the beginning and at the end
    :return:
    
    santas_route = np.concatenate(([0], santas_route, [0]))
    route_length = compute_route_with_north_pole_length(cities_coordinates, santas_route)
    return route_length


def compute_route_with_north_pole_length(cities_coordinates, santas_route):
    
    Compute the length of the specified santas_route according to the coordinates specified in cities_coordinates
    :param cities_coordinates: df that contains the cities' X and Y coordinates
    :param santas_route: Path that DO contain North Pole at the beginning and at the end
    :return:
    
    df = cities_coordinates.copy()
    df = df.loc[santas_route].reset_index()
    df = df.rename(columns={'index': 'CityId'})
    df['dist'] = np.sqrt((df.X - df.X.shift()) ** 2 + (df.Y - df.Y.shift()) ** 2)
    df = df.drop(0)
    idx = (df.index % 10 == 0)
    idx = df.loc[idx].CityId.apply(not_prime)
    idx = idx.index[idx.values]
    df.loc[idx, 'dist'] = df.loc[idx, 'dist'] + df.loc[idx, 'dist'] / 10
    # print(df)
    return np.sum(df['dist'])
"""


def compute_route_length(r, c, not_primes_bool):
    r = np.concatenate(([0], r))
    c = c[r, :]
    cs = np.roll(c, -1, axis=0)
    cid = cs[:, 0].astype(int)
    d = np.sqrt((c[:, 1] - cs[:, 1]) ** 2 + (c[:, 2] - cs[:, 2]) ** 2)
    idx = np.arange(9, len(c), 10)
    pc = cid[idx]
    sel = (idx + 1)[not_primes_bool[pc]]
    d[sel - 1] *= 1.1

    return np.sum(d)
