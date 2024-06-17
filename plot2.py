import pandas as pd

import os
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

import matplotlib.style as mplstyle
mplstyle.use('fast')

import matplotlib as mpl

mpl.rcParams['path.simplify'] = True
mpl.rcParams['path.simplify_threshold'] = 1.0

def read_csv(file_path):
    data = defaultdict(list)
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        headers = next(reader)
        print(headers)
        for row in reader:
            for header, value in zip(headers, row):
                if headers == "timestamp" :
                    data[header].append(float(value));
                else:
                    try:
                        data[header].append(float(value));
                    except:
                        data[header].append(value);
    return headers, data

file = "../Documents/muzero/logs/2024-6-17_20_5_23/";
_, l1 = read_csv(file + "levitation_board1/airgap_left.csv")
_, r1 = read_csv(file + "levitation_board1/airgap_right.csv")
_, l2 = read_csv(file + "levitation_board2/airgap_left.csv")
_, r2 = read_csv(file + "levitation_board2/airgap_right.csv")
_, l3 = read_csv(file + "levitation_board3/airgap_left.csv")
_, r3 = read_csv(file + "levitation_board3/airgap_right.csv")


_, vdc = read_csv(file + "levitation_board1/vdc_voltage.csv")


x = "timestamp"
# x = "mod_index"

plt.plot(l1[x], l1["value"], label="l1")
plt.plot(r1[x], r1["value"], label="r1")
plt.plot(l2[x], l2["value"], label="l2")
plt.plot(r2[x], r2["value"], label="r2")
plt.plot(l3[x], l3["value"], label="l3")
plt.plot(r3[x], r3["value"], label="r3")
# plt.plot(state[x], state["value"], label="state")
# plt.plot(cmd[x], cmd["value"], label="command")
# plt.plot(l1_state[x], l1_state["value"], label="l1_state")
# plt.plot(l1_precharge[x], l1_precharge["value"], label="l1_precharge")
# plt.plot(l1_feedthrough[x], l1_feedthrough["value"], label="l1_feedthrough")


# plt.plot(l2_state[x], l2_state["value"], label="l2_state")
# plt.plot(l2_precharge[x], l2_precharge["value"], label="l2_precharge")
# plt.plot(l2_feedthrough[x], l2_feedthrough["value"], label="l2_feedthrough")
#
# plt.plot(l3_state[x], l3_state["value"], label="l3_state")
# plt.plot(l3_precharge[x], l3_precharge["value"], label="l3_precharge")
# plt.plot(l3_feedthrough[x], l3_feedthrough["value"], label="l3_feedthrough")
#
# plt.plot(lcmd[x], lcmd["value"], label="levitation_command")
# plt.plot(vdc[x], vdc["value"], label="vdc")

# plt.plot(l3_mcu[x], l3_mcu["value"], label="mcu_temperature")

# plt.plot(output_i_left[x], output_i_left["value"], label="current_output_left")
# plt.plot(output_i_right[x], output_i_right["value"], label="current_output_right")

# plt.plot(l2_assert[x], l2_assert["value"], label="current_output_right")

plt.xlabel(x)
plt.legend()
plt.show();
