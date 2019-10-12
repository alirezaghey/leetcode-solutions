// https://leetcode.com/problems/distance-between-bus-stops/
// Related Topics: Array
// Difficulty: Easy

/*
Initial thoughts:
The problem boils down to calculating the sum of the values between
start and destination while moving forward and destination and start while also
moving forward and circling back to the beginning of the distance array
to reach start from behind (imagine the distance array as a circular linked list)
The result is the minimum sum of of the two calculations above.
To avoid going out of index when we move forward from destination to start, we use the
modulus operator.

Time complexity: O(n) where n === len(distance)
Space complexity: O(1)
*/

/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
  let s = start;
  let d = destination;
  let cwise = (ccwise = 0);

  while (s !== destination) {
    cwise += distance[s];
    s = (s + 1) % distance.length;
  }

  while (d !== start) {
    ccwise += distance[d];
    d = (d + 1) % distance.length;
  }

  return Math.min(cwise, ccwise);
};
