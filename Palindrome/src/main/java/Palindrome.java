public class Palindrome {

    public static boolean isPalindrome(String text) {

        String cleaned = text.replaceAll("[^a-zA-Z0-9]", "")
                .toLowerCase();

        String reversed = new StringBuilder(cleaned)
                .reverse()
                .toString();


        return cleaned.equals(reversed);

    }
}
