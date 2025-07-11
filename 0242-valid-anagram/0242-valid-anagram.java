class Solution {
    public boolean isAnagram(String s, String t) {
        boolean isA = true;
        if(s.length() != t.length()){
            isA = false;
        }else{
            Map<Character, Integer> count = new HashMap<>();
            for(int i = 0; i < s.length(); ++i){
                count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0) + 1);
            }
            for(int i = 0; i < t.length() && isA; ++i){
                count.put(t.charAt(i), count.getOrDefault(t.charAt(i), 0) - 1);
                if(count.get(t.charAt(i)) == -1){
                    isA = false;
                }
            }
        }
        return isA;
    }
}