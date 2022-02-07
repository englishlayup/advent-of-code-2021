import numpy as np

if __name__ == '__main__':
    with open('day3.in') as f:
        diag_reports = f.read().splitlines()

    bit_matrix = np.array([list(map(int, report)) for report in diag_reports])

    gamma_rate = ''
    epsilon_rate = ''

    for col in range(bit_matrix.shape[1]):
        count_ones = len(bit_matrix[bit_matrix[:, col] == 1])
        count_zeros = len(bit_matrix[bit_matrix[:, col] == 0])

        gamma_rate += '1' if count_ones > count_zeros else '0'
        epsilon_rate += '0' if count_ones > count_zeros else '1'

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))

    oxi_gen_rate = bit_matrix.copy()
    CO2_scrub_rate = bit_matrix.copy()

    for col in range(bit_matrix.shape[1]):
        count_ones = len(oxi_gen_rate[oxi_gen_rate[:, col] == 1])
        count_zeros = len(oxi_gen_rate[oxi_gen_rate[:, col] == 0])

        if len(oxi_gen_rate) > 1:
            oxi_gen_rate = oxi_gen_rate[oxi_gen_rate[:, col] == 1] if count_ones >= count_zeros \
                else oxi_gen_rate[oxi_gen_rate[:, col] == 0]

    for col in range(bit_matrix.shape[1]):
        count_ones = len(CO2_scrub_rate[CO2_scrub_rate[:, col] == 1])
        count_zeros = len(CO2_scrub_rate[CO2_scrub_rate[:, col] == 0])

        if len(CO2_scrub_rate) > 1:
            CO2_scrub_rate = CO2_scrub_rate[CO2_scrub_rate[:, col] == 0] if count_ones >= count_zeros \
                else CO2_scrub_rate[CO2_scrub_rate[:, col] == 1]

    oxi_gen = ''
    for bit in list(map(str, oxi_gen_rate[0])):
        oxi_gen += bit

    CO2_scrub = ''
    for bit in list(map(str, CO2_scrub_rate[0])):
        CO2_scrub += bit

    print(int(oxi_gen, 2) * int(CO2_scrub, 2))
