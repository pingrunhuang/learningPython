import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import numexpr as ne


class Particle:
    __slots__ = ('x', 'y', 'ang_vel') # reduce memory foot print

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class CounterClockParticleSimulator:

    TIMESTEP = 0.00001

    def __init__(self, ps):
        self.particles = ps
    

    def _simulate_python(self, dt:float)->None:
        nsteps = int(dt // self.TIMESTEP)
        for _ in range(nsteps):
            for p in self.particles:
                radius = (p.x**2+p.y**2)**0.5
                v_x = p.ang_vel * (-p.y / radius) # the negative symbol is because this is counter clock movement
                v_y = p.ang_vel * (p.x / radius)
                d_x = v_x * self.TIMESTEP
                d_y = v_y * self.TIMESTEP
                p.x += d_x
                p.y += d_y


    def _simulate_numpy(self, dt: float)->None:
        nsteps = int(dt//self.TIMESTEP)
        positions = np.array([[p.x, p.y] for p in self.particles])
        ang_vels = np.array([p.ang_vel for p in self.particles])

        for _ in range(nsteps):
            radius = np.sqrt((positions**2).sum(axis=1))
            v_i = positions[:,[1,0]] # the reason why we swap here is because the v_x is multiply by y and v_y by x
            v_i[:, 0] *= -1
            v_i[:,] /= radius[:, np.newaxis]
            d_i = self.TIMESTEP * ang_vels[:, np.newaxis] * v_i
            positions += d_i

        # release and update
        for i, p in enumerate(self.particles):
            p.x, p.y = positions[i]


    def _simulate_numexpr(self, dt: float)->None:
        nsteps = int(dt//self.TIMESTEP)
        positions = np.array([[p.x, p.y] for p in self.particles])
        ang_vels = np.array([p.ang_vel for p in self.particles])

        for _ in range(nsteps):
            radius_square = ne.evaluate('sum(positions**2, 1)')
            radius = ne.evaluate('sqrt(radius_square)')
            v_i = positions[:,[1,0]] # the reason why we swap here is because the v_x is multiply by y and v_y by x
            v_i[:, 0] *= -1
            v_i[:,] /= radius[:, np.newaxis]
            d_i = self.TIMESTEP * ang_vels[:, np.newaxis] * v_i
            positions += d_i

        # release and update
        for i, p in enumerate(self.particles):
            p.x, p.y = positions[i]


    def simulate(self, dt:float, method:str='python')->None:
        if method == 'python':
            return self._simulate_python(dt)
        elif method == 'numpy':
            return self._simulate_numpy(dt)
        elif method == 'numexpr':
            return self._simulate_numexpr(dt)
        else:
            raise ValueError("No corresponding method: {}".format(method))


def visualize(simulator:CounterClockParticleSimulator, time_window:float=0.01)->None:
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]
    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        simulator.simulate(time_window)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X, Y)
        return line, 

    anim = animation.FuncAnimation(fig, func=animate, init_func=init, blit=True, interval=10)
    plt.show()

# a pretty good idea of how to implement testing 
def test_simulate():
    particles = [Particle(0.3, 0.5, 1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, 3)]
    simulator = CounterClockParticleSimulator(particles)
    simulator.simulate(0.1, 'numpy')

    def fequal(a, b, eps=1e-5):
        return abs(a-b) < eps

    p0, p1, p2 = simulator.particles

    assert fequal(p0.x, 0.21027)
    assert fequal(p0.y, 0.54386)
    assert fequal(p1.x, -0.09933)
    assert fequal(p1.y, -0.49003)
    assert fequal(p2.x,  0.19133)
    assert fequal(p2.y, -0.36524)


def test_visualize():
    particles = [Particle(0.3, 0.5, 1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, 3)]
    simulator = CounterClockParticleSimulator(particles)
    visualize(simulator)


def benchmark(npart:int=100, method:str='python')->None:
    particles = [Particle(np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(npart)]
    simulator = CounterClockParticleSimulator(particles)
    simulator.simulate(0.1, method=method)


if __name__ == "__main__":
    benchmark(method='numexpr')