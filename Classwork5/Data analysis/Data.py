import numpy as np
import matplotlib
from matplotlib import pyplot as plt


# Получение данных
def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3


def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
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

# Настройки графика
plt.figure(figsize=(9, 8))
plt.tight_layout()
matplotlib.rcParams['font.size'] = 17

plt.grid(visible=True, which='major', axis='both', alpha=1)
plt.grid(visible=True, which='minor', axis='both', alpha=0.5)
plt.minorticks_on()

plt.title("Fake graph")
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.ylim(-22, 25)
plt.xlim(-6, 16)

# Построение данных
plt.scatter(x_data, y_data, label='Fake data')

# Построение прямой
fit = np.polyfit(x_data, y_data, deg=1)
poly = np.poly1d(fit)
xpoly = np.linspace(-5, 15, 1000)
plt.plot(xpoly, poly(xpoly), 'r-', label='Fit')

# Метод наименьших квадратов
b = (np.mean(x_data * y_data) - np.mean(x_data) * np.mean(y_data)) / (np.mean(x_data ** 2) - np.mean(x_data) ** 2)
a = np.mean(y_data) - b * np.mean(x_data)
y_mnk = x_data * b + a
plt.plot(x_data, y_mnk, 'y--', label="МНК")

# Легенда
plt.legend()

# Сохранение
plt.savefig('Fake data.jpg')
