# init: gaussian distro
# goes in Particle
def guassian_distro():
   if(len(self.average_velocity) != len(self.thermal_speed)):
      return -1 # throw error
   velocity_components = []
   for dimension in xrange(self.dimensions):
      r1, r2 = ourRandom(), ourRandom()
      velocity_components.append(self.average_velocity[dimension] - math.cos(2*math.pi*r2)*self.thermal_speed[dimension]*math.log(math.sqrt(r1)))


# gather source (charge density)
# goes in Particle
def gatherSource():
   w = []
   for dimension in xrange(self.dimensions):
      cell_corner = math.floor(self.position[dimension])
      cell_corner_next = cell_corner+1 # need to adjust ixp if using PBC
      w.append((cell_corner_next - self.position[dimension]), self.position[dimension] - cell_corner) # weights from left to right on cell
   for x in xrange(pow(2,self.dimensions)):
      delta_rho = self.charge
      for dimension in xrange(self.dimensions):
         delta_rho *= w[dimension][int(bin(x)[dimension])] # floor(x/2) for determining if left or right on cell weights.
      self.space.corners[self.calculateCorner()].rho += delta_rho

# mesh over-relax to find new potential; then calc E-field
err = 1.e-5; # convergence parm
w = 1.2; # over-relax parm
for cnt in range(0:100)
   loop over cells
      i = xcell; j = ycell;
      ip = i + 1; im = i - 1; jp = j + 1; jm = j - 1;
# need to adjust ixp and jyp if using PBC
      potnew[i,j] =
w*.25*(pot[ip,j]+pot[i,jp]+pot[im,j]+pot[i,jm]+rho[i,j])+(1-w)*pot[i,j];
   devmax = 0;
   loop over cells
      i = xcell; j = ycell;
      devmax = max(devmax,abs(potnew[i,j]-pot[i,j]));
      pot[i,j] = potnew[i,j];
   if (devmax < err) break
# calc e-field
loop over cells
   i = xcell; j = ycell;
   ip = i + 1; im = i - 1; jp = j + 1; jm = j - 1;
# need to adjust ixp and jyp if using PBC
   ex[i,j] = .5*(pot[im,j]-pot[ip,j]);
   ey[i,j] = .5*(pot[i,jm]-pot[i,jp]);

# push and move
loop over types
   mk = m[type];
   qk = q[type];
   loop over particles
      xj = x[j]; yj = y[j];
      ix = floor(xj); jy = floor(yj); ixp=ix+1; jyp=jy+1;
# need to adjust ixp and jyp if using PBC
      wl = ixp-xj; wu = jyp-yj; wr = xj-ix; wb = yj-jy;
      exj = wl*wb*ex[ix,jy] + wr*wb*ex[ixp,jy] + wl*wu*ex[ix,jyp] +
wr*wu*ex[ixp,jyp]; eyj = wl*wb*ey[ix,jy] + wr*wb*ey[ixp,jy] +
wl*wu*ey[ix,jyp] + wr*wu*ey[ixp,jyp]; axj = qk*exj/mk; ayj = qk*eyj/mk;
      vx[j] += axj*dt; vy[j] += ayj*dt;
      x[j] += vx[j]*dt; y[j] += vy[j]*dt;
# need to adjust x[j] and y[j] if using PBC

# accumulate diagnostics
energyField = 0;
loop over cells
   i = xcell; j = ycell;
   energyField += ex[i,j]^2 + ey[i,j]^2;
energyParticles = 0;
loop over types
   mk = m[type];
   loop over particles
      energyParticles += .5*mk*(vx[j]^2 + vy[j]^2);
#need 2D FFT on pot to follow modes
