// Clamp a number to the range [lo, hi]. Swaps the bounds if they are given the wrong way round.
export function clamp(value, lo, hi) {
  if (lo > hi) [lo, hi] = [hi, lo];
  return Math.min(Math.max(value, lo), hi);
}
