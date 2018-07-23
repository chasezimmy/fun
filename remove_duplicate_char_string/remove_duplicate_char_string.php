<?php
// Remove Duplicate Character in String

class Solution {

    public function removeDuplicate($string) {
        $char_in_string = [];
        $seen = [];
        $chars = str_split($string);

        foreach($chars as $char) {
            if (!isset($seen[$char])) {
                $char_in_string[] = $char;
                $seen[$char] = 1;
            }
        }

        return $char_in_string;
    }

}

$string = "Tree Traversal";
$sol = new Solution();
print implode('',$sol->removeDuplicate($string));
