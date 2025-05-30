class Solution {
    public char findTheDifference(String s, String t) {
        Map<Character, Integer> count = new HashMap<>();
        char extra = ' ';
        for(int i = 0; i < s.length(); ++i){
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0) + 1);
        }
        for(int i = 0; i < t.length(); ++i){
            count.put(t.charAt(i), count.getOrDefault(t.charAt(i), 0) - 1);
            if(count.get(t.charAt(i)) == -1){
                extra = t.charAt(i);
            }
        }
        return extra;
    }
}