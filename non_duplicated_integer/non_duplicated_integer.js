/*
 *	Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
 *
 *	For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
 *
 */
 
class Solution {
	nonDuplicatedInt(array) {
		var duplicates = {};

		array.forEach(element => {
			if (element in duplicates) {
				duplicates[element] += 1;
			} else {
				duplicates[element] = 1;
			}
		});

		for (var key in duplicates) {
			if (duplicates[key] == 1) {
				return duplicates[key];
			}
		}

		return;
	}
}

sol = new Solution();
console.log(sol.nonDuplicatedInt([13,19,13,13]));