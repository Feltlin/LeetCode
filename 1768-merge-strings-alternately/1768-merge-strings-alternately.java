class Solution {
    public String mergeAlternately(String word1, String word2) {
        String merge = "";
        int l = Math.min(word1.length(), word2.length());
        for(int i = 0; i < l; ++i){
            merge = merge + word1.charAt(i) + word2.charAt(i);
        }
        return merge + word1.substring(l) + word2.substring(l);
    }
}