# Return True if the given string contains an appearance of "xyz" 
# where the xyz is not directly preceeded by a period (.). 
# So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True


def xyz_there(str):
  if 'xyz' and '.xyz' in str:
    return str.count('xyz')>str.count(".")
  return "xyz" in str and not ".xyz" in str

