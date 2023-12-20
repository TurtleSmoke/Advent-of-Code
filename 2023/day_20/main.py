#!/usr/bin/env python
import itertools
import math
import re
from collections import defaultdict

input_file = "input"

input_modules = {
    name: (type, destinations.split(", "))
    for type, name, destinations in re.findall(r"([%&]?)(\w+) -> (.*)", open(input_file).read())
}
input_conjunctions = defaultdict(dict)
for source, (_, dst) in input_modules.items():
    for d in dst:
        input_conjunctions[d][source] = 0


def play_sequence(modules, conjonctions, stop_at=None):
    pulse_counts = [0, 0]
    flips = defaultdict(int)
    source_rx = next(src for src, (_, destinations) in modules.items() if "rx" in destinations)
    rx_ins = {i: 0 for i in conjonctions[source_rx]}

    for i in itertools.count(1):
        if stop_at is not None and i == stop_at + 1:
            return math.prod(pulse_counts)

        if stop_at is None and all(rx_ins.values()):
            return math.lcm(*rx_ins.values())

        queue = [("", "broadcaster", 0)]
        while queue:
            previous_module, current_module, pulse_in = queue.pop(0)
            pulse_counts[pulse_in] += 1

            if current_module not in modules:
                continue

            module_type, destinations = modules[current_module]
            match module_type, pulse_in:
                case "", _:
                    pulse_out = pulse_in
                case "%", 0:
                    flips[current_module] = not flips[current_module]
                    pulse_out = flips[current_module]
                case "&", _:
                    conjonctions[current_module][previous_module] = pulse_in
                    pulse_out = not all(conjonctions[current_module].values())
                    if pulse_out and current_module in rx_ins and rx_ins[current_module] == 0:
                        rx_ins[current_module] = i
                case _, _:
                    continue

            for destination in destinations:
                queue.append((current_module, destination, pulse_out))


print(play_sequence(input_modules, input_conjunctions.copy(), 1000))
print(play_sequence(input_modules, input_conjunctions.copy()))
