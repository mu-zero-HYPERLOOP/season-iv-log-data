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

file = "../Documents/muzero/logs/2024-6-17_21_37_29/";
_, airgap_left = read_csv(file + "levitation_board1/airgap_left.csv")
_, target_airgap_left = read_csv(file + "levitation_board1/target_airgap_left.csv")
_, p_term = read_csv(file + "levitation_board1/left_airgap_controller_p_term.csv")
_, i_term = read_csv(file + "levitation_board1/left_airgap_controller_i_term.csv")
_, d_term = read_csv(file + "levitation_board1/left_airgap_controller_d_term.csv")
_, output = read_csv(file + "levitation_board1/left_airgap_controller_output.csv")
_, l2_assert = read_csv(file + "levitation_board3/assertion_fault.csv")
_, state = read_csv(file + "mother_board/state.csv")
_, cmd = read_csv(file + "mother_board/command.csv")


_, output_i_left = read_csv(file + "levitation_board2/left_current_controller_output.csv")
_, output_i_right = read_csv(file + "levitation_board2/right_current_controller_output.csv")

_, l1_state = read_csv(file + "levitation_board1/state.csv")
_, l1_precharge = read_csv(file + "levitation_board1/precharge_status.csv")
_, l1_feedthrough = read_csv(file + "levitation_board1/feedthrough_status.csv")

_, l2_state = read_csv(file + "levitation_board2/state.csv")
_, l2_precharge = read_csv(file + "levitation_board2/precharge_status.csv")
_, l2_feedthrough = read_csv(file + "levitation_board2/feedthrough_status.csv")

_, l3_state = read_csv(file + "levitation_board3/state.csv")
_, l3_precharge = read_csv(file + "levitation_board3/precharge_status.csv")
_, l3_feedthrough = read_csv(file + "levitation_board3/feedthrough_status.csv")

_, l3_mcu = read_csv(file + "levitation_board3/mcu_temperature.csv")

_, lcmd = read_csv(file + "mother_board/levitation_command.csv")

_, vdc = read_csv(file + "levitation_board1/vdc_voltage.csv")


x = "timestamp"
# x = "mod_index"

plt.plot(d_term[x], d_term["value"], label="KdTerm")
plt.plot(airgap_left[x], airgap_left["value"], label="airgap")
plt.plot(target_airgap_left[x], target_airgap_left["value"], label="target")
plt.plot(output[x], output["value"], label="output")
plt.plot(i_term[x], i_term["value"], label="KiTerm")
plt.plot(p_term[x], p_term["value"], label="KpTerm")
# plt.plot(output_i_left[x], output_i_left["value"], label="V");
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
