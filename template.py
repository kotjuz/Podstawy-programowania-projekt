import random

class BoardTemplates:
    def __init__(self):
        self.templates = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, "S",
            11, "S", "S", "S", "S", 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, "S", 30,
            31, 32, "S", 34, 35, 36, 37, 38, "S", 40,
            41, 42, "S", 44, 45, 46, 47, 48, 49, 50,
            "S", 52, "S", 54, 55, "S", "S", 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, 75, "S", 77, 78, 79, 80,
            81, "S", 83, 84, 85, 86, 87, 88, 89, 90,
            91, "S", 93, 94, "S", 96, "S", "S", "S", 100],

            [1, 2, 3, 4, "S", 6, 7, 8, 9, "S",
            "S", 12, 13, "S", 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, "S", 33, 34, 35, 36, "S", 38, 39, "S",
            41, "S", 43, 44, 45, 46, "S", 48, 49, 50,
            51, "S", 53, 54, 55, 56, "S", 58, 59, 60,
            61, "S", 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, "S", "S", "S", 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, "S", "S",
            91, "S", "S", 94, "S", 96, 97, 98, 99, 100],

            [1, "S", 3, 4, 5, "S", 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, "S", "S", "S", "S",
            21, 22, "S", "S", 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, "S", 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, "S", 50,
            51, "S", "S", "S", 55, 56, 57, 58, "S", 60,
            61, 62, 63, 64, 65, 66, 67, 68, "S", 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, "S", "S", 85, 86, 87, 88, 89, 90,
            91, "S", 93, 94, 95, 96, 97, "S", "S", 100],

            [1, 2, 3, 4, 5, "S", "S", 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            "S", 22, 23, 24, 25, 26, 27, "S", "S", "S",
            "S", 32, 33, "S", 35, 36, 37, 38, 39, 40,
            "S", 42, 43, 44, 45, 46, 47, 48, 49, 50,
            "S", 52, 53, 54, 55, "S", 57, "S", "S", 60,
            61, 62, 63, 64, "S", 66, 67, 68, 69, 70,
            71, 72, "S", 74, 75, 76, 77, 78, 79, "S",
            81, 82, "S", 84, 85, 86, 87, 88, 89, 90,
            91, 92, 93, 94, 95, 96, "S", "S", "S", 100],

            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, "S", "S", "S", 15, 16, 17, 18, 19, "S",
            21, 22, 23, 24, 25, 26, "S", 28, 29, 30,
            31, 32, 33, 34, 35, 36, "S", 38, 39, 40,
            41, 42, "S", 44, 45, 46, 47, 48, 49, 50,
            51, 52, "S", 54, 55, "S", 57, 58, 59, "S",
            "S", 62, 63, 64, 65, 66, 67, 68, 69, "S",
            71, 72, "S", 74, 75, "S", "S", 78, 79, "S",
            81, 82, 83, 84, 85, 86, 87, 88, 89, "S",
            91, "S", "S", "S", 95, 96, 97, 98, 99, 100]

        ]

        self.ships_placement = [
            [[12,13,14,15], [33,43,53], [97,98,99], [29,39], [56,57], [82,92], [10], [51], [76], [95]],
            [[32, 42, 52, 62], [37, 47, 57], [75, 76, 77], [5, 14], [92, 93], [89, 90], [10], [11], [40], [95]],
            [[17, 18, 19, 20], [52, 53, 54], [49, 59, 69], [23, 24], [83, 84], [98, 98], [2], [6], [37], [92]],
            [[21, 31, 41, 51], [28, 29, 30], [97, 98, 99], [6, 7], [58, 59], [73, 83], [34], [56], [65], [80]],
            [[60, 70, 80, 90], [92, 93, 94], [12, 13, 14], [27, 37], [43, 53], [76, 77], [20], [61], [73], [56]]
        ]
    def get_random_template(self):
        return random.choice(self.templates)

    def get_ships_placement(self, template):
        return self.ships_placement[self.templates.index(template)]