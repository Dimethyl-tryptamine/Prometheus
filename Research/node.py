# Researching node constructors and tools for modifying
# Prometheus' adaptive tree architecture

import random


class Node:

    def __init__(self, node_id, input_value):

        # Identity
        self.id = node_id

        # Connections
        self.parents = []
        self.children = []

        # Memory
        self.history = []

        # State
        self.value = input_value
        self.sensitivity = len(self.parents) * self.history * self.value

        # Exploration
        self.randomness = random.uniform(-1, 1)

    def snapshot(self):

        self.history.append({
            "value": self.value,
            "sensitivity": self.sensitivity
        })


    def compare_last(self):

        if len(self.history) < 2:
            return None

        previous = self.history[-2]
        current = self.history[-1]

        value_change = (
            current["value"] -
            previous["value"]
        )

        sensitivity_change = (
            current["sensitivity"] -
            previous["sensitivity"]
        )

        return value_change, sensitivity_change
    def update(self, input_value):

        memory_effect = 1

        if len(self.history) > 0:
            average = sum(
                x["value"] for x in self.history
            ) / len(self.history)

            memory_effect = average


        self.value = (
            input_value *
            self.sensitivity *
            memory_effect
        )


        self.snapshot()


    def __repr__(self):
        return f"Node({self.id},  value={self.value}, sensativity={self.sensitivity})"