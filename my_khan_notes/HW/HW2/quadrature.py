#!/usr/bin/python
# Object for decoding/estimating Quadrature decodings.
# Framework by: Jason Ziglar <jpz@vt.edu>

class QuadratureEstimator:
  def __init__(self, ticks_per_revolution):
    self.ticks_per_revolution = ticks_per_revolution
    self._position = 0
    self._velocity = 0
  def update(self, a_state, b_state, time):
    # Implement decoding here. Note you'll remove the pass statement once you start implementing this
    pass

  @property
  def position(self):
      return self._position
  @property
  def velocity(self):
      return self._velocity

