import numpy as np
import csv


class Dice:

    def __init__(self, faces):
        self.faces = faces
        self._n = len(self._faces)
        self.current_face = -1
        self.roll()

    @property
    def faces(self):
        return self._faces

    @faces.setter
    def faces(self, face_arr):
        if len(face_arr) < 3:
            raise ValueError('Dice should have 3 or more faces')

        if any([type(face) != int for face in face_arr]):
            raise TypeError('Dice faces should be integer value.')

        self._faces = face_arr

    def roll(self):
        random_pos = np.random.randint(self._n)
        self.current_face = self._faces[random_pos]
        return self.current_face


class Coin:
    def __init__(self):
        pass


def main():
    means = list()
    d = Dice()
    ITER_NUM = 5_000_000

    for j in range(ITER_NUM):

        if j % 500_000 == 0:
            print(j, round(j / ITER_NUM, 2))

        res = np.zeros(25, np.int64)
        for i in range(25):
            res[i] = d.roll()

        means.append([np.mean(res), res])

    with open('./data/dice_25rolls.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['avg', 'result'])
        writer.writerows(means)


#if __name__ == '__main__':
#    main()

#%%
