import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

# Настройка шрифта
mpl.rcParams['font.size'] = 18


# Получение информации
def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std ** .5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])

    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand() * 10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y


student = 7

x_data, y_data = fake_data_generator(get_numbers(student))

# Настройка графика
plt.figure(figsize=(9, 8))
plt.tight_layout()

plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)
plt.minorticks_on()

plt.title("Fake graph")
plt.xlabel(r"$\xi, cm$")
plt.ylabel(r"$\rho, mm^{-3}$")
plt.ylim(-30, 30)
plt.xlim(-6, 16)

# Построение данных с погрешностями
y_error = abs(y_data) ** 0.5
x_error = 0.1
plt.errorbar(x_data, y_data, xerr=x_error, yerr=y_error, fmt='g.', label="Fake data")
# Ошибка по оси X не видна из за размера точек

# Построение средних значений по осям
mean_x = sum(x_data) / len(x_data)
mean_y = sum(y_data) / len(y_data)
plt.plot(np.array([mean_x] * 2), np.array([-30, 30]), 'b--', label=f'Mean x = {mean_x}')
plt.plot(np.array([-6, 16]), np.array([mean_y] * 2), 'r-.', label=f'Mean y = {round(mean_y, 1)}')

# Построение примерной прямой
plt.plot(np.array([16, -6]), np.array([-23.4, 23.9]), 'black', label='Fit')

# Точка пересечения прямых
plt.plot(4.9, 0.5, 'b^')

# Легенда
plt.legend(loc='upper right')

# Сохранение
plt.savefig("Data analysis.jpg")
