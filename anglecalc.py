#
# Bounds the provided angle between [-180, 180) degrees.
# Ex. 360 becomes 0, 270 becomes -90, -450 becomes -90.
# @param angle Input angle in degrees.
# @return The bounded angle in degrees.
#
def boundTo180(angle):
  if angle >= -180 and angle < 180:
    return angle
  else:
    # Calculate bound angle (to 360) first
    bound_angle = angle % 360
    # If not already bound to 180, find new bound angle and return
    if bound_angle >= 180:
      return bound_angle - 360
    elif bound_angle < -180:
      return 360 - bound_angle
    else:
      return bound_angle

#
# Determines whether |middle_angle| is in the acute angle between the other two bounding angles.
# Note: Input angles are bounded to 180 for safety.
# Ex. -180 is between -90 and 110 but not between -90 and 80.
# @param first_angle First angle in degrees.
# @param middle_angle Middle angle in degrees.
# @param second_angle Second angle in degrees.
# @return Whether |middle_angle| is between |first_angle| and |second_angle| (exclusive).
#
def isAngleBetween(first_angle, middle_angle, second_angle):
  if first_angle < 0:
    first_angle += 360
  if second_angle < 0:
    second_angle += 360
  # Calculate angle difference
  angle_diff = abs(first_angle - second_angle)
  # Set acute angle (smaller angle)
  if angle_diff < (360 - angle_diff):
    acute_angle = angle_diff
  else:
    acute_angle = 360 - angle_diff
  # TODO

