# Researching node constructors and tools for modifying
# Prometheus' adaptive tree architecture


class Node:
    def __init__(self, id, value, parent=None):
        self.id = id
        self.value = value

        self.parent = parent
        self.children = []

        self.depth = self.calculate_depth()

        # Placeholder until learning rules exist
        self.error_history = 0
        self.usage_variance = 0

        self.change_rate = self.calculate_change_rate()


    def calculate_depth(self):
        depth = 0
        current = self.parent

        while current:
            depth += 1
            current = current.parent

        return depth


    def calculate_change_rate(self):
        return (
            self.depth * 0.1
            + self.error_history
            + self.usage_variance
        )


    def add_child(self, child):
        self.children.append(child)


    def split(self, child_count):
        """
        Divide this node's value into child nodes
        while maintaining total value.
        """

        child_value = self.value / (child_count + 1)

        # keep some value at parent
        self.value = child_value

        for i in range(child_count):
            child = Node(
                id=f"{self.id}_{i}",
                value=child_value,
                parent=self
            )

            self.add_child(child)

