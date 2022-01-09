#! /usr/bin/python3
#[1] C. Wang, H. Nilsson, J. Yang, et al. 1D-3D coupling for hydraulic system transient simulations. Computer Physics Communications, 210:1–9, 2017

from nutils import mesh, function, solver, export, cli
from nutils.expression_v2 import Namespace
import numpy, itertools, treelog

def main (nelems=800, timestep=0.005, refdensity=1e3, refpressure=101325., psi=1e-6, viscosity=1e-3, theta = 1.0):
  
  domain, geom = mesh.rectilinear([numpy.linspace(0, 1000, nelems+1)])

  bezier = domain.sample('bezier', 2)

  ns = Namespace()
  ns.x = geom
  ns.δ = function.eye(domain.ndims)
  ns.define_for('x', gradient='∇', normal='n', jacobians=('dV', 'dS'))
  ns.ρref = refdensity
  ns.pref = refpressure
  ns.pin = 91800
  ns.μ = viscosity
  ns.ψ = psi
  ns.ρbasis = domain.basis('std', degree=1) #basis function for density
  ns.ubasis = domain.basis('std', degree=2).vector(domain.ndims) #basis function for velocity
  
  #using the formula for shape function for mass and momentum conservation 
  ns.ρ = function.dotarg('ρ', (ns.ρbasis + ns.ρref)) # density is shifted by ref density
  ns.u = function.dotarg('u', ns.ubasis)
  
  ns.p = 'pref + (ρ - ρref) / ψ' # pressure-density connection, see equ (8) of [1]
  
  #https://en.wikipedia.org/wiki/Derivation_of_the_Navier%E2%80%93Stokes_equations
  #the stress tensor is completely defined in the wikipedia derivation
  ns.σ_ij = 'μ (∇_j(u_i) + ∇_i(u_j)) - p δ_ij' # diffusive term (incompressible) and pressure gradient
  ns.h = 1 / nelems
  ns.k = 'ρ h / μ' # needs work, stabilization coefficient

  #mass conservation
  ρres = domain.integral('ρbasis_n (∇_k(ρ u_k)) dV' @ ns, degree=4)
  #momentum conservation
  ures = domain.integral('(ubasis_ni ∇_j(ρ u_i u_j) + ∇_j(ubasis_ni) σ_ij) dV' @ns, degree=4)
  
  #accounting the boundary condition for pressure at inlet: pin=91800
  ures += domain.boundary['left'].integral('pin ubasis_ni n_i dS' @ns, degree=4)
  t = 0
  lhsu = numpy.zeros(ures.shape)
  lhsρ = numpy.zeros(ρres.shape)
  #open a file for 
  f = open("watchpoint.txt", "w")

  sqr = domain.boundary['right'].integral('(u_0 - 1)^2 dS' @ ns, degree=4)
  ucons0 = solver.optimize('u', sqr, droptol=1e-14)
  cons = dict(u=ucons0)

  #time derivative term from mass and momentum conservation as inertia
  uinertia = domain.integral('ubasis_ni ρ u_i dV' @ns, degree=9)
  ρinertia = domain.integral('ρbasis_n ρ dV' @ns, degree=9)

  with treelog.iter.plain('timstep', solver.impliciteuler(('u', 'ρ'),\
     residual = (ures, ρres), inertia=(uinertia, ρinertia), constrain=cons,\
       arguments=dict(u=lhsu, ρ=lhsρ), timestep=timestep, newtontol=1e-8)) as steps:
    for istep, state in enumerate(steps):
      t = istep * timestep

      x, p, ρ, u = bezier.eval(['x_i', 'p', 'ρ', 'u_i'] @ ns, **state)
      f.write("%e; %e; %e\n" % (t, p[1599], u[799]))
      f.flush()

      if t>=20:
        break

  f.close()


main()  